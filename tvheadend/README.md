# dvb-utils

## eitlogs.py

This parses tvheadend log files to summarize the results of EIT grabbers by mux

Typical usage is:

```
$ cat /var/log/syslog.1 /var/log/syslog | ./eitlogs.py
No subscription found for 11758H in DVB-S Network: Jul 24 21:24:58 vdr tvheadend[1296]: epggrab: 11758H in DVB-S Network - registerin
g mux for OTA EPG                                                                                                                    
                                                                                                                                     
No subscription found for 11626.5V in DVB-S Network: Jul 24 21:40:20 vdr tvheadend[1296]: epggrab: 11626.5V in DVB-S Network - regist
ering mux for OTA EPG                                                                                                                
                                                                                                                                     
No subscription found for 11719.5H in DVB-S Network: Jul 24 21:43:28 vdr tvheadend[1296]: epggrab: 11719.5H in DVB-S Network - regist
ering mux for OTA EPG                                                                                                                
                                                                                                                                     
No subscription found for 11973V in DVB-S Network: Jul 24 21:45:52 vdr tvheadend[1296]: epggrab: 11973V in DVB-S Network - registerin
g mux for OTA EPG                                                 

{'10714.25H': {'EIT: DVB Grabber': 'data completion timeout for 10714.25H in DVB-S Network',
               'UK: Freesat (EIT)': 'data completion timeout for 10714.25H in DVB-S Network'},
 '10758.5V': {'EIT: DVB Grabber': 'data completion timeout for 10758.5V in DVB-S Network'},
 '10773H': {'EIT: DVB Grabber': 'data completion timeout for 10773H in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 10773H in DVB-S Network'},
 '10788V': {'EIT: DVB Grabber': 'data completion timeout for 10788V in DVB-S Network'},
 '10803H': {'EIT: DVB Grabber': 'data completion timeout for 10803H in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 10803H in DVB-S Network'},
 '10818V': {'EIT: DVB Grabber': 'data completion timeout for 10818V in DVB-S Network'},
 '10847V': {'EIT: DVB Grabber': 'data completion timeout for 10847V in DVB-S Network'},
 '10891H': {'EIT: DVB Grabber': 'data completion timeout for 10891H in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 10891H in DVB-S Network'},
 '10906V': {'EIT: DVB Grabber': 'data completion timeout for 10906V in DVB-S Network'},
 '10936V': {'EIT: DVB Grabber': 'data completion timeout for 10936V in DVB-S Network'},
 '10964H': {'EIT: DVB Grabber': 'data completion timeout for 10964H in DVB-S Network'},
 '11023.25H': {'EIT: DVB Grabber': 'data completion timeout for 11023.25H in DVB-S Network'},
 '11082.25H': {'EIT: DVB Grabber': 'data completion timeout for 11082.25H in DVB-S Network'},
 '11097V': {'EIT: DVB Grabber': 'data completion timeout for 11097V in DVB-S Network'},
 '11112H': {'EIT: DVB Grabber': 'data completion timeout for 11112H in DVB-S Network'},
 '11126.5V': {'EIT: DVB Grabber': 'data completion timeout for 11126.5V in DVB-S Network'},
 '11225V': {'EIT: DVB Grabber': 'data completion timeout for 11225V in DVB-S Network'},
 '11265V': {'EIT: DVB Grabber': 'data completion timeout for 11265V in DVB-S Network'},
 '11307V': {'EIT: DVB Grabber': 'data completion timeout for 11307V in DVB-S Network'},
 '11343V': {'EIT: DVB Grabber': 'data completion timeout for 11343V in DVB-S Network'},
 '11344.5H': {'EIT: DVB Grabber': 'data completion timeout for 11344.5H in DVB-S Network'},
 '11425H': {'EIT: DVB Grabber': 'data completion timeout for 11425H in DVB-S Network',
            'UK: Freesat': 'data completion timeout for 11425H in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 11425H in DVB-S Network'},
 '11426.5V': {'EIT: DVB Grabber': 'data completion timeout for 11426.5V in DVB-S Network'},
 '11479V': {'EIT: DVB Grabber': 'data completion timeout for 11479V in DVB-S Network'},
 '11493.75H': {'EIT: DVB Grabber': 'data completion timeout for 11493.75H in DVB-S Network'},
 '11508.5V': {'EIT: DVB Grabber': 'data completion timeout for 11508.5V in DVB-S Network'},
 '11538V': {'EIT: DVB Grabber': 'data completion timeout for 11538V in DVB-S Network'},
 '11552.75H': {'EIT: DVB Grabber': 'data completion timeout for 11552.75H in DVB-S Network'},
 '11567.5V': {'EIT: DVB Grabber': 'data completion timeout for 11567.5V in DVB-S Network'},
 '11582.25H': {'EIT: DVB Grabber': 'data completion timeout for 11582.25H in DVB-S Network'},
 '11597V': {'EIT: DVB Grabber': 'data completion timeout for 11597V in DVB-S Network'},
 '11670.75H': {'EIT: DVB Grabber': 'data completion timeout for 11670.75H in DVB-S Network'},
 '11685.5V': {'EIT: DVB Grabber': 'data completion timeout for 11685.5V in DVB-S Network',
              'UK: Freesat (EIT)': 'data completion timeout for 11685.5V in DVB-S Network'},
 '11719.5H': {'EIT: DVB Grabber': 'data completion timeout for 11719.5H in DVB-S Network',
              'UK: Freesat': 'data completion timeout for 11719.5H in DVB-S Network',
              'UK: Freesat (EIT)': 'data completion timeout for 11719.5H in DVB-S Network'},
 '11836.5H': {'EIT: DVB Grabber': 'data completion timeout for 11836.5H in DVB-S Network'},
 '11914.5H': {'EIT: DVB Grabber': 'data completion timeout for 11914.5H in DVB-S Network'},
 '11973V': {'EIT: DVB Grabber': 'data completion timeout for 11973V in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 11973V in DVB-S Network'},
 '12070.5H': {'EIT: DVB Grabber': 'data completion timeout for 12070.5H in DVB-S Network'},
 '12129V': {'EIT: DVB Grabber': 'data completion timeout for 12129V in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 12129V in DVB-S Network'},
 '12363V': {'EIT: DVB Grabber': 'data completion timeout for 12363V in DVB-S Network',
            'UK: Freesat (EIT)': 'data completion timeout for 12363V in DVB-S Network'},
 '12382.5H': {'EIT: DVB Grabber': 'data completion timeout for 12382.5H in DVB-S Network'}}

