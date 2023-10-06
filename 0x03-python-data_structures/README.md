PYTHON DATA STRUCTURES

list.append(x) add x to a list
list.extend(iterable) extend list  by appending all the items from the iterable.
list.insert(i, x) insert an item at a given position in a list first argument is index to insert
list.remove(x) removes item ehose value is x from a list
list.pop([i]) remove item at positon i and return it if i is not specified a.pop() removes and returns the last element in the list.
list.clear() == del a[:] removes all items from the list.
list.index(x[, start[, end]]) return a zero based index in the list of the first item whose vlue is equal to x raises value error if there is no such item.optional arg start and end are slice notation are used to limit the search 
list.count(x) returns the number of times x appears in the list.
list.sort(*, key=None, reverse=False) sort items in the list
list.reverse() reverse the elements of the list in place
list.copy() returns a shallow copy of the list == a[:]

insert remove and sort - modify the list and have no return value printed return the default None.this is adesign principle for all mutable data structures in python.

sorted() = used to sort iterables such as list tuples and strings and return a new sorted list.
sorted(iterable, key=key, reverse=reverse)
iterable(list, tuple, string)
key(optional) - a fxn to extract a comparison key from each element
reverse - Boolean indicating whether to sort in descending order
reverse does not return a modified list thus to return a modified list. new_list = vlist(reversed(list))
