# Importing libraries
import random
import copy

# Class definition for the hat object
class Hat:

  # Constructor Method
  def __init__(self, **kwargs):
    self.contents = [k for k, v in kwargs.items() for i in range(v)]
  
  # Draw Method
  def draw(self, num_balls):
    if num_balls < len(self.contents):
      drawn_balls = []
      for i in range(num_balls):
        drawn_ball = random.choice(self.contents)
        drawn_balls.append(drawn_ball)
        self.contents.remove(drawn_ball)
      return drawn_balls
    else:
      return self.contents

# Function definition to carry out the experiment
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # Accumulator for the number of successes
  num_success = 0

  # For each experiment
  for n in range(num_experiments):
    # Creating a deep copy of the hat object passed
    temp_hat = copy.deepcopy(hat)
    # Drawing the required number of balls from the hat
    drawn_balls = temp_hat.draw(num_balls_drawn)
    # Indicator flag for success
    success_flag = 1
    # For each expected ball and its count
    for k, v in expected_balls.items():
      # If the count is atleast the required count, then continue
      if drawn_balls.count(k) >= v:
        continue
      # If not, then experiment is a failure
      else:
        success_flag = 0
        break
    # Count the number of successful experiments
    if success_flag:
      num_success += 1 
  
  # Calculating the probability
  return (num_success / num_experiments)