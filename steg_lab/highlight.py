from PIL import Image
import random

key = 2026
coverImagePath = 'steg_lab/img/flowers.bmp'
outputHighlight = 'steg_lab/highlighted-image.bmp'

image = Image.open(coverImagePath).convert("RGB")
width, height = image.size
pixels = image.load()

total_bits_needed = 14 + (1488 * 7)

shuffledIndices = list(range(width * height))
random.seed(key)
random.shuffle(shuffledIndices)

for i in range(total_bits_needed):
    idx = shuffledIndices[i]
    x = idx % width
    y = idx // width
    pixels[x, y] = (255, 0, 0) 

image.save(outputHighlight)