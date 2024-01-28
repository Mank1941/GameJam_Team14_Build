# Wildfire Simulation with Wind Animation

This Python script simulates the spread of a wildfire on a grid using a simple finite-difference method. The wildfire is influenced by wind, which changes direction periodically.

## Requirements
- Python 3
- NumPy
- Matplotlib

## How to Use
1. Install the required dependencies using `pip install numpy matplotlib`.
2. Copy and paste the provided code into a Python file (e.g., `wildfire_simulation.py`).
3. Run the script using `python wildfire_simulation.py`.

## Parameters
- `grid_size`: Size of the grid for the simulation.
- `time_steps`: Total number of time steps for the simulation.
- `wind_speed`: Speed of the wind influencing the wildfire.
- `warm_probability`: Probability of a cell being warm initially.
- `change_direction_frame`: Frame interval at which the wind direction changes.
- `hot_pocket`: Probability of having a hot pocket on the grid.
- `hot_pocket_temp`: Temperature of the hot pockets.
- `hot_pockets_count`: Number of hot pockets added to the grid.

## Initial Setup
The simulation initializes a grid with random warm and cold cells. Hot pockets, represented by cells with an elevated temperature, are added to the grid.

## Plot
The Matplotlib plot displays the initial grid with temperature values. The white line and arrows represent the initial wind direction.

## Animation
The animation simulates the wildfire spread over time. The wind direction changes periodically, affecting the spread pattern.

## Simulation Update
The script uses a finite-difference method to simulate heat transfer with wind, updating the temperature grid at each time step.

Feel free to modify the parameters and experiment with different configurations to observe the wildfire's behavior under various conditions.