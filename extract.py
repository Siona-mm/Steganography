from PIL import Image
import random
import sys


key = 2026
colourPlane = 1
significantBit = 7
stegoImagePath = "steg_lab/stego-image.bmp"

image = Image.open(stegoImagePath).convert("RGB")
width, height = image.size
pixels = image.load()

total_pixels = width * height
shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)

extractedBits = []
for i in shuffledIndices:
    x = i % width
    y = i // width
    val = pixels[x, y][colourPlane]

    bit = (val >> (7 - significantBit)) & 1
    extractedBits.append(str(bit))


len_bits = "".join(extractedBits[:14])
message_length = int(len_bits, 2)


decoded_chars = []
for i in range(message_length):
    start = 14 + (i * 7)
    char_bits = "".join(extractedBits[start : start + 7])
    decoded_chars.append(chr(int(char_bits, 2)))

print("-" * 30)
print("RECOVERED SECRET MESSAGE:")
print("".join(decoded_chars))
print("-" * 30)