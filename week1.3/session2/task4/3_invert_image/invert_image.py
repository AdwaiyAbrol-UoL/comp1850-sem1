# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except
try:
    with open('../images/sample.pgm', 'r') as f:
        data = f.readlines()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value
invert_pixel_value = [int(max_gray) - value for value in original_pixel_value]

# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"
try:
    with open('../images/inverted_sample.pgm', 'w') as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")
        f.write(" ".join(str(item) for item in invert_pixel_value))
except Exception as e:
    print(f"An error occurred while writing the file: {e}")
    exit()
 