"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
def main():
  """Get user score, generate random score and print both results."""

  user_score = float(input("Enter your score: "))
  result = get_score_result(user_score)
  print(result)

  random_score = random.randint(0, 100)
  print(f"Random score: {random_score}")  # Generate a random score
  print(get_score_result(random_score))

def get_score_result(score):
  """Determine result based on the score."""
  if score < 0 or score > 100:
    return "Invalid score"
  elif score < 50:
    return "Bad"
  elif score <= 90:
    return "Passable"
  else:
    return "Excellent"

main()