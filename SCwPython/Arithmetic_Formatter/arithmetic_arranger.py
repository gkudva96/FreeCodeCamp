def arithmetic_arranger(problems, show_answer = False):

  # If the user has supplied more than 5 problems
  if len(problems) > 5:
    return("Error: Too many problems.")

  # List for each operand and the operator
  operand_1, operator, operand_2, answers = [], [], [], []
  max_length = []

  # For each problem
  for problem in problems:

    # Splitting the string into constituent units
    o1, op, o2 = problem.split(' ')
    operand_1.append(o1)
    operator.append(op)
    operand_2.append(o2)

    # If either operand contains more than 4 digits
    if len(o1) > 4 or len(o2) > 4:
      return("Error: Numbers cannot be more than four digits.")

    # Determining the max length of each expression
    max_length.append(max(len(o1), len(o2)))

    # If the operands contain non-digits
    try:
      o1 = int(o1)
      o2 = int(o2)
    except:
      return("Error: Numbers must only contain digits.")
    
    # If the operator is not '+' or '-'
    if op not in ['+', '-']:
      return("Error: Operator must be '+' or '-'.")

    # Computing the answer
    answer = o1 + o2 if op == '+' else o1 - o2
    answers.append(str(answer))
    
  # Formatted display
  first_line, second_line, third_line, fourth_line = '', '', '', ''
  
  for i in range(len(operand_1)):

    # Adding the number of preceeding white-spaces
    first_line += ' ' * (2 + max_length[i] - len(operand_1[i]))
    second_line += operator[i] + ' ' * (1 + max_length[i] - len(operand_2[i]))
    third_line += '-' * (2 + max_length[i])
    fourth_line += ' ' * (2 + max_length[i] - len(answers[i]))

    # Adding the operand itself
    first_line += operand_1[i]
    second_line += operand_2[i]
    fourth_line += answers[i]

    # Adding the 4 white-spaces after each problem
    if i != len(operand_1) - 1:
      first_line += ' ' * 4
      second_line += ' ' * 4
      third_line += ' ' * 4
      fourth_line += ' ' * 4
  
  # Adding the trailing newline character
  first_line += '\n'
  second_line += '\n'
  if show_answer:
    third_line += '\n'
  
  # Option to display the answer
  if not show_answer:
    arranged_problems = first_line + second_line + third_line
  else:
    arranged_problems = first_line + second_line + third_line + fourth_line
  
  # Returning the formatted display
  return arranged_problems