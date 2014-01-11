ls -1 *.pcap | tail -n50 | parallel --gnu 'tcpdump -s0 -A -n -r {1}' | python test.py
