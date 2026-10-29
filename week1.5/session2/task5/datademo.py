# Week 1.5, Session 2: Task 5

from data import Dataset

filename = input("Enter the name of the data file: ")
dataset = Dataset(filename)

print("Dataset size:", len(dataset))
print("Mean:", dataset.mean())
print("Median:", dataset.median())

print("Values:")
for value in dataset:
    print(value)
