# main.py

from prob_calculator import Hat, experiment

# Get user input for hat and expected balls
hat_input = input("Enter the hat configuration (e.g., {'black': 6, 'red': 4, 'green': 3}): ")
hat = Hat(**eval(hat_input))

expected_balls_input = input("Enter the expected balls configuration (e.g., {'red': 2, 'green': 1}): ")
expected_balls = eval(expected_balls_input)

# Get user input for the number of balls drawn and experiments
num_balls_drawn = int(input("Enter the number of balls to draw: "))
num_experiments = int(input("Enter the number of experiments to perform: "))

# Run the experiment
probability = experiment(hat=hat, expected_balls=expected_balls, num_balls_drawn=num_balls_drawn, num_experiments=num_experiments)

print("Probability:", probability)
