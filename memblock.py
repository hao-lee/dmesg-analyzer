import re
import numpy
import pylab
from unitify import *

class Region:
	def __init__(self, start_addr, end_addr):
		self.start_addr = start_addr
		self.end_addr = end_addr

class Memblock:
	def __init__(self, dmesg):
		self.dmesg = dmesg
		self.memory_regions = []
		self.reserved_regions = []

	def extract_memory_regions(self):
		regex = r"memblock_add:\s\[(0x[0-9a-f]+)-(0x[0-9a-f]+)\]"
		pattern = re.compile(regex)
		intervals = pattern.findall(self.dmesg)
		for interval in intervals:
			start_addr = int(interval[0], 16) # string to number
			end_addr = int(interval[1], 16)
			region = Region(to_mb(start_addr), to_mb(end_addr))
			self.memory_regions.append(region)

	def extract_reserved_regions(self):
		regex = r"memblock_reserve:\s\[(0x[0-9a-f]+)-(0x[0-9a-f]+)\]"
		pattern = re.compile(regex)
		intervals = pattern.findall(self.dmesg)
		for interval in intervals:
			start_addr = int(interval[0], 16) # string to number
			end_addr = int(interval[1], 16)
			region = Region(to_mb(start_addr), to_mb(end_addr))
			self.reserved_regions.append(region)

	def visuallization(self):
		self.extract_memory_regions()
		self.extract_reserved_regions()
		all = []
		for region in self.memory_regions:
			all.append(region.start_addr)
			all.append(region.end_addr)
		for region in self.reserved_regions:
			all.append(region.start_addr)
			all.append(region.end_addr)
		all = list(set(all))
		all.sort()
		for region in self.memory_regions:
			x1 = all.index(region.start_addr)
			x2 = all.index(region.end_addr)
			y1 = y2 = 2
			plot_memory, = pylab.plot([x1, x2], [y1, y2])
			# http://blog.csdn.net/sinat_36772813/article/details/77187578
			# start label
			pylab.annotate(str(region.start_addr), xy=(x1, y1),
			                xytext=(-15, 20), xycoords='data',
			                textcoords='offset points',
			                arrowprops=dict(arrowstyle='-'))
			# end label
			pylab.annotate(str(region.end_addr), xy=(x2, y2),
			                xytext=(-15, 10), xycoords='data',
			                textcoords='offset points',
			                arrowprops=dict(arrowstyle='-'))
		for region in self.reserved_regions:
			x1 = all.index(region.start_addr)
			x2 = all.index(region.end_addr)
			y1 = y2 = 1
			plot_reserved, = pylab.plot([x1, x2], [y1, y2])
			# start label
			pylab.annotate(str(region.start_addr), xy=(x1, y1),
			                xytext=(-15, -10), xycoords='data',
			                textcoords='offset points',
			                arrowprops=dict(arrowstyle='-'))
			# end label
			pylab.annotate(str(region.end_addr), xy=(x2, y2),
			                xytext=(-15, -20), xycoords='data',
			                textcoords='offset points',
			                arrowprops=dict(arrowstyle='-'))
		# x axis scale
		#pylab.xscale('log', basex=2)
		# y axis range
		pylab.yticks(range(4))
		# legend
		pylab.legend([plot_memory, plot_reserved], ["first line", "second line"])
		pylab.show()