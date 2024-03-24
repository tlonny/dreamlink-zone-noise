from os.path import join, dirname
from json import dumps
from random import random

root_dir = dirname(dirname(__file__))
for i in range(16):
    name = f"noise.{i}"
    with open(join(root_dir, "texture/samples", f"{name}.json"), "w") as f:
        f.write(dumps({
            "lookup.position": [144, 32 + i],
            "lookup.dimensions": [1, 1],
            "animation.stride": [1, 0],
            "animation.frames.total": 16,
            "animation.frames.row": 16,
            "animation.frames.start": 0,
            "animation.speed": random() * 0.8 + 0.1
        }, indent = 4))
    
    with open(join(root_dir, "blocks", f"{name}.json"), "w") as f:
        f.write(dumps({
            "meta.id": i + 4,
            "texture.sample.front": name,
            "texture.sample.back": name,
            "texture.sample.left": name,
            "texture.sample.right": name,
            "texture.sample.top": name,
            "texture.sample.bottom": name,
        }, indent = 4))
