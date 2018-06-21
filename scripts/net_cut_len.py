"""
Usage:
    net_cut_len.py  [-d <cluster dir>] [--netwl <WLnets.out>]
                    [--netcut <connectivity_partition.txt>]
    net_cut_len.py (--help|-h)

Options:
    -d <cluster dir>        Clustering directory. e.g. "ldpc_hierarchical-geometric_2"
                            (full path)
    --netwl <WLnets.out>    File with the length of all nets
    --netcut <connectivity_partition.txt>
                            File with all the nets cut by the partition

    -h --help               Print this help
"""

import os
from docopt import docopt

if __name__ == "__main__":

    clusterDir = ""
    netwlFile = "WLnets.out"
    netcutFile = "connectivity_partition.txt"
    netcutwlFile = "netCutWL.csv"

    args = docopt(__doc__)
    if args["-d"]:
        clusterDir = args["-d"]
    if args["--netwl"]:
        netwlFile = args["--netwl"]
    if args["--netcut"]:
        netcutFile = args["--netcut"]

    partitionDirs = []

    for subdir in os.listdir(clusterDir):
        if "partitions" in subdir:
            partitionDirs.append(os.path.join(clusterDir, subdir))
            nets = dict()
            with open(os.path.join(os.path.join(clusterDir, subdir), netcutFile), 'r') as f:
                for net in f.readline().split(',')[3:]:
                    nets[net] = 0
            with open(os.path.join(clusterDir, netwlFile), 'r') as f:
                for line in f.readlines():
                    line = line.split()
                    if line[0] in nets:
                        nets[line[0]] = float(line[2])
            netStr = ""
            for k in nets:
                netStr += str(k) + ", " + str(nets[k]) + "\n"
            with open(os.path.join(os.path.join(clusterDir, subdir), netcutwlFile), 'w') as f:
                f.write(netStr)

