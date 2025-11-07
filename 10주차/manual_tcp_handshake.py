from scapy.all import IP, TCP, sr1, send, conf
conf.use_pcap = True

dst = "127.0.0.1"
dport = 50007

# 1) SYN 전송 (client seq = 1000)
syn = IP(dst=dst)/TCP(dport=dport, flags="S", seq=1000)
print("[*] Sending SYN")
synack = sr1(syn, timeout=2)  # 서버로부터 단일 응답 기다림
if not synack:
    print("[!] No response. Is a server listening on", dport, "?")
    exit(1)
print("[*] Received:", synack.summary())
# 2) SYN-ACK 확인 후 ACK 전송 (ack = server.seq + 1)
if synack.haslayer(TCP) and (synack[TCP].flags & 0x12):  # 0x02(SYN) | 0x10(ACK)
    ack = IP(dst=dst)/TCP(dport=dport, flags="A",
                           seq=1001, ack=synack[TCP].seq + 1)
    send(ack)
    print("[*] Sent ACK — logical 3-way complete")
else:
    print("[!] Response not SYN-ACK")