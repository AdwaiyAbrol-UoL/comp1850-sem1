# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
try:
    with open('../images/sample.pgm', 'r') as f:
        data = f.readlines()
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Read the file content
for line in data:
    print(line.strip())

# print image dimension (i.e., Dimensions: width x height pixels)
width, height = data[1].strip().split()
print(f"Dimensions: {width} x {height} pixels")

# print max gray value (i.e., Max Gray Value: max_gray_value)
max_gray = data[2].strip()
print(f"Max Gray Value: {max_gray}")