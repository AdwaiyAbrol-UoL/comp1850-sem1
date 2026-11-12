# Week 1.6, Session 2

"""
Simple benchmark for the Image class using the coins.pgm sample image.
"""

import time
from pathlib import Path

from image import Image


IMAGE_PATH = Path(__file__).resolve().parents[2] / "images" / "coins.pgm"


def benchmark(label, func, repeat=5):
    """
    Runs a timing benchmark for a function and prints the elapsed time.
    """
    timings = []
    for _ in range(repeat):
        start = time.perf_counter()
        func()
        elapsed = time.perf_counter() - start
        timings.append(elapsed)

    average = sum(timings) / len(timings)
    print(f"{label}: {average:.6f} seconds (average over {repeat} runs)")


def load_image():
    return Image.read(str(IMAGE_PATH))


def invert_image():
    image = load_image()
    for i in range(len(image.pixels)):
        image.pixels[i] = 255 - image.pixels[i]
    return image


def copy_image():
    image = load_image()
    return image.copy()


def sum_pixels():
    image = load_image()
    return sum(image.pixels)


def main():
    if not IMAGE_PATH.exists():
        raise FileNotFoundError(f"Could not find image file: {IMAGE_PATH}")

    print(f"Benchmarking {IMAGE_PATH.name}")
    print(f"Image dimensions: {load_image().width} x {load_image().height}")
    print()

    benchmark("Load image", load_image)
    benchmark("Invert all pixels", invert_image)
    benchmark("Copy image", copy_image)
    benchmark("Sum pixel values", sum_pixels)


if __name__ == "__main__":
    main()
