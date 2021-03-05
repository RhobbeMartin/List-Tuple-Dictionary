## List

A data structure that is a mutable (changeable) ordered sequence of elements defined by having values between square brackets, [].

*Ex.*

```python

groceryList = ["chips", "ice cream", "chocolate", "pizza", "banana", "pinaple"] # List of Strings
```
### Indexing List
Each item in a list corresponds to an index number, which is an integer, starting with 0.

'len(grocerylist)' --6
len() gives us the length of our list

### List Functions
-LIST.append(Element) # Adds an item to the end of List
'groceryList.append("milk")'
- LIST.insert(INDEX, Element) # Add an item to the index location
'groceryList.insert(2, "apples")'
-LIST.remove(Element) # Searches the list andremoves item'groceryList.remove("banana")
'groceryList.remove("banana)'
-LIST.pop(INDEX) # Remove an item at the specified index
'groceryList.pop(4)

To reference an item we use List[Index]

## Tuple

Another type of list that stores data/values inside but in parentheses().
unlike lists, tuples __cannot__ be changed (they are immutable).

'colors = ("blue", "red", "yellow")'
'print(colors[2])' --> yellow


## Dictionary
Another type of list that stores data/values inside curly brackets {}
Similar to a list, it is mutable (changeable), however, the index is a key, which is linked to a data/value.

```python
students = {
  "visham" : "029138",
  "jake" : "123894",
  "Ben" : "848592",
}
print(students["visham])
```
>029138