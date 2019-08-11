<p align="center"><img src="assets/logo.png" width=100/></p>
<h1 align="center">net-csi</h1>
<p>an open-source neural net utility for investigating potential sources of past network attacks</p>

<hr>

NOTE: This project is sort of broken at the moment, since I'm still learning TensorFlow and it's therefore in a very early development stage. Once it's working, I'll update the README to say so, and add installation/usage instructions.

Progress
--------
- [x] A traffic capture (Wireshark PCAP) is analyzed with `suricata` and a base ruleset is generated.
- [x] The original capture data and `suricata`'s resulting `eve.json` log are loaded into net-csi as a dataset.
- [ ] The user will have the option to either scan everything based on the log, or specify a port, protocol or alert type they want to filter via command-line options. I'll probably need `argparse` for this.
- [ ] `net-csi` will then use some variant of neural net to identify patterns in packet payloads that correspond to malicious activity.(The current model is feed-forward for testing purposes, but I may switch to something else later)
- [ ] Once it's processed all the train data, `net-csi` will then read any arbitrary capture file it's called on as well as a number of optional command-line arguments, labeling any pcap entries it deems low-security and/or malicious and writing them to console output, a log file, or both.