import re
def arithmetic_arranger(problems, answer=False):
  output = ""
  firstline = ""
  secondline = ""
  thirdline = ""
  answerline = ""
  if len(problems) > 5:
    return "Error: Too many problems."
  # symbol = "[+|-]"
  for problem in problems:
    question1 , capture, question2 = problem.split()
    if capture not in ['+','-']:
      return "Error: Operator must be '+' or '-'."
    # question = re.split(symbol, i)
    question1 = question1.strip()
    question2 = question2.strip()
    if len(question1) > 4 or len(question2) > 4:
      return "Error: Numbers cannot be more than four digits."
    if not question1.isnumeric() or not question2.isnumeric():
      return "Error: Numbers must only contain digits."
    max_length = max(len(question1), len(question2)) + 2
    firstline += question1.rjust(max_length) + "    "
    secondline += capture + " " + question2.rjust(max_length - 2) + "    "
    thirdline += "-" * max_length + "    "
    if answer == True:
      if (capture[0] == "+"):
        solution = str(int(question1) + int(question2))
      else:
        solution = str(int(question1) - int(question2))
      answerline += solution.rjust(max_length) + "    "
  output += firstline.rstrip() + "\n"
  output += secondline.rstrip() + "\n"
  output += thirdline.rstrip()
  if answer:
    output += "\n" + answerline.rstrip()
  return output
