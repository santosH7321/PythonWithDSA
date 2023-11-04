# Python Collection (Arrays)

1. Lists
2. Tuple
3. Set
4. Dictionary

## List: 
#### These allow us to store multiple items in a single variable.

> fruits = ["Apple", "Banana", "Charry"]

#### List Items
. Indexed
. Ordered
. Mutable (That mean changable)
. Duplication allowed
. Any dataype 
. Mix of different data types

## Accessing items of a list

1. Indexing
2. Negative indexing
3. Range of indexes
4. Rangge of negative indexes

> 1. list[2]
> 2. list[-2]
> 3. list[starting(inclusive) : ending(exclusive)]
> 4. list[1:3]

## Adding elements to a list

1. append() (add item to the end of the list)
2. insert()  --> ()
3. extend()

#### append()
```
list = [10,20,30,40]
list.append(50)
```

#### insert()
> 1. [10,20,30,40,50]
> list.insert(2,60)
> [10,20,60,30,40,50]

#### extend()
list.extend(list2)
##### 




## Removing elements from a list
1. remove()
2. pop()

## Change item in a list
1. At an index
2. In a range



## Sorting a list

1. Asecending
2. Desending


## List Comprehension
#### when we want to make a new list from items of an existing list 

> list = [10,20,30,40]
newlist = [ i for i in list if i > 25]

## Nasted Lists


## Tuples
#### use to multiple items in a variables

#### ex: 
colours = ("blue", "green", "red")


1. Orederd
2. Immutable (Value is not changable)
3. Duplicates allowed
4. Any datatype
5. Mix of different data types

# Tuple vs List

1. Iterating through a 'tuple ' is faster than in a 'list'.

2. 'Lists' are mutable 'tuples' are immutable.

3. Tuples that contain immutable elements can be used as a key for a distionary

# Sets 
#### contain for storing multiple values in a variable 

> names = {"John","May","Dave"}

#### set items
1. Unordered
2. Immutable
3. Unindexed
4. Duplicates not allowed 
5. Any datatypes
6. Mix of different data types



# Dictionary
#### Be store key value pair 

#### Creating a dictionary
> numbers = {
    "John" : 8825848
    "Ria" : 94849394
    "Joy" : 9084902385
 }

 > dect = {
    key1 : value
    key2 : value2
 }

 ## Dictionary items
 1. Ordered
 2. Changeable
 3. Unindexed
 4. Duplicates not allowed
 5. Any  datatype