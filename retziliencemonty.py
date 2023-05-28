import tkinter as tk
from tkinter import messagebox
import random
import os

# File to log the results
LOG_FILE = '/Users/renatofigueiredo/Documents/montylog.txt'
LOGGING_ENABLED = True

class MontyHallApp:
    def __init__(self, master):
        self.master = master
        master.title("Monty Hall Retzilience Simulator")

        self.label = tk.Label(master, text="Enter the number of doors and trials")
        self.label.pack()

        self.doors_label = tk.Label(master, text="Number of doors")
        self.doors_label.pack()

        self.doors_entry = tk.Entry(master)
        self.doors_entry.pack()

        self.trials_label = tk.Label(master, text="Number of trials")
        self.trials_label.pack()

        self.trials_entry = tk.Entry(master)
        self.trials_entry.pack()

        self.run_button = tk.Button(master, text="Run simulation", command=self.run_simulation)
        self.run_button.pack()

    def run_simulation(self):
        try:
            N = int(self.doors_entry.get())
            num_trials = int(self.trials_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values")
            return

        stick_wins = 0
        switch_wins = 0
        for _ in range(num_trials):
            stick, switch = self.simulate_game(N)
            if stick:
                stick_wins += 1
            if switch:
                switch_wins += 1

        prob_stick = stick_wins / num_trials
        prob_switch = switch_wins / num_trials

        if LOGGING_ENABLED:
            with open(LOG_FILE, 'a') as f:
                f.write(f"After {num_trials} trials with {N} doors:\n")
                f.write(f"Probability of winning if stick with first choice: {prob_stick}\n")
                f.write(f"Probability of winning if always switch: {prob_switch}\n")
                f.write("\n")

        messagebox.showinfo("Results", f"After {num_trials} trials with {N} doors:\n"
                                    f"Probability of winning if stick with first choice: {prob_stick}\n"
                                    f"Probability of winning if always switch: {prob_switch}")

    def simulate_game(self, N):
        doors = list(range(N))
        prize_door = random.choice(doors)
        first_choice = random.choice(doors)
        if first_choice == prize_door:
            doors.remove(first_choice)
            doors_to_open = doors
            door_to_leave_closed = random.choice(doors_to_open)
        else:
            doors.remove(first_choice)
            doors.remove(prize_door)
            doors_to_open = doors
            door_to_leave_closed = prize_door
        switch_choice = door_to_leave_closed
        return first_choice == prize_door, switch_choice == prize_door

root = tk.Tk()
app = MontyHallApp(root)
root.mainloop()
