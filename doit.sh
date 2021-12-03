#bgpdump -m /mnt/ris/rrc03/2019.04/bview.20190407.0000.gz | ./peer-similarity-as-links.py 

YYYY=2021
MM=12
DD=01

#https://stat.ripe.net/data/ris-peers/data.json?query_time=$YYYY-$MM-$DD > peers.json
#rm ris-fullfeeds.csv
#wget https://sg-pub.ripe.net/stats/ris-fullfeeds.csv
for i in /mnt/ris/rrc*/$YYYY.$MM/bview.$YYYY$MM$DD.0000.gz
do
    bgpdump -m $i
done | ./extract-as-links.py as-links.rrcALL.$YYYY-$MM-$DD.pcl ## extract as a python pcl file
./calculate-peer-similarity.py as-links.rrcALL.$YYYY-$MM-$DD.pcl | gzip -9 > as-links-sim.rrcALL.$YYYY-$MM-$DD.txt

#done | ./research-peer-similarity-as-links.py  | tee as-links-sim.rrcALL.$YYYY-$MM-$DD.txt
#gzip -9 as-links-sim.rrcALL.$YYYY-$MM-$DD.txt
### done | ./research-peer-similarity-as-links.py  | tee rrcALL.test.txt
