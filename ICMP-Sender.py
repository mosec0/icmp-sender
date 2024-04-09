from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1
from datetime  import datetime

print("#"*28)
print(" [+] Coded By:~# Mohamed Ali")
print(" [+] Sending Started at:" + str(datetime.now()))
print("#"*28)

while True:
    try:
        src_ip       = input(" Enter Your Ip > ")
        dst_ip       = input(" Destnation Name > ")

        ip_header    = IP(src=src_ip,dst=dst_ip)
        icmp_opt     = ICMP(id=100)
        full_packets = ip_header / icmp_opt

        packet_send  = sr1(full_packets)
        if packet_send:
            print( packet_send.show() )
        ua = input(" Do You Want Continue ?? ")
        if ua.lower()=="y" or ua.lower()=="yes":
            continue
        else:
            print(" Good Bey :)")
            break

    except Exception:
        print(" [-] Please Enter Correct Data")
        
