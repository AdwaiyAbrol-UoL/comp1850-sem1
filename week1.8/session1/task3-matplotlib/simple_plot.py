
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(10) ] # create some data
y = [ k*k for k in x ]

plt.plot(x,y) # create a plot
plt.xlabel('x')
plt.ylabel('y=x^2') # annotate
plt.show() # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions

# Test 1: Line graph of y = x^2
# Creates x values from 1 to 10 and calculates the square of each value.
# Plots the points and connects them with a line. The annotation points to (5, 25).

# x = range(1,11)  # create a range for the data
# y = [ k*k for k in x ]      # create a simple function y=x^2

# plt.plot(x,y, marker = "o")  # create a 2d plot

# plt.xlabel("x")
#plt.ylabel("y= x squared")  # annotate
# plt.title("Square numbers")
# plt.annotate("Here: (5, 25)", xy=(5, 25), xytext=(6, 15), arrowprops={"arrowstyle": "->"})
# plt.show()  # display



# Test 2: Pie chart of example daily hours
# Shows how 24 example hours are divided between four activities.
# Labels identify each slice, and autopct displays each activity's percentage.

# labels = ["Study", "Sleep", "Social", "Other"]
# hours = [6, 8, 3, 7]
# plt.pie(hours, labels=labels, autopct="%1.1f%%", startangle=90)
# plt.title("Example daily hours")
# plt.axis("equal")
# plt.show()
