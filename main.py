# Libraries
import numpy as np
from PIL import Image # known as Pillow
import pyxel

''' PARAMETERS ''' 
# Pyxel palette (edit if you are using a custom one)
PYXEL_COLORS = np.array([
    [0, 0, 0], [43, 51, 95], [126, 32, 114], [25, 149, 156],
    [139, 72, 82], [57, 92, 152], [169, 193, 255], [238, 238, 238],
    [212, 24, 108], [211, 132, 65], [233, 195, 91], [112, 198, 169],
    [118, 150, 222], [163, 163, 163], [255, 151, 152], [237, 199, 176]
])

# Path to the input image you want to transform
input_image_path = "input-example.png"

# Prefix for the output Pyxel resource files
output_pyxres_prefix = "output-example"

def closest_color(rgb_color):
    rgb_color = np.array(rgb_color) / 255.0
    palette = PYXEL_COLORS / 255.0
    color_diffs = np.linalg.norm(palette - rgb_color, axis=1)
    return np.argmin(color_diffs)

def image_to_pyxres(input_image_path, output_pyxres_prefix):
    image = Image.open(input_image_path).convert('RGB')
    width, height = image.size

    pyxel.init(width, height, title="image2pyxres", display_scale=1)

    num_tilesets_x = (width + 255) // 256
    num_tilesets_y = (height + 255) // 256

    for ty in range(num_tilesets_y):
        for tx in range(num_tilesets_x):
            pyxel.image(0).cls(0)

            for y in range(256):
                for x in range(256):
                    src_x = tx * 256 + x
                    src_y = ty * 256 + y
                    if src_x < width and src_y < height:
                        color_index = closest_color(image.getpixel((src_x, src_y)))
                        pyxel.image(0).pset(x, y, color_index)

            output_pyxres_path = f"{output_pyxres_prefix}_{ty}_{tx}.pyxres"
            pyxel.save(output_pyxres_path)
            print(f".pyxres file saved as: {output_pyxres_path}")

    return num_tilesets_x, num_tilesets_y, width, height, output_pyxres_prefix

def load_and_draw_image(num_tilesets_x, num_tilesets_y, width, height, prefix):
    def draw():
        pyxel.cls(0)
        for ty in range(num_tilesets_y):
            for tx in range(num_tilesets_x):
                pyxel.load(f"{prefix}_{ty}_{tx}.pyxres")
                pyxel.blt(tx * 256, ty * 256, 0, 0, 0, 256, 256)

    pyxel.run(lambda: None, draw)

num_tilesets_x, num_tilesets_y, width, height, prefix = image_to_pyxres(input_image_path, output_pyxres_prefix)

load_and_draw_image(num_tilesets_x, num_tilesets_y, width, height, prefix)
