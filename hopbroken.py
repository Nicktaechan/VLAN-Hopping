#Import scapy
from scapy.all import *

#craft packet with 802.1Q headers
packet =  Ether(dst="ff:ff:ff:ff:ff:ff")/\
          DOT1Q(vlan=1)/\
          DOT1Q(vlan=2)/\
          IP(src="IPv4 address", dst="IPv4 address")/\
          ICMP()
          
#show packet
packet.show()

#send packet
sendp(packet)