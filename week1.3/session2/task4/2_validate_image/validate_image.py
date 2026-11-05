# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except
try:
    with open('../images/sample.pgm', 'r') as f:
        data = f.readlines()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Read the file content 
for line in data:
    print(line.strip())

# Store the width, the height, and the maximum gray value
width, height = data[1].strip().split()
print(f"Dimensions: {width} x {height} pixels")
max_gray = data[2].strip()
print(f"Max Gray Value: {max_gray}")

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive
pixel_values = [int(value) for value in data [3:3+int(width)*int(height)]]
print(f"Pixel values : {pixel_values}")

# Check if the widths and heights are the same as specified
width_check = len(pixel_values) == int(width) * int(height)
height_check = len(pixel_values) == int(width) * int(height)
print(f"Width check: {width_check}")
print(f"Height check: {height_check}")

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

if width_check and height_check and all(0 <= value <= int(max_gray) for value in pixel_values):
    print("Valid image")
elif not width_check:
    print("Invalid width")
elif not height_check:
    print("Invalid height")
elif not all(0 <= value <= int(max_gray) for value in pixel_values):
    print("Invalid pixel values")
else:
    print("Invalid image")