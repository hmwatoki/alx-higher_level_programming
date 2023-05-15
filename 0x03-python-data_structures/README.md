# Welcome to my Python project on Data Structures: Lists, Tuples

This is my project for the ALX SE bootcamp on Python Data Structures: Lists, Tuples. I'll be learning we how to use these structures to store and manipulate data like a pro. But before we dive in, let me introduce myself.

My name is Harry, and I'm a Python enthusiast. I love using this language. It's really cool :)

## What are Lists and Tuples?

Lists and tuples are two of the most commonly used data structures in Python. They allow us to store a collection of items in a single variable, which we can then access and manipulate as needed. Here's a quick rundown of each structure:

- **Lists**: A list is a collection of items that are ordered and changeable. we can add, remove, or modify items in a list, and we can access individual items by their index.
- **Tuples**: A tuple is similar to a list, but it's immutable, which means we can't change the items after we create it. Tuples are often used to store related pieces of information that shouldn't be changed, like the coordinates of a point on a map.

## How to Use Lists and Tuples

Now that we know what lists and tuples are, let's dive into how to use them in Python. Here are some common operations we might perform with these structures:

- **Creating a list or tuple**: To create a list or tuple, we simply put the items inside square brackets (for a list) or parentheses (for a tuple), separated by commas. For example:
`python mylist = [1, 2, 3, 4, 5] mytuple = ("apple", "banana", "cherry")`


- **Accessing items in a list or tuple**: To access an item in a list or tuple, we use its index. Keep in mind that Python uses zero-based indexing, which means the first item in the list or tuple is at index 0. For example:
`python mylist = [1, 2, 3, 4, 5] firstitem = mylist[0]' # This will be 1 lastitem = my_list[-1] # This will be 5`


- **Adding items to a list**: To add an item to the end of a list, we can use the `append()` method. For example:
`python mylist = [1, 2, 3, 4, 5] mylist.append(6) # This will add 6 to the end of the list`

- **Removing items from a list**: To remove an item from a list, we can use the `remove()` method. For example:
`python mylist = [1, 2, 3, 4, 5] mylist.remove(3)`
