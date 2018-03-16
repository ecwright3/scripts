import os
import csv
import sys

s = open('S:/wrighte/ServerList.txt', 'r')
servers = list(map(lambda x: x.strip("\n"), s.readlines()))

total = len(servers)
complete = 1
o = open('S:/wrighte/ServerList.csv','w+', newline='')

for server in servers:
    perComplete = "{0:.0f}%".format(complete / total * 100)
    response = list(map(lambda x: x.strip("\n"), os.popen("ping -n 1 -4 %s" %server).readlines()))
    response = list(filter(None,response))
    result = response[0].split(" ")[:3]
    if result[0] != 'Pinging':
        result = ['failed',server, None]
    else:
        result[0] = 'successful'
        result[2] = result[2][1:-1]
    wr = csv.writer(o, quoting=csv.QUOTE_ALL)
    wr.writerow(result)
    #print(result)
    complete += 1
    #print("%s Complete" %perComplete)
    sys.stdout.write("\r%s Complete" %perComplete)
    sys.stdout.flush()


print("done!!!")
   
