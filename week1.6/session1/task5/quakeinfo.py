# Week 1.6, Session 1: Task 5

import sys

from dataset import QuakeDataset
from feed import QuakeFeed


def main():
    if len(sys.argv) >= 3:
        level, period = sys.argv[1], sys.argv[2]
    else:
        level = input("Enter a quake level (all, 1.0, 2.5, 4.5, significant): ")
        period = input("Enter a time period (hour, day, week, month): ")

    feed = QuakeFeed(level, period)
    dataset = QuakeDataset(feed)
    dataset.read_feed()

    if len(dataset) == 0:
        print(f"0 quakes, from {feed}")
        return

    strongest = dataset.strongest_quake()

    print(f"{len(dataset)} quakes, from {feed}")
    print(f"Mean depth = {dataset.mean_depth():.2f} km")
    print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")
    print()
    print(f"Strongest quake occurred at {strongest.when.strftime('%H:%M:%S')} on {strongest.when.strftime('%Y-%m-%d')}")
    print(f"at {strongest.longitude}° longitude, {strongest.latitude}° latitude")
    print(f"The depth was {strongest.depth:.1f} km")
    print(f"The magnitude was {strongest.magnitude:.1f}")


if __name__ == "__main__":
    main()
