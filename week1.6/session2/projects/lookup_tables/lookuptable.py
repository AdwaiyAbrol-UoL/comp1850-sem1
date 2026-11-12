# Week 1.6, Session 2

"""Apply a pixel look-up table to a greyscale image."""

import math
import sys
from pathlib import Path

from image import Image


class LookupTable:
    """
    A standard 256-entry greyscale look-up table.
    """

    def __init__(self, values=None):
        if values is None:
            values = list(range(256))
        if len(values) != 256:
            raise ValueError("look-up table must contain 256 values")
        self.values = values

    def display(self):
        """
        Prints a concise description of the mapping for the look-up table.
        """
        for i in range(0, 256, 16):
            chunk = self.values[i:i + 16]
            print(f"{i:3}: {chunk}")

    def apply(self, image):
        """
        Returns a new image whose pixels are transformed by this look-up table.
        """
        transformed = image.copy()
        transformed.pixels = [self.values[p] for p in image.pixels]
        return transformed

    def apply_in_place(self, image):
        """
        Modifies the given image using this look-up table.
        """
        for i, pixel in enumerate(image.pixels):
            image.pixels[i] = self.values[pixel]
        return image


def invert_table():
    """
    Creates a look-up table that inverts image brightness.
    """
    return LookupTable([255 - value for value in range(256)])


def contrast_table(scale=1.0):
    """
    Creates a look-up table that boosts dark values while preserving the full range.
    """
    table = []
    for value in range(256):
        mapped = math.sqrt(value / 255.0) * 255.0 * scale
        table.append(int(max(0, min(255, round(mapped)))))
    return LookupTable(table)


def main():
    if len(sys.argv) != 3:
        print("Usage: python look-up table.py <input.pgm> <output.pgm>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    image = Image.read(str(input_file))
    table = invert_table()
    output = table.apply(image)
    output.write_pgm(str(output_file))

    print(f"Applied lookup table to {input_file.name} and wrote {output_file.name}")


if __name__ == "__main__":
    main()
