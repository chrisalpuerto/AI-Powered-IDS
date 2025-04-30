# packet sniffer program

from scapy.all import sniff, IP, TCP, UDP_SERVICES
from ai_engine.detector import classify_packet