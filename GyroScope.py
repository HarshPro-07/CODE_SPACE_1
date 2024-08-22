import tkinter as tk
from time import sleep
import keyboard

# Initialize main window
root = tk.Tk()
root.title("X and Y Value Tracker")

# Create a label widget to display the x and y values
status_label = tk.Label(root, text="x : 0 :: y : 0", font=('Helvetica', 24))
status_label.pack(pady=20)

x, y = 0, 0
dx, dy = 5, 5  # Rate of Change in angles

def update_label():
    """Update the label with the current values of x and y."""
    status_label.config(text=f"x : {x} :: y : {y}")
    root.update()  # Update the tkinter window to reflect the changes

def main_loop():
    global x, y
    
    # This loop will continuously check for key presses and update values
    while True:
        if keyboard.is_pressed('x'):
            if keyboard.is_pressed('+'):
                if x >= 360:
                    x = 0
                x += dx
            elif keyboard.is_pressed('-'):
                if x <= -360:
                    x = 0
                x -= dx

        elif keyboard.is_pressed('y'):
            if keyboard.is_pressed('+'):
                if y >= 360:
                    y = 0
                y += dy
            elif keyboard.is_pressed('-'):
                if y <= -360:
                    y = 0
                y -= dy

        update_label()  # Update the tkinter window with new values of x and y
        sleep(0.05)  # Delay to prevent excessive CPU usage

# Run the main loop in a separate thread to avoid freezing the GUI
root.after(10, main_loop)

# Start the tkinter main loop
root.mainloop()

