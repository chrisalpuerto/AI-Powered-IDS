

from scapy.all import sniff, IP 

sus_ips = {
    "1.2.3.4",
    "5.6.7.8",
    "192.168.1.50"
}

def is_suspicious_ip(ip):
    return ip in sus_ips


def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto


sniff(prn=process_packet, store=0)