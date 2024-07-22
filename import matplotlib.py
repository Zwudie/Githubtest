import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Set the number of rows and columns
rows, cols = 3, 10

# Create a grid of squares
for row in range(rows):
    for col in range(cols):
        square = plt.Rectangle((col, -row), 1, 1, fill=None, edgecolor='black')
        ax.add_patch(square)

# Set the limits and aspect ratio
ax.set_xlim(0, cols)
ax.set_ylim(-rows, 0)
ax.set_aspect('equal')

# Hide the axes
ax.axis('off')

# Show the plot
plt.show()
