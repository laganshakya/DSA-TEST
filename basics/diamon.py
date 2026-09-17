
# By chatGPT

def print_diamond(n):
  # Upper half of the diamond
  for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

  # Lower half of the diamond
  for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


# Driver code (n represents the number of rows in the upper half)
print_diamond(5)