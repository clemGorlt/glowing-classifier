#ls -1 *.pcap | tail -n50 | parallel --gnu 'tcpdump -s0 -A -n -r {1}' | python import.py
cd sample/pcap/
ls -1 . | head -n500 | parallel -j 10 --gnu "cat {1} | tshark -E separator=, -E header=yes -Tfields -e http.user_agent -r {1} | python ../../bin/import.py -f {1}"
