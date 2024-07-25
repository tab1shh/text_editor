from linked_list import LinkedList
from stack import Stack

class TextEditor:
    def __init__ (self):
        self.text = LinkedList() # store text
        self.undo_stack = Stack() # keep track of actions for undo functionality

    def insert(self, char):
        self.text.append(char) # adds 'char' to end of the linked list 'self.text'
        self.undo_stack.push(('insert', char)) # pushes a tuple '('insert', char)' onto stack to keep track of this action for undo purposes

    def delete(self):
        deleted_char = self.text.delete_last() # deletes last character from linked list and and stores it in 'deleted_char'
        if deleted_char: # checks if character was deleted
            self.undo_stack.push(('delete', deleted_char)) # pushes a tuple '('delete', delete_char)' onto stack to keep track of this action for undo purposes

    def undo(self):
        if self.undo_stack.is_empty(): # checks if undo stack is empty, and to return if it is
            return
        action, char = self.undo_stack.pop() # pops last action from undo stack
        if action == 'insert': # if last action was 'insert' it deletes last character
            self.text.delete_last()
        elif action == 'delete': # if last action was 'delete' it re inserts the character
            self.text.append(char)
    
    def __str__(self):
        return str(self.text)
    
def main():
    editor = TextEditor()

    while True:
        print("Text Editor")
        print("Current text:", editor)
        print("Options: (I)nsert, (D)elete, (U)ndo, (Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == 'I':
            char = input("Enter character to insert: ")
            editor.insert(char)
        elif choice == 'D':
            editor.delete()
        elif choice == 'U':
            editor.undo()
        elif choice == 'Q':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    
