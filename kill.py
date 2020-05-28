import subprocess
import sys
import os
import time

target = sys.argv[1]

cmd = "ps aux | grep %s | awk '{print $2}' | xargs" % target
pids = subprocess.check_output(cmd, shell=True)
# pids = subprocess.check_output("ps aux | grep ffmpeg | awk '{print $2}' | xargs", shell=True)
pids = pids.decode("utf-8").strip()
# pids = pids.split(" ")
print(pids)
os.system("sudo kill -9 %s" % pids)
#for p in pids:
#    try:
#        print(p)
#        os.system("sudo kill -9 %s" % p)
#        time.sleep(0.5)
#    except Exception as e:
#        print("Error")
#        print(e)
#        continue
