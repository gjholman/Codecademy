from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks = [left_stack, middle_stack, right_stack]

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while(num_disks < 3):
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
        
for i in range(num_disks,0,-1):
  left_stack.push(i)
  
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {num_moves} moves".format(num_moves=num_optimal_moves))

def get_input():
  while True:
    choices=[]
    for i in range(len(stacks)):
      choices.append(stacks[i].get_name()[0])
      #print("Press {letter} for {name}".format(letter=stacks[i].get_name()[0], name=stacks[i].get_name()))
    user_input = input()
    
    for j in range(len(choices)):
      if user_input==choices[j]:
        print("You have selected stack {stack}".format(stack=j))
        return stacks[j]
    
#Play the game!
num_user_moves = 0

while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
    
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      to_stack.push(from_stack.pop())
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try again")
      

print("\n\nYou completed the game in {this_many} moves, and the optimal number of moves is {that_many}".format(this_many=num_user_moves, that_many=num_optimal_moves))
