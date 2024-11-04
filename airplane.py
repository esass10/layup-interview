import tkinter as tk
import math

class AirplaneControlApp:
    def __init__(self, root):
        # Set up the main window and canvas
        self.root = root
        self.root.title("Airplane Control Simulation")
        
        # Canvas dimensions and initialization
        self.canvas_width, self.canvas_height = 1200, 800
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Set initial values for the airplane's position and movement
        self.x, self.y = self.canvas_width / 2, self.canvas_height / 2
        self.angle = 0  # Yaw angle in degrees
        self.speed = 0  # Airspeed in knots
        self.previous_position = (self.x, self.y)

        # Yaw angle input
        tk.Label(root, text="Yaw Angle (degrees)").pack()
        self.angle_entry = tk.Entry(root)
        self.angle_entry.pack()
        self.angle_entry.insert(0, "0")

        # Airspeed input
        tk.Label(root, text="Airspeed (knots)").pack()
        self.speed_entry = tk.Entry(root)
        self.speed_entry.pack()
        self.speed_entry.insert(0, "0")

        # Buttons to update and reset controls
        update_button = tk.Button(root, text="Update Controls", command=self.update_controls)
        update_button.pack()
        reset_button = tk.Button(root, text="Reset", command=self.reset)
        reset_button.pack()

        # Start the trajectory update loop
        self.update_trajectory()

    def update_controls(self):
        # Get the angle and speed from user input
        try:
            self.angle = float(self.angle_entry.get())
            self.speed = float(self.speed_entry.get())
        except ValueError:
            print("Please enter valid numbers for angle and speed")

    def update_trajectory(self):
        # Adjust angle so 0 degrees points to the top of the screen
        adjusted_angle = self.angle - 90
        radians = math.radians(adjusted_angle)
        dx = math.cos(radians) * self.speed * 0.1  # Adjust speed down for smooth movement
        dy = math.sin(radians) * self.speed * 0.1

        # Update the position
        new_x, new_y = self.x + dx, self.y + dy
        wrapped = False

        # Wrap around the canvas edges
        if new_x > self.canvas_width:
            new_x -= self.canvas_width
            wrapped = True
        elif new_x < 0:
            new_x += self.canvas_width
            wrapped = True
        if new_y > self.canvas_height:
            new_y -= self.canvas_height
            wrapped = True
        elif new_y < 0:
            new_y += self.canvas_height
            wrapped = True

        # Draw the trajectory line if no wrapping happened
        if not wrapped:
            self.canvas.create_line(self.previous_position[0], self.previous_position[1], new_x, new_y, fill="black")

        # Update airplane position and redraw the airplane icon
        self.x, self.y = new_x, new_y
        self.previous_position = (self.x, self.y)
        self.draw_airplane()

        # Schedule the next plane update
        self.root.after(50, self.update_trajectory)

    def draw_airplane(self):
        # Clear the previous airplane icon
        self.canvas.delete("airplane")

        # Adjust angle so 0 degrees points to the top of the screen
        adjusted_angle = self.angle - 90
        angle_rad = math.radians(adjusted_angle)

        # Draw a triangle to represent the airplane, pointing in the direction of travel
        size = 10
        p1 = (self.x + size * math.cos(angle_rad), self.y + size * math.sin(angle_rad))
        p2 = (self.x + size * math.cos(angle_rad + 2.5), self.y + size * math.sin(angle_rad + 2.5))
        p3 = (self.x + size * math.cos(angle_rad - 2.5), self.y + size * math.sin(angle_rad - 2.5))

        # Draw the airplane icon as a triangle
        self.canvas.create_polygon(p1, p2, p3, fill="brown", tags="airplane")

    def reset(self):
        # Reset position, angle, and speed to initial values
        self.x, self.y = self.canvas_width / 2, self.canvas_height / 2
        self.angle, self.speed = 0, 0
        self.previous_position = (self.x, self.y)

        # Clear the canvas and input fields
        self.canvas.delete("all")
        self.angle_entry.delete(0, tk.END)
        self.angle_entry.insert(0, "0")
        self.speed_entry.delete(0, tk.END)
        self.speed_entry.insert(0, "0")

        # Redraw the airplane at the reset position
        self.draw_airplane()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AirplaneControlApp(root)
    root.mainloop()
