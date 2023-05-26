#Import scapy
from scapy.all import *

#craft packet with 802.1Q headers
packet =  Ether(dst="ff:ff:ff:ff:ff:ff")/\
          DOT1Q(vlan=1)/\
          DOT1Q(vlan=2)/\
          DOT1Q(vlan=2)/\
          IP(src="source_IPv4_address", dst="destination_IPv4_address")/ \
          ICMP()

#show packet
packet.show()

#send packet
sendp(packet)