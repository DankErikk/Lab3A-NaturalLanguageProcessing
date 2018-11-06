# Erik Rivera
# Lab3A
# CS2302 TR @ 10:30-11:50 
# Professor Aguirre, Diego
# TA Saha, Manoj
# Date of last modification 11/5/2018
# Purpose of this lab assigment is to gain familiarity with bst in avl or redblack formats
# This lab uses word embeddings to get the similarity between to words


import string
import random
from AVLTree import AVLTree
from AVLTree import Node
from RedBlackTree import RedBlackTree
from RedBlackTree import RBTNode

# This creates an avl tree from a file based off the glove files
def createAVLTree(file_name):
    avlTree = AVLTree()
    with open(file_name) as file:
        alphabet = list(string.ascii_letters)
        for line in file:
            array = line.split(" ")
            word = array[0]
            if alphabet.__contains__(word[0]):
                numbers = []
                for num in array[1:]:
                    numbers.append(float(num))
                wordNode = Node(word, numbers)
                avlTree.insert(wordNode)
    return avlTree

# This creates a RedBlack tree from a file based off the glove files
def createRedBlackTree(file_name):
    redBlackTree = RedBlackTree()
    with open(file_name) as file:
        alphabet = list(string.ascii_letters)
        for line in file:
            array = line.split(" ")
            word = array[0]
            if alphabet.__contains__(word[0]):
                numbers = []
                for num in array[1:]:
                    numbers.append(float(num))
                wordNode = RBTNode(word, None,None, None, None, numbers)
                redBlackTree.insert_node(wordNode)
    return redBlackTree
    
# This recursively prints a tree in which the ROOT node is given
def __printTree__(root):
    temp = root
    if temp is None:
        return
    __printTree__(temp.left)
    print(temp.key)
    __printTree__(temp.right)

# This will generate a text file and call it word_pairs.txt
def generate_text_file(file_name):
    limit = 100
    counter = 0
    word_pairs_file = open("word_pairs.txt", "w+")
    with open(file_name) as file:
        alphabet = list(string.ascii_letters)
        for line in file:
            # Check that current line starts with a word
            array = line.split(" ")
            word = array[0]
            # If the element begins with a character in the alphabet
            # then it is a word
            
            # Set limit to chose how many word pairs to write
            if alphabet.__contains__(word[0]) and counter<limit:
                word_pairs_file.write(word + " " + str(get_Random_Word(file_name))+ "\n")
                counter+=1

# This method will return a random word in the file
def get_Random_Word(file_name):
    random_int = random.randint(0, get_num_lines(file_name))
    with open(file_name) as file:
        i = 0
        for line in file:
            if i !=random_int:
                i +=1
                continue
            else:
                array = line.split(" ")
                word = array[0]
                alphabet = list(string.ascii_letters)
                if alphabet.__contains__(word[0]):
                    return word
                return get_Random_Word(file_name)
            
# This method will return amount of lines in a file
def get_num_lines(file_name):
    counter = 0
    with open(file_name) as file:
        for line in file:
            counter +=1
    return counter

def main():
    file_name = "test.txt"
    # Read the file, store each word and its embedding into an avl or redblack tree.
    # Only use words in the text file
    print("Would you like to use a AVL[1] or Red Black Tree[2]?")
    while True:
            try:
                user_ans = int(input("Please enter 1 or 2...\n"))
            except ValueError:
                print("Sorry that is not a number...\n")
                continue
            if user_ans!=1 and user_ans!=2:
                continue
            else:
                break
    if user_ans == 1:
        print("You chose 1!")
        userTree = createAVLTree(file_name)
    if user_ans == 2:
        print("Your chose 2!")
        userTree = createRedBlackTree(file_name)
    # Now we have the tree as userTree
    
    # Read another file containing pairs of words (two per line) and for every pair of words
    # find similarity of words using word pairs text file
     

    # Generate text file with word pairs
    generate_text_file(file_name)

    # TODO: Finish this fucking assignment cuz tis already late af
    # TODO: implement formula and rest of assignment
    

    
main()