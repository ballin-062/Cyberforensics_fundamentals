from flask import Flask, request, render_template, redirect, url_for
from scapy.all import rdpcap, IP
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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
                'src': pkt[IP].src,
                'dst': pkt[IP].dst,
                'proto': pkt[IP].proto
            }
            packet_list.append(packet_info)

    return render_template('packets.html', packets=packet_list, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
