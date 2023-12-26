import argparse
import os
import sys

job_name = sys.argv[1]

if job_name == 'all':
    os.system("ps -ef | grep python | grep FedScale > fedscale_running_temp")
else:
    os.system("ps -ef | grep python | grep 'job_name {}' > fedscale_running_temp".format(job_name))

for l in open("fedscale_running_temp").readlines():
    print(l.strip())
    print("kill -9 "+str(l.split()[1]) + " 1>/dev/null 2>&1" + "\n") 
    
[os.system("kill -9 "+str(l.split()[1]) + " 1>/dev/null 2>&1") for l in open("fedscale_running_temp").readlines()]
os.system("lsof -t -i:42069| xargs -I {} kill -9 {}")
os.system("rm fedscale_running_temp")
