# Modified by DrRadical15.
# Created by SethBling.
# http://youtube.com/SethBling

import random

displayName = "Mapify"

inputs = (
	("Block", "blocktype"),
)

def perform(level, box, options):
	block = options["Block"].ID
	data = options["Block"].blockData

	for x in xrange(box.minx, box.maxx):
		for z in xrange(box.minz, box.maxz):
			exists = False
			for y in xrange(box.miny, box.maxy):
				if (level.blockAt(x, y, z) != 0):
					exists = True
			if exists:
				level.setBlockAt(x, 255, z, block)
				level.setBlockDataAt(x, 255, z, data)

	level.markDirtyBox(box)
