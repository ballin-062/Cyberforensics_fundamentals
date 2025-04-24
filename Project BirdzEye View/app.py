from flask import Flask, request, render_template, redirect, url_for
from scapy.all import rdpcap, IP, TCP, UDP
import os
import networkx as nx
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def get_protocol_name(proto_number):
    proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    return proto_map.get(proto_number, f"Unknown ({proto_number})")

def generate_network_graph(packets, output_path='static/graph.png'):
    G = nx.DiGraph()
    traffic_counts = {}

    for pkt in packets:
        if IP in pkt:
            src = pkt[IP].src
            dst = pkt[IP].dst
            pair = (src, dst)
            traffic_counts[pair] = traffic_counts.get(pair, 0) + 1

    for (src, dst), count in traffic_counts.items():
        G.add_edge(src, dst, weight=count)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)

    if G.edges:
        weights = [G[u][v]['weight'] for u, v in G.edges()]
        nx.draw_networkx_nodes(G, pos, node_color='#990000', node_size=500)
        nx.draw_networkx_labels(G, pos, font_color='white')
        nx.draw_networkx_edges(
            G, pos,
            edge_color='gray',
            width=[(w / max(weights)) * 5 for w in weights]
        )

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        pcap_file = request.files['file']
        if pcap_file and pcap_file.filename.endswith('.pcapng'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], pcap_file.filename)
            pcap_file.save(filepath)
            return redirect(url_for('show_packets', filename=pcap_file.filename))
        else:
            return "Invalid file type. Please upload a .pcapng file."
    return render_template('upload.html')

@app.route('/packets/<filename>')
def show_packets(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    packets = rdpcap(filepath)

    packet_list = []
    for pkt in packets:
        if IP in pkt:
            packet_info = {
                'time': pkt.time,
                'src_ip': pkt[IP].src,
                'dst_ip': pkt[IP].dst,
                'proto': get_protocol_name(pkt[IP].proto),
                'length': len(pkt),
                'src_port': '',
                'dst_port': ''
            }

            if TCP in pkt:
                packet_info['src_port'] = pkt[TCP].sport
                packet_info['dst_port'] = pkt[TCP].dport
            elif UDP in pkt:
                packet_info['src_port'] = pkt[UDP].sport
                packet_info['dst_port'] = pkt[UDP].dport

            packet_list.append(packet_info)

    sort_key = request.args.get('sort')
    if sort_key and sort_key in packet_list[0]:
        packet_list.sort(key=lambda x: x[sort_key])

    generate_network_graph(packets)
    return render_template('packets.html', packets=packet_list, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)