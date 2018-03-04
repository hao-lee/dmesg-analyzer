from memblock import *

class Analyzer():
	def __init__(self, filename):
		with open(filename) as fd:
			self.dmesg = fd.read()

	def analyze_memblock(self):
		memblock = Memblock(self.dmesg)
		memblock.visuallization()

if __name__ == "__main__":
	analyzer = Analyzer("E:\桌面迁移\Kernel\log")
	analyzer.analyze_memblock()