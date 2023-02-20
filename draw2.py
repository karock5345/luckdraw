import tkinter as tk
import random
import time

class RandomNumberGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Number Generator")
        
        self.range_label = tk.Label(self.master, text="Enter range of numbers:")
        self.range_label.pack()
        
        self.first_num = tk.Entry(self.master)
        self.first_num.pack()
        
        self.second_num = tk.Entry(self.master)
        self.second_num.pack()
        
        self.count_label = tk.Label(self.master, text="Enter number of outputs desired:")
        self.count_label.pack()
        
        self.count_entry = tk.Entry(self.master)
        self.count_entry.pack()
        
        self.generate_button = tk.Button(self.master, text="Generate", command=self.generate_numbers)
        self.generate_button.pack()
        
        self.output_label = tk.Label(self.master, text="")
        self.output_label.pack()
        
    def generate_numbers(self):
        first = int(self.first_num.get())
        second = int(self.second_num.get())
        count = int(self.count_entry.get())
        
        if second < first:
            self.output_label.config(text="Invalid range")
        elif count > (second - first + 1):
            self.output_label.config(text="Too many outputs requested")
        else:
            self.output_label.config(text="Generating numbers...")
            self.master.update()
            
            numbers = random.sample(range(first, second + 1), count)
            self.animate_roulette(numbers)
            
            numbers_str = ", ".join(str(x) for x in numbers)
            self.output_label.config(text="Generated numbers: " + numbers_str)
            
    def animate_roulette(self, numbers):
        for number in numbers:
            self.output_label.config(text="Selected number: " + str(number))
            self.master.update()
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()