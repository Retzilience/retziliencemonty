# Quantum Choices and the Monty Hall Problem: A Study in Probabilistic Decision Making

Welcome to the _Monty Hall Retzilience Simulator_! This is not just another Monty Hall problem simulator, it is an adventure in the quantum landscape of choices and probabilities. Let's unravel the Monty Hall problem, but this time with a flavor of quantum mechanics.

## The Classic Monty Hall Problem

Here's the classic setup: you're on a game show with three doors. Behind one door is a car; behind the other two, goats. You pick a door, say, Door #1. Now, the host, who knows what's behind the doors, opens another door, say, Door #3, which has a goat. Now he gives you a choice: do you want to stick with your original choice (Door #1) or switch to the remaining unopened door (Door #2)?

As counter-intuitive as it may seem, the best strategy is to **always switch**. By switching, your probability of winning the car goes up to 2/3, as opposed to sticking with your original choice which has a probability of 1/3.

## The Quantum Choice Perspective

Much like the quantum world, where particles exist in multiple states until observed, the car is behind all the doors until Monty opens a door. In other words, the Monty Hall problem exhibits a form of _quantum superposition_ - multiple potential realities existing simultaneously. The act of Monty opening a door is akin to the observation that 'collapses' this superposition, leaving us with a new set of probabilities.

## But What if We Increase the Number of Doors?

If three doors make you scratch your head, how about a hundred? Or a thousand? The core idea behind this simulator is to take the Monty Hall problem to the extreme. When you increase the number of doors, the benefit of switching becomes exponentially apparent and confirms what was once counter-intuitive as something fundamentally intuitive. And this is precisely what our _Monty Hall Retzilience Simulator_ does - it allows you to simulate the game with as many doors and trials as you'd like.

## The Power of Simulation

The _Monty Hall Retzilience Simulator_ combines the power of Python's random module with the intuitive graphical user interface of tkinter, providing an engaging and insightful way to explore this problem. The program simulates thousands of Monty Hall games in a matter of seconds, collecting data on the outcomes based on whether you stick or switch. This way, you can see the surprising power of the switching strategy in action.

Remember, probability isn't just theory - it's reality playing out. And our simulator is a sandbox where this reality unfolds. The Monty Hall problem is a beautiful demonstration of how our intuition can often lead us astray in the face of hard probabilistic truth. By simulating the problem, we don't just understand it - we experience it.

## Wrapping Up

The Monty Hall problem is a fascinating journey into the world of probability, and our simulator serves as your tour guide. By allowing for an arbitrary number of doors and trials, it illuminates the counter-intuitive reality of the problem. It is not just a program; it's a digital playground to experience the whimsical world of quantum choices. So go ahead, step into the quantum landscape of doors, and remember, sometimes it's wiser to switch!

# Setting Up and Running the Monty Hall Retzilience Simulator: A Friendly Guide

Welcome to the fun part! Let's get the Monty Hall Retzilience Simulator up and running on your machine. Don't worry if you're a newbie to coding, this is a no-jargon zone! Follow these steps, and you'll have it running in no time.

## Step 1: Installing Python

First things first, we need to make sure Python is installed on your system. Here's how:

### Windows:

1. Visit the [Python downloads page](https://www.python.org/downloads/windows/).
2. Click on the latest Python release.
3. Download and run the installation package.
4. Make sure to tick the box that says "Add Python to PATH" before clicking on Install.

### MacOS:

1. Open Terminal (you can find it in Applications -> Utilities).
2. Type in `brew install python3` and hit Enter (you need to have Homebrew installed, a handy package manager for MacOS. If you don't, head over to the [Homebrew site](https://brew.sh/) and follow the instructions there).
3. Wait for the magic to happen!

### Linux:

1. Open Terminal.
2. Type `sudo apt-get install python3.8` and hit Enter.
3. Type in your password when prompted and wait for Python to be installed.

## Step 2: Installing Anaconda Navigator

Anaconda Navigator is a great tool that simplifies the management of Python packages and environments. It also comes with Tkinter, a library needed for our script to run. Here's how to install it:

1. Visit the [Anaconda distribution page](https://www.anaconda.com/distribution/).
2. Download the installer for your operating system and follow the installation instructions provided there.

## Step 3: Cloning the Repository

We've stored the Monty Hall Retzilience Simulator script in a GitHub repository. To copy this repository to your local machine, follow these steps:

1. Navigate to the GitHub repository page ( https://github.com/Retzilience/retziliencemonty ).
2. Click on the 'Code' button and copy the URL shown.
3. Open Terminal (or Command Prompt for Windows users).
4. Navigate to the location where you want to clone the repository by typing `cd path_to_your_directory`. 
5. Type `git clone ` and paste the URL you copied from the GitHub page.
6. Press Enter to clone the repository.

## Step 4: Setting up the Log File

Our simulator keeps track of each simulation in a log file. You need to set the path to where this file will be created:

1. Open the cloned `retziliencemonty.py` file in a text editor.
2. Look for the line `LOG_FILE = '/your_path/montylog.txt'`.
3. Replace `'/your_path/montylog.txt'` with the path where you want the log file to be created, e.g., `'/Users/YourName/Documents/montylog.txt'` for MacOS or `'C:/Users/YourName/Documents/montylog.txt'` for Windows.
4. Save and close the file.

## Step 5: Running the Simulator

Now, it's time to bring our simulator to life!

1. Open Anaconda Navigator.
2. Click on the 'Environments' tab.
3. Find 'base(root)' in the list and click on the play button on the right.
4. Select 'Open Terminal'.
5. In the Terminal, navigate to the location of the `retziliencemonty.py` file using the `cd` command.
6. Type `python3 retziliencemonty.py` and hit Enter.

Congratulations! You're now running

 the Monty Hall Retzilience Simulator! Enter the number of doors and trials, and witness the magic of probability unfold!

Remember, there are no goats or cars behind the doors, just quantum probabilities waiting to be unraveled. Happy exploring!
