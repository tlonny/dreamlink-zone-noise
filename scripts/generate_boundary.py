from os.path import join, dirname
from random import randint

from dreamlinktools.zone_chunks import ZoneChunks
from dreamlinktools.utils.vec3 import Vec3

root_dir = dirname(dirname(__file__))
chunks = ZoneChunks(root_dir)
chunks.load()

dims = chunks.block_space_dimensions
for ix in range(dims.volume()):
    block_pos = Vec3.unpack(ix, chunks.block_space_dimensions)
    if block_pos.x == 1 or block_pos.x == dims.x - 2:
        chunks[block_pos] = randint(4, 19)
    if block_pos.y == 1 or block_pos.y == dims.y - 2:
        chunks[block_pos] = randint(4, 19)
    if block_pos.z == 1 or block_pos.z == dims.z - 2:
        chunks[block_pos] = randint(4, 19)

chunks.save()
