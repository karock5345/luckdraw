import tkinter as tk
import random

class RandomNumberGenerator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Random Number Generator")
        self.geometry("300x200")

        # Input fields
        self.range_start = tk.Entry(self)
        self.range_start.pack()
        self.range_end = tk.Entry(self)
        self.range_end.pack()
        self.quantity = tk.Entry(self)
        self.quantity.pack()

        # Generate numbers button
        self.generate_button = tk.Button(self, text="Generate Numbers", command=self.generate_numbers)
        self.generate_button.pack()

        # Results label
        self.results_label = tk.Label(self, text="")
        self.results_label.pack()

    def generate_numbers(self):
        try:
            # Get the inputs
            start = int(self.range_start.get())
            end = int(self.range_end.get())
            qty = int(self.quantity.get())

            # Generate the numbers
            numbers = random.sample(range(start, end), qty)

            # Update the results label
            self.results_label.config(text=numbers)
        except ValueError:
            self.results_label.config(text="Invalid input. Please enter integers for start, end, and quantity.")

app = RandomNumberGenerator()
app.mainloop()