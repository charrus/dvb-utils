#!/usr/bin/python3

import re

class EITParser:


    def __init__(self):
        self.muxes = {}
        self.eits = {}
    
    def parse(self, file):
        re_sub = re.compile(r'.*"epggrab" subscribing to mux \"([^"]+)"')
        re_epggrab = re.compile(r'.*epggrab: (.+) - (.*)$')
        re_unsub = re.compile(r'.*subscription: [0-9a-fA-F]{4}: "epggrab" unsubscribing')
        current_mux = None

        with open(file, 'rt') as f:
            for line in f.readlines():
                if not 'tvheadend' in line:
                    continue

                m_re_sub = re_sub.match(line)
                m_re_epggrab = re_epggrab.match(line)
                m_re_unsub = re_unsub.match(line)

                if m_re_sub:
                    mux_name = m_re_sub.group(1)
                    current_mux = EITMux(mux_name)
                elif m_re_epggrab:
                    if current_mux is None:
                        print('No subscription found for %s: %s' % (m_re_epggrab.group(1), line))
                    else:
                        eit_name = m_re_epggrab.group(1)
                        eit_result = m_re_epggrab.group(2)
                        grabber = EITGrabber(eit_name, eit_result)
                        current_mux.add_grabber(grabber)
                elif m_re_unsub:
                    self.muxes[current_mux.name] = current_mux
                else:
                    continue
    
class EITGrabber:

    def __init__(self, name, description):
        self.name = name
        self.description = description

class EITMux:

    def __init__(self, name):
        self.name = name
        self.grabbers = list()

    def add_grabber(self, grabber):
        self.grabbers.append(grabber)
        
# Demonstration and testing.
#
def main():
    import pprint

    muxes = EITParser()
    muxes.parse('/var/log/syslog.1')
    pprint.pprint(muxes.muxes)

if __name__ == '__main__':
    main()