# Week 1.6, Session 1: Task 5

from datetime import datetime

from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """
    An exception type for errors involving QuakeDataset.
    """


class QuakeDataset:
    """
    An earthquake dataset obtained from a USGS data feed.
    """

    def __init__(self, feed):
        """
        Creates an empty dataset, linked to a specific data feed.
        """
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")

        self.feed = feed
        self.data = []

    def read_feed(self):
        """
        Refreshes this dataset with data from the linked feed.

        The new data replaces any existing data.
        """
        self.data = []

        for info in self.feed.reader():
            if not info.get("time") or not info.get("longitude"):
                continue

            try:
                quake = Quake(
                    when=datetime.fromisoformat(info["time"][:19]),
                    longitude=float(info["longitude"]),
                    latitude=float(info["latitude"]),
                    depth=float(info["depth"]),
                    magnitude=float(info["mag"] or 0.0),
                )
            except (TypeError, ValueError):
                continue

            self.data.append(quake)

    def __len__(self):
        """
        Returns the size of this dataset.
        """
        return len(self.data)

    def __str__(self):
        """
        Returns information on this dataset as a string.
        """
        return f"{len(self.data)} quakes, from {self.feed}"

    def mean_depth(self):
        """
        Returns the mean depth of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.depth for quake in self.data)
        return total / len(self.data)

    def mean_magnitude(self):
        """
        Returns the mean magnitude of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.magnitude for quake in self.data)
        return total / len(self.data)

    def shallowest_quake(self):
        """
        Returns details of the shallowest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        shallowest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth < shallowest.depth:
                shallowest = quake
        return shallowest

    def strongest_quake(self):
        """
        Returns details of the strongest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        strongest = self.data[0]
        for quake in self.data[1:]:
            if quake.magnitude > strongest.magnitude:
                strongest = quake
        return strongest
