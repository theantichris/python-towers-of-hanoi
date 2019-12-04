from stack import Stack

print ("Let's play Towers of Hanoi!\n")

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disks = int(input("How many disks do you want to play with: "))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3: "))

for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {} moves.".format(num_optimal_moves))

def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {} for {}".format(letter, name))
    user_input = input("").upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]


num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()

  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again.")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Movie. Try Again.")

print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}.".format(num_user_moves, num_optimal_moves))
