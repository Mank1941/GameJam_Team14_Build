import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
grid_size = 20
time_steps = 200  # Adjust the total number of time steps
wind_speed = 0.1
warm_probability = 0.25
change_direction_frame = 30  # Frame interval at which to change the wind direction
hot_pocket = 0.25
hot_pocket_temp = -20
hot_pockets_count = int((grid_size * grid_size) * hot_pocket)  # Number of hot pockets to add

# Initialize temperature grid with a probability of a cell being warm or cold
temperature_grid = np.random.choice([np.random.uniform(low=-80, high=-50), np.random.uniform(low=-50, high=-20)],
                                    size=(grid_size, grid_size), p=[1 - warm_probability, warm_probability])

# Add hot pockets
hot_pocket_indices = np.random.choice(range(grid_size * grid_size), size=hot_pockets_count, replace=False)
hot_pocket_positions = np.unravel_index(hot_pocket_indices, (grid_size, grid_size))
temperature_grid[hot_pocket_positions] = hot_pocket_temp  # Set the temperature to the warmest value

# Set up the plot
fig, ax = plt.subplots()
cax = ax.imshow(temperature_grid, cmap='coolwarm', origin='lower', extent=[0, grid_size, 0, grid_size], vmin=-80, vmax=-20)
plt.colorbar(cax)

# Initial wind direction
wind_direction = np.array([1, 1])

# Draw a line to represent the initial wind direction
wind_line, = ax.plot([grid_size // 2, grid_size // 2 + wind_direction[0] * 10],
                     [grid_size // 2, grid_size // 2 + wind_direction[1] * 10], color='white')

# Add arrows to represent the initial wind influence
arrow_scale = 5
ax.quiver(grid_size // 2, grid_size // 2, wind_direction[0], wind_direction[1],
          scale=arrow_scale, color='white', scale_units='xy', angles='xy')

# Function to update the plot for each time step
def update(frame):
    global temperature_grid, wind_line, wind_direction
    # Apply finite-difference method to simulate heat transfer with wind
    dt = 0.1
    dx = 1.0
    alpha = 0.01
    # temperature_grid += alpha * (np.roll(temperature_grid, shift=(0, 1), axis=(0, 1)) +
    #                             np.roll(temperature_grid, shift=(0, -1), axis=(0, 1)) +
    #                             np.roll(temperature_grid, shift=(1, 0), axis=(0, 1)) +
    #                             np.roll(temperature_grid, shift=(-1, 0), axis=(0, 1)) -
    #                             4 * temperature_grid)
    wind_effect = (wind_direction[0] * np.roll(temperature_grid, shift=(0, 1), axis=(0, 1)) -
                   wind_direction[0] * temperature_grid +
                   wind_direction[1] * np.roll(temperature_grid, shift=(1, 0), axis=(0, 1)) -
                   wind_direction[1] * temperature_grid) / dx
    temperature_grid += dt * wind_speed * wind_effect

    cax.set_array(temperature_grid)

    # Update the line representing the wind direction
    wind_line.set_xdata([grid_size // 2, grid_size // 2 + wind_direction[0] * 10])
    wind_line.set_ydata([grid_size // 2, grid_size // 2 + wind_direction[1] * 10])

    # Change the wind direction every change_direction_frame frames
    if frame % change_direction_frame == 0:
        new_wind_direction = np.random.rand(2)  # Change to a random new direction
        new_wind_direction /= np.linalg.norm(new_wind_direction)  # Normalize the new direction
        wind_direction = new_wind_direction

        # Update the line for the new wind direction
        wind_line.set_xdata([grid_size // 2, grid_size // 2 + wind_direction[0] * 10])
        wind_line.set_ydata([grid_size // 2, grid_size // 2 + wind_direction[1] * 10])

    return cax, wind_line

# Create an animation
animation = FuncAnimation(fig, update, frames=time_steps, interval=10, blit=True)

plt.show()