#The function should return num raised to the 10th power
def tenth_power(num):
    return num ** 10

# Write a function named square_root() that has one parameter named num.
def square_root(num):
  return num ** 0.5
#
# print(square_root(16))

#Create a function called win_percentage() that takes two parameters named wins and losses.
def win_percentage(wins,losses):
   return (losses + wins) * wins

print(win_percentage(5, 5))