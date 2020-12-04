# Importing Libraries
import math

# Class definition for category object
class Category:

  # Constructor Method
  def __init__(self, category_name):
    self.category_name = category_name
    self.ledger = []

  # Deposit Method
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount" : amount, "description" : description})

  # Get Balance Method
  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry['amount']
    return balance

  # Check Funds Method
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  # Withdraw Method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount" : -amount, "description" : description})
      return True
    else:
      return False

  # Transfer Method
  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_category.category_name)
      budget_category.deposit(amount, "Transfer from " + self.category_name)
      return True
    else:
      return False

  # Method invoked when the object is printed
  def __str__(self):
    object_string = ""
    num_asterisks = (30 - len(self.category_name)) // 2
    first_line = ("*" * num_asterisks) + self.category_name + ("*" * num_asterisks)
    if len(first_line) < 30:
      first_line += '*'
    object_string += first_line + '\n'
    for entry in self.ledger:
      temp_description = entry['description'][0:23] if len(entry['description']) > 23 else entry['description']
      object_string += f"{temp_description:<23}{entry['amount']:>7.2f}\n"
    object_string += f"Total: {self.get_balance():.2f}"
    return object_string

# Function definition to display bar chart of percentage spent per category
def create_spend_chart(categories):

  # Total amount spent
  total_spent_amount = 0

  # Amount spent per category
  amount_per_category = [0] * len(categories)

  # For each category in the list of categories
  for i in range(len(categories)):
    # For each entry in the ledger of that category
    for entry in categories[i].ledger:
      # Only adding the withdrawals
      if entry['amount'] < 0:
        total_spent_amount += abs(entry['amount'])
        amount_per_category[i] += abs(entry['amount'])
  
  # Calculating percentage spent per category
  percentage_per_category = [0] * len(categories)
  for i in range(len(categories)):
    percentage_per_category[i] = math.floor((amount_per_category[i] / total_spent_amount) * 100)

  # Displaying the bar chart
  final_string = ""
  final_string += "Percentage spent by category\n"
  for x in range(100, -1, -10):
    init_string = f"{x:>3}| "
    for p in percentage_per_category:
      if x <= p:
        init_string += "o  "
      else:
        init_string += "   "
    init_string += '\n'
    final_string += init_string
  final_string += " " * 4 + "-" * (3 * len(categories) + 1) + '\n'
  max_category_name_length = max([len(x.category_name) for x in categories])
  for x in range(max_category_name_length):
    init_string = " " * 5
    for category in categories:
      if x < len(category.category_name):
        init_string += category.category_name[x] + " " * 2
      else:
        init_string += " " * 3
    init_string += '\n'
    final_string += init_string
  
  # Returning the bar chart string
  return final_string[0:-1]