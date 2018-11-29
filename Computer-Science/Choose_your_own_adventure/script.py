### This is a codecademy project for learning about trees. This is an interactive terminal game using tree structures in python
### Start time:12:05
print('Once Upon a Time....')
#Treenode class
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []
    def add_child(self, node):
        self.choices.append(node)
    def traverse(self):
        story_node = self
        while len(story_node.choices) != 0:
            print(story_node.story_piece)
            while True:
                selection = input()
                num_select = int(selection) - 1
                if num_select < len(story_node.choices):
                    story_node = story_node.choices[num_select]
                    break
                print("Invalid input, try again!") 
        print(story_node.story_piece)
        print("End game")

user_name = input("What is your name? \n")

### Variables for tree with parent definitions underneath
#Story root is the start or the 'root' of the tree
story_root = TreeNode(
"""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""
)

# Choice a from root -> Roar Back
choice_a = TreeNode(
"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
)
story_root.add_child(choice_a)

# Choice b from root -> Run to the left...
choice_b = TreeNode(
"""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
)
story_root.add_child(choice_b)

choice_a_1 = TreeNode(
"""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
)
choice_a.add_child(choice_a_1)

choice_a_2 = TreeNode(
"""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""
)
choice_a.add_child(choice_a_2)


choice_b_1 = TreeNode(
"""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
)
choice_b.add_child(choice_b_1)


choice_b_2 = TreeNode(
"""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
)
choice_b.add_child(choice_b_2)


#Testing Area
story_root.traverse()


