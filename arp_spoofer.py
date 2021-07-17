#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.2.15", hwdst="00:00:00:00:00:01", psrc="10.0.2.2")