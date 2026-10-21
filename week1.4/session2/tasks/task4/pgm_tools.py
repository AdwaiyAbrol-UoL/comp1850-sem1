
# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename,"r") as f:    # read in the file
        data = f.readlines()
        
    # Split each line into separate pieces of text.
    cleaned_data = []
    for line in data[1:]:
        cleaned_line = line.strip().split()
        cleaned_data.append(cleaned_line)
          
    width = int(cleaned_data[0][0])
    height = int(cleaned_data[0][1])
    max_gray = int(cleaned_data[1][0])

    pixels = []
    for row_number in range(height):
        pixel_row = []
        for pixel_number in range(width):
            pixel = int(cleaned_data[2 + row_number][pixel_number])
            pixel_row.append(pixel)
        pixels.append(pixel_row)
    
    return width,height,max_gray,pixels   # tuple of PGM data
    
def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    with open(filename, "w") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")

        for row in pixels:
            for pixel in row:
                f.write(str(pixel) + " ")
            f.write("\n")

def invertPGM( image ):
    '''
    Invert an image by subtracting each pixel from the maximum gray value.
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    inverted = []
    for row in pixels:
        inverted_row = []
        for pixel in row:
            inverted_pixel = max_gray - pixel
            inverted_row.append(inverted_pixel)
        inverted.append(inverted_row)
    
    return width,height,max_gray,inverted

# code to test the PGM functions

image = readPGM("images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"{image[3]}")

# write further code to test your own functions
