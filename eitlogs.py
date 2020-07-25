#!/usr/bin/python3

import re
import pprint

# subscription: 0141: "epggrab" subscribing to mux "11567.5V", weight: 4, adapter: "Montage Technology M88DS3103 #5 : DVB-S #0", network: "DVB-S Network", service: "Raw PID Subscription"
# epggrab: EIT: DVB Grabber - data completion timeout for 11567.5V in DVB-S Network
# subscription: 0141: "epggrab" unsubscribing

re_sub = re.compile(r'.*"epggrab" subscribing to mux \"([^"]+)"')
re_epggrab = re.compile(r'.*epggrab: (.+) - (.*)$')
re_unsub = re.compile(r'.*subscription: [0-9a-fA-F]{4}: "epggrab" unsubscribing')

muxes = {}
current_mux = None
eits = []
current_eit = None

# muxes = {"11567.5V": { "EIT: DVB Grabber": "data completion timeout for 11567.5V in DVB-S Network" }}

with open('/var/log/syslog', 'rt') as file:
    for line in file:

        m_re_sub = re_sub.match(line)
        m_re_epggrab = re_epggrab.match(line)
        m_re_unsub = re_unsub.match(line)

        if m_re_sub:
            current_mux = m_re_sub.group(1)
            if not muxes.get(current_mux):
                muxes[current_mux] = []
        elif m_re_epggrab:
            if current_mux is None:
                print('No subscription found for %s' % (m_re_epggrab.group(1)))
            else:
                current_eit = m_re_epggrab.group(1)
                eit_result = m_re_epggrab.group(2)
                muxes[current_mux].append({current_eit: eit_result})
        elif m_re_unsub:
            current_mux = None
        else:
            next

pprint.pprint(muxes, width=120)