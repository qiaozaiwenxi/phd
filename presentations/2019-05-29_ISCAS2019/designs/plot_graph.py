from __future__ import division
import matplotlib.pyplot as plt

fileList = ["boomcore_WLnets.out", "ldpc4x4-serial_WLnets.out", "ccx_WLnets.out", "ldpc4x4_WLnets.out", "spc_WLnets.out", "filpr_WLnets.out", "LDPC_WLnets.out"]
hplList = [203.968, 527.85, 1192.59, 650.176, 1972.908, 242.596, 115.054]

lengths = list()
cumulNums = list()
cumulLens = list()

for j in range(len(fileList)):
	with open(fileList[j], 'r') as f:
		fileLines = f.readlines()

	length = list()
	cumulLen = list()
	cumulNum = list()

	for i in range(1, len(fileLines)):
		length.append(float(fileLines[i].split(' ')[2])/hplList[j])

	totLen = sum(length)
	totNum = len(length)

	length.sort()
	n = 0
	m = 0

	for l in length:
		n += 1
		m += l
		cumulLen.append( 100 * (m + l)/totLen )
		cumulNum.append(100 * n/totNum)
	lengths.append(length)
	cumulLens.append(cumulLen)
	cumulNums.append(cumulNum)

for i in range(len(fileList)):
	plt.plot(lengths[i], cumulNums[i])
	plt.plot(lengths[i], cumulLens[i])
	# plt.axis([0, self.width, 0, self.height])
	# plt.yscale("log")
	plt.xscale("log")
	plt.title(fileList[i])
	plt.xlabel("Net length, normalized on HPL")
	plt.legend(('Cumulated number of wires', 'Cumulated wire-length'))
	plt.figure()
plt.show()