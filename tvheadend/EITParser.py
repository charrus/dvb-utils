#!/usr/bin/python3

import re

class EITParser:

    def __init__(self):
        self.muxes = {}
        self.eits = {}
    
    def parse(self, file):
        current_mux = None
        current_eit = None

        re_sub = re.compile(r'.*"epggrab" subscribing to mux \"([^"]+)"')
        re_epggrab = re.compile(r'.*epggrab: (.+) - (.*)$')
        re_unsub = re.compile(r'.*subscription: [0-9a-fA-F]{4}: "epggrab" unsubscribing')

        for line in file:

            m_re_sub = re_sub.match(line)
            m_re_epggrab = re_epggrab.match(line)
            m_re_unsub = re_unsub.match(line)

            if m_re_sub:
                current_mux = m_re_sub.group(1)
                if not self.muxes.get(current_mux):
                    self.muxes[current_mux] = {}
            elif m_re_epggrab:
                if current_mux is None:
                    print('No subscription found for %s: %s' % (m_re_epggrab.group(1), line))
                else:
                    current_eit = m_re_epggrab.group(1)
                    eit_result = m_re_epggrab.group(2)
                    self.muxes[current_mux][current_eit] = eit_result
            elif m_re_unsub:
                current_mux = None
            else:
                next

# Demonstration and testing.
#
def demo():
    import fileinput
    import pprint

    muxes = EITParser()
    muxes.parse(fileinput.input())
    pprint.pprint(muxes.muxes)

if __name__ == '__main__':
    demo()