#!/usr/bin/python3

import re
import pprint
import fileinput

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

for line in fileinput.input():

    m_re_sub = re_sub.match(line)
    m_re_epggrab = re_epggrab.match(line)
    m_re_unsub = re_unsub.match(line)

    if m_re_sub:
        current_mux = m_re_sub.group(1)
        if not muxes.get(current_mux):
            muxes[current_mux] = {}
    elif m_re_epggrab:
        if current_mux is None:
            print('No subscription found for %s: %s' % (m_re_epggrab.group(1), line))
        else:
            current_eit = m_re_epggrab.group(1)
            eit_result = m_re_epggrab.group(2)
            muxes[current_mux][current_eit] = eit_result
    elif m_re_unsub:
        current_mux = None
    else:
        next

pprint.pprint(muxes, width=120)

# Output:
#
# '10714.25H': {'EIT: DVB Grabber': 'data completion timeout for 10714.25H in DVB-S Network',
#                'UK: Freesat (EIT)': 'data completion timeout for 10714.25H in DVB-S Network'},
#  '10758.5V': {'EIT: DVB Grabber': 'data completion timeout for 10758.5V in DVB-S Network'},
#  '10773H': {'EIT: DVB Grabber': 'data completion timeout for 10773H in DVB-S Network',
#             'UK: Freesat (EIT)': 'data completion timeout for 10773H in DVB-S Network'},
#  '10788V': {'EIT: DVB Grabber': 'data completion timeout for 10788V in DVB-S Network'},
#  '10803H': {'EIT: DVB Grabber': 'data completion timeout for 10803H in DVB-S Network',
#             'UK: Freesat (EIT)': 'data completion timeout for 10803H in DVB-S Network'},
#  '10818V': {'EIT: DVB Grabber': 'data completion timeout for 10818V in DVB-S Network'},
#  '10847V': {'EIT: DVB Grabber': 'data completion timeout for 10847V in DVB-S Network'},
#  '10891H': {'EIT: DVB Grabber': 'data completion timeout for 10891H in DVB-S Network'},
#  '10906V': {'EIT: DVB Grabber': 'data completion timeout for 10906V in DVB-S Network'},
#  '10936V': {'EIT: DVB Grabber': 'data completion timeout for 10936V in DVB-S Network'},
#  '10964H': {'EIT: DVB Grabber': 'data completion timeout for 10964H in DVB-S Network'},
#  '11023.25H': {'EIT: DVB Grabber': 'data completion timeout for 11023.25H in DVB-S Network'},
#  '11082.25H': {'EIT: DVB Grabber': 'data completion timeout for 11082.25H in DVB-S Network'},
#  '11097V': {'EIT: DVB Grabber': 'data completion timeout for 11097V in DVB-S Network'},
#  '11112H': {'EIT: DVB Grabber': 'data completion timeout for 11112H in DVB-S Network'},
#  '11126.5V': {'EIT: DVB Grabber': 'data completion timeout for 11126.5V in DVB-S Network'},
#  '11225V': {'EIT: DVB Grabber': 'data completion timeout for 11225V in DVB-S Network'},
#  '11265V': {'EIT: DVB Grabber': 'data completion timeout for 11265V in DVB-S Network'},
#  '11307V': {'EIT: DVB Grabber': 'data completion timeout for 11307V in DVB-S Network'},
#  '11343V': {'EIT: DVB Grabber': 'data completion timeout for 11343V in DVB-S Network'},
#  '11344.5H': {'EIT: DVB Grabber': 'data completion timeout for 11344.5H in DVB-S Network'},
#  '11425H': {'EIT: DVB Grabber': 'data completion timeout for 11425H in DVB-S Network',
#             'UK: Freesat': 'data completion timeout for 11425H in DVB-S Network',
#             'UK: Freesat (EIT)': 'data completion timeout for 11425H in DVB-S Network'},
#  '11426.5V': {'EIT: DVB Grabber': 'data completion timeout for 11426.5V in DVB-S Network'},
#  '11479V': {'EIT: DVB Grabber': 'data completion timeout for 11479V in DVB-S Network'},
#  '11493.75H': {'EIT: DVB Grabber': 'data completion timeout for 11493.75H in DVB-S Network'},
#  '11508.5V': {'EIT: DVB Grabber': 'data completion timeout for 11508.5V in DVB-S Network'},
#  '11538V': {'EIT: DVB Grabber': 'data completion timeout for 11538V in DVB-S Network'},
#  '11552.75H': {'EIT: DVB Grabber': 'data completion timeout for 11552.75H in DVB-S Network'},
#  '11567.5V': {'EIT: DVB Grabber': 'data completion timeout for 11567.5V in DVB-S Network'},
#  '11582.25H': {'EIT: DVB Grabber': 'data completion timeout for 11582.25H in DVB-S Network'},
#  '11597V': {'EIT: DVB Grabber': 'data completion timeout for 11597V in DVB-S Network'},
#  '11670.75H': {'EIT: DVB Grabber': 'data completion timeout for 11670.75H in DVB-S Network'},
#  '11685.5V': {'EIT: DVB Grabber': 'data completion timeout for 11685.5V in DVB-S Network',
#               'UK: Freesat (EIT)': 'data completion timeout for 11685.5V in DVB-S Network'},
#  '11719.5H': {'EIT: DVB Grabber': 'data completion timeout for 11719.5H in DVB-S Network',
#               'UK: Freesat': 'data completion timeout for 11719.5H in DVB-S Network',
#               'UK: Freesat (EIT)': 'data completion timeout for 11719.5H in DVB-S Network'},
#  '11836.5H': {'EIT: DVB Grabber': 'data completion timeout for 11836.5H in DVB-S Network'},
#  '11914.5H': {'EIT: DVB Grabber': 'data completion timeout for 11914.5H in DVB-S Network'},
#  '11973V': {'EIT: DVB Grabber': 'data completion timeout for 11973V in DVB-S Network',
#             'UK: Freesat (EIT)': 'data completion timeout for 11973V in DVB-S Network'},
#  '12070.5H': {'EIT: DVB Grabber': 'data completion timeout for 12070.5H in DVB-S Network'},
#  '12129V': {'EIT: DVB Grabber': 'data completion timeout for 12129V in DVB-S Network',
#             'UK: Freesat (EIT)': 'data completion timeout for 12129V in DVB-S Network'},
#  '12363V': {'EIT: DVB Grabber': 'data completion timeout for 12363V in DVB-S Network',
#             'UK: Freesat (EIT)': 'data completion timeout for 12363V in DVB-S Network'},
#  '12382.5H': {'EIT: DVB Grabber': 'data completion timeout for 12382.5H in DVB-S Network'}}
