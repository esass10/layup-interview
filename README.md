# Layup Interview

This project contains two Python programs designed as part of an interview take-home assignment. The applications include:

- **Airplane Control Simulation**: A 2D simulation where users can control an airplane's yaw angle and airspeed, with real-time visualization of its trajectory.
- **Layup Sequence Calculation**: A script to compute values in a custom sequence using dynamic programming.

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure Python 3.x is installed on your system. You can check by running:

   ```
   python3 --version
   ```

2. **Virtual Environment (Recommended)**: Set up a virtual environment to isolate dependencies.

### Step-by-Step Setup

1. **Clone the Repository**

   ```
   git clone https://github.com/esass10/layup-interview.git
   cd layup-interview
   ```

2. **Create and Activate a Virtual Environment**

   - On macOS/Linux:

     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:

     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**

   - Install all necessary packages from `requirements.txt`:

     ```
     pip install -r requirements.txt
     ```

### Requirements Explanation

- `matplotlib` and `numpy` are required for `sequence.py` for plotting on the graph.
  `tkinter` is used in `airplane.py` for the graphical interface. On macOS, if `tkinter` is not available by default, you can install it with:

  ```
  brew install python-tk
  ```

## How to Run Each Program

1. **Airplane Control Simulation** (`airplane.py`):

   ```
   python3 airplane.py
   ```

- **Controls**:
  - **Yaw Angle (degrees)**: Input to adjust the airplane’s direction.
  - **Airspeed (knots)**: Input to control speed.
  - **Update Controls Button**: Applies the yaw angle and speed changes.
  - **Reset Button**: Clears the trajectory and resets the airplane to its initial position.
  - **Note**: 0° points the airplane upward, following aviation conventions.

2. **Layup Sequence Calculation** (`sequence.py`):

   ```
   python3 sequence.py
   ```

- This script calculates the 10,000th term in a sequence defined by a custom recurrence relation. It also measures runtime, analyzes time complexity in a commented report, and plots runtime for various values of N up to 10,000 to visualize time complexity.

## Airplane Control Simulation Documentation

### Overview

This application simulates the control of an airplane moving on a 2D plane at a fixed altitude. Users can adjust yaw angle and airspeed, and the airplane’s trajectory updates dynamically on a canvas, wrapping around edges for continuous plane movement.

### Trajectory Calculation Logic

1. **Angle and Movement Calculation**:

   - The yaw angle (in degrees) is adjusted so that `0°` points upward on the screen.
   - The adjusted angle is converted to radians and used to calculate `dx` and `dy` (change in `x` and `y`
     positions):

     ```
     dx = math.cos(adjusted_angle_in_radians) * speed
     dy = math.sin(adjusted_angle_in_radians) * speed
     ```

2. **Position Update**:

   - The new position (`new_x`, `new_y`) is computed by adding `dx` and `dy` to the current coordinates.
   - If the new position goes beyond the canvas boundaries, the airplane wraps around to the opposite edge.

3. **Trajectory Drawing**:

   - The application draws a line segment from the previous position to the new position on each update, creating a continuous trajectory.

4. **Airplane Icon**:

   - A triangle represents the airplane, pointing in the direction of travel and recalculated each update based on the yaw angle.
