# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data = []

        with open(filename, "r") as file:
            for line in file:
                value = line.strip()
                if value:
                    self.data.append(float(value))

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        if not self.data:
            raise ValueError("Cannot calculate the mean of an empty dataset.")
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        if not self.data:
            raise ValueError("Cannot calculate the median of an empty dataset.")

        sorted_data = sorted(self.data)
        middle = len(sorted_data) // 2

        if len(sorted_data) % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        return sorted_data[middle]
