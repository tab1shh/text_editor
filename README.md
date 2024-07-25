# Simple Text Editor
A simple text editor implemented in Python using a linked list to store the text and a stack to manage undo operations.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [LinkedList](#linkedList)
  - [Stack](#stack)
  - [Main](#main)

## Overview
This projects aims to implement a text editor with the use of fundamental data structures such as linked lists and stacks. It allows basic text manipulation such as insertion, deletion, and undoing the last action

## Features
- Insert characters into the text
- Delete the last character
- Undo the last action (insert or delete)

## Setup
To run this project, you need Python installed on your system. Follow these steps to set up and run the text editor:

1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Run the main script:
```bash
python main.py
```

## Usage
Once the program is running, you will see a simple command-line interface with options to insert characters, delete the last character, undo the last action, or quit the program.
Example interaction:
```bash
Text Editor
Current text: 
Options: (I)nsert, (D)elete, (U)ndo, (Q)uit
Choose an option: I
Enter character to insert: H
Current text: H
Options: (I)nsert, (D)elete, (U)ndo, (Q)uit
Choose an option: I
Enter character to insert: i
Current text: Hi
Options: (I)nsert, (D)elete, (U)ndo, (Q)uit
Choose an option: U
Current text: H
Options: (I)nsert, (D)elete, (U)ndo, (Q)uit
Choose an option: Q
```

## Code Overview
### LinkedList
'linked_list.py' contains the 'Node' and 'LinkedList' classes . The 'LinkedList' class provides methods to append data to the end of the list, delete the last node, and convert the list to a string.

### Stack
'stack.py' contains the 'Stack' class which provides methods to push data onto the stack, pop data from the stack, and check if the stack is empty.

### Main
'main.py' contains the 'TextEditor' class and the main program loop. The 'TextEditor' class uses a 'LinkedList' to store the text and a 'Stack' to manage undo operations.