from scapy.all import rdpcap, IP

packets = rdpcap("pcap-smear\\test\\bonus_project.pcapng")

#print(packets[0:100])

packets.summary
print("*"*80)
packets.show

print("*"*80)
packets.plot