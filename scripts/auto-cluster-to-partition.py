import os
import shutil
from natsort import natsorted # https://pypi.python.org/pypi/natsort
import time

"""
This script copies every clustering files from on design
into the temp dir of phoney.
It then call phoney to partition the design and then
executes the csv-extracting scripts.
"""

tStart = time.time()

clusterDir = "/home/para/dev/def_parser/2018-01-15_15-31-14/"
partitionDir = "/home/para/dev/metis_unicorn/temp_design/"
phoneyScript = "/home/para/dev/metis_unicorn/script/phoney.py"

connectivityFile = "/home/para/dev/metis_unicorn/script/connectivity_partition.txt"
connectivityScript = "/home/para/dev/metis_unicorn/script/netcut_to_csv.py"

netCutFile = "/home/para/dev/metis_unicorn/script/cutLength_partition.txt"
netCutScript = "/home/para/dev/metis_unicorn/script/netcutlen_to_csv.py"

# Delete the previous analysis files
os.unlink(connectivityFile)
os.unlink(netCutFile)

for subdir in natsorted(os.listdir(clusterDir)):
    clusterSubDir = os.path.join(clusterDir, subdir)
    design = clusterSubDir.split('/')[-1].split('_')[0]
    clustering = clusterSubDir.split('/')[-1].split('_')[1]
    print "##############################################"
    print "Processing " + clusterSubDir

    # Delete everything in the target directory
    for file in os.listdir(partitionDir):
        os.unlink(os.path.join(partitionDir, file))

    # Copy everything from the source to the target
    for file in os.listdir(clusterSubDir):
        shutil.copy(os.path.join(clusterSubDir, file), partitionDir)

    print partitionDir + " content replaced. Let's do this."

    # Partition
    # TODO This is ugly as shit. I should import the script.
    # Phoney is stupid, so I need to change the working directory.
    os.chdir("/".join(phoneyScript.split('/')[:-1]))
    os.system("python " + phoneyScript)

    print "###############################################"

# Analysis
# Backup the raw file
newConnectivityFile = connectivityFile.split('.')[0] + \
                    "_" + design + "_" + clustering + \
                    time.strftime('_%Y-%m-%d_%H-%M-%S') + \
                    connectivityFile.split('.')[-1]
shutil.copy(connectivityFile, newConnectivityFile)
os.system("python " + connectivityScript)

newNetCutFile = netCutFile.split('.')[0] + \
                "_" + design + "_" + clustering + \
                time.strftime('_%Y-%m-%d_%H-%M-%S') + \
                netCutFile.split('.')[-1]
shutil.copy(netCutFile, newNetCutFile)
os.system("python " + netCutScript)

print "Total duration: " + str(time.time() - tStart)