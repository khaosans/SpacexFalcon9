import tkinter as tk
from chakraui import ChakraUI

def display_dashboard():
    # Create the main window
    root = tk.Tk()
    root.title("DeFi Dashboard")

    # Create input fields for job parameters using Chakra UI components
    job_parameters = ChakraUI.Input(
        label="Job Parameters:",
        placeholder="Enter job details",
        type="text"
    )

    # Create a button to submit the job
    tk.Button(root, text="Submit Job", command=lambda: print("Job submitted")).grid(row=2)

    # Create a label to display running jobs
    tk.Label(root, text="Running Jobs:").grid(row=3)
    tk.Label(root, text="None").grid(row=4)

    root.mainloop()

display_dashboard()
