from PIL import Image
import random
import sys
import os


key = 2026
colourPlane = 1     
significantBit = 7    
coverImagePath = 'steg_lab/img/flowers.bmp'
secretFilePath = 'steg_lab/secret.txt'
outputImagePath = "steg_lab/stego-image.bmp"


if not os.path.exists(coverImagePath):
    print(f"Error: {coverImagePath} not found.")
    sys.exit()

image = Image.open(coverImagePath).convert("RGB")
width, height = image.size
pixels = image.load()

with open(secretFilePath, "r", encoding="utf-8") as f:
    secret_text = f.read()


total_pixels = width * height
sbits = ''.join(format(ord(char), '07b') for char in secret_text)
lbits = format(len(secret_text), '014b')
bits_to_hide = lbits + sbits

if len(bits_to_hide) > total_pixels:
    print("Error: Message too large for image capacity.")
    sys.exit()


shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)


def modify_pixel(pixel, plane, bit, modifier):
    m = modifier * (2 ** (7 - bit))
    p_list = list(pixel)
    p_list[plane] += m
    return tuple(p_list)


for i in range(len(bits_to_hide)):
    idx = shuffledIndices[i]
    x = idx % width
    y = idx // width

    current_val = pixels[x, y][colourPlane]

    bit_val = (current_val >> (7 - significantBit)) & 1
    target_bit = int(bits_to_hide[i])

    if bit_val == 0 and target_bit == 1:
        pixels[x, y] = modify_pixel(pixels[x, y], colourPlane, significantBit, 1)
    elif bit_val == 1 and target_bit == 0:
        pixels[x, y] = modify_pixel(pixels[x, y], colourPlane, significantBit, -1)


image.save(outputImagePath)
print(f"Success! Stego-image saved to {outputImagePath}")