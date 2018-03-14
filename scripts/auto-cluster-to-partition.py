import os
import shutil
from natsort import natsorted # https://pypi.python.org/pypi/natsort
import time
import sys, getopt

"""
This script calls phoney on every clusterings of a
given design. Then it executes the csv-extracting scripts.

Usage: script -d <Parent directory of clusters> -p <path to phoney> -c <path to connectivity script> -n <path to netcut script>
"""

tStart = time.time()

clusterDir = ""
phoneyScript = ""
connectivityScript = ""
netCutScript = ""
try:
    opts, args = getopt.getopt(sys.argv[1:],"d:p:c:n:")
except getopt.GetoptError:
    print "YO FAIL"
else:
    for opt, arg in opts:
        if opt == "-d":
            clusterDir = arg
        elif opt == "-p":
            phoneyScript = arg
        elif opt == "-c":
            connectivityScript = arg
        elif opt == "-n":
            netCutScript = arg

    if clusterDir == "":
        clusterDir = "/home/para/dev/def_parser/2018-01-25_16-16-50/"
    if phoneyScript == "":
        phoneyScript = "/home/para/dev/metis_unicorn/script/phoney.py"
    if connectivityScript == "":
        connectivityScript = "/home/para/dev/metis_unicorn/script/netcut_to_csv.py"
    if netCutScript == "":
        netCutScript = "/home/para/dev/metis_unicorn/script/netcutlen_to_csv.py"

connectivityFile = "connectivity_partition.txt"
netCutFile = "cutLength_partition.txt"

for subdir in natsorted(os.listdir(clusterDir)):
    clusterSubDir = os.path.join(clusterDir, subdir)
    if os.path.isdir(clusterSubDir):
        design = clusterSubDir.split('/')[-1].split('_')[0]
        clustering = clusterSubDir.split('/')[-1].split('_')[1]
        print "##############################################"
        print "Processing " + clusterSubDir

        # Partition
        # TODO This is ugly as shit. I should import the script.
        # Phoney is stupid, so I need to change the working directory.
        os.chdir("/".join(phoneyScript.split('/')[:-1]))
        os.system("python " + phoneyScript + " -d " + clusterSubDir)
        
        for subsubdir in natsorted(os.listdir(clusterSubDir)):
            partitionDir = os.path.join(clusterSubDir, subsubdir)
            if os.path.isdir(partitionDir):
                os.system("python " + connectivityScript + " -f " + os.path.join(partitionDir, connectivityFile))
                os.system("python " + netCutScript + " -f " + os.path.join(partitionDir, netCutFile))

        print "###############################################"

print "Total duration: " + str(time.time() - tStart)