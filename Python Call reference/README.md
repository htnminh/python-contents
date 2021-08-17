<!-- 















 $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$$\  $$ |\__$$  __|$$  _____|$$$\  $$ |\__$$  __|$$  __$$\ 
$$ /  \__|$$ /  $$ |$$$$\ $$ |   $$ |   $$ |      $$$$\ $$ |   $$ |   $$ /  \__|
$$ |      $$ |  $$ |$$ $$\$$ |   $$ |   $$$$$\    $$ $$\$$ |   $$ |   \$$$$$$\  
$$ |      $$ |  $$ |$$ \$$$$ |   $$ |   $$  __|   $$ \$$$$ |   $$ |    \____$$\ 
$$ |  $$\ $$ |  $$ |$$ |\$$$ |   $$ |   $$ |      $$ |\$$$ |   $$ |   $$\   $$ |
\$$$$$$  | $$$$$$  |$$ | \$$ |   $$ |   $$$$$$$$\ $$ | \$$ |   $$ |   \$$$$$$  |
 \______/  \______/ \__|  \__|   \__|   \________|\__|  \__|   \__|    \______/ 
                                     
-->

- [PYTHON CALL REFERENCE](#python-call-reference)
- [Built-in Functions](#built-in-functions)
  - [`abs()`](#abs)
  - [`bin()`](#bin)
  - [`complex()`](#complex)
  - [`dict()`](#dict)
  - [`dir()`](#dir)
  - [`divmod()`](#divmod)
  - [`enumerate()`](#enumerate)
  - [`eval()`](#eval)
  - [`float()`](#float)
  - [`format()`](#format)
  - [`frozenset()`](#frozenset)
  - [`help()`](#help)
  - [`hex()`](#hex)
  - [`input()`](#input)
  - [`int()`](#int)
  - [`isinstance()`](#isinstance)
  - [`issubclass()`](#issubclass)
  - [`len()`](#len)
  - [`list()`](#list)
  - [`map()`](#map)
  - [`max()`](#max)
  - [`min()`](#min)
  - [`oct()`](#oct)
  - [`open()`](#open)
  - [`ord()`](#ord)
  - [`pow()`](#pow)
  - [`print()`](#print)
  - [`range()`](#range)
  - [`reversed()`](#reversed)
  - [`round()`](#round)
  - [`class()`](#class)
  - [`slice()`](#slice)
  - [`sorted()`](#sorted)
  - [`str()`](#str)
  - [`sum()`](#sum)
  - [`super()`](#super)
  - [`tuple()`](#tuple)
  - [`type()`](#type)
  - [`zip()`](#zip)
- [Built-in Types](#built-in-types)
  - [Strings](#strings)
    - [`capitalize()`](#capitalize)
    - [`center()`](#center)
    - [`count()`](#count)
    - [`endswith()`](#endswith)
    - [`find()`](#find)
    - [`index()`](#index)
    - [`join()`](#join)
    - [`lower()`](#lower)
    - [`lstrip()`](#lstrip)
    - [`replace()`](#replace)
    - [`rfind()`](#rfind)
    - [`rindex()`](#rindex)
    - [`rstrip()`](#rstrip)
    - [`split()`](#split)
    - [`splitlines()`](#splitlines)
    - [`startswith()`](#startswith)
    - [`strip()`](#strip)
    - [`title()`](#title)
    - [`upper()`](#upper)
  - [Sets](#sets)
    - [`issubset()`](#issubset)
    - [`issuperset()`](#issuperset)
    - [`union()`](#union)
    - [`intersection()`](#intersection)
    - [`difference()`](#difference)
    - [`symmetric_difference()`](#symmetric_difference)
    - [`copy()`](#copy)
    - [`update()`](#update)
    - [`intersection_update()`](#intersection_update)
    - [`difference_update()`](#difference_update)
    - [`symmetric_difference_update()`](#symmetric_difference_update)
    - [`add()`](#add)
    - [`remove()`](#remove)
    - [`discard()`](#discard)
    - [`pop()`](#pop)
  - [Tuples](#tuples)
    - [`count()`](#count-1)
    - [`index()`](#index-1)
- [Data Structures](#data-structures)
  - [Lists](#lists)
    - [`append()`](#append)
    - [`extend()`](#extend)
    - [`insert()`](#insert)
    - [`remove()`](#remove-1)
    - [`pop()`](#pop-1)
    - [`index()`](#index-2)
    - [`count()`](#count-2)
    - [`sort()`](#sort)
    - [`reverse()`](#reverse)
    - [`copy()`](#copy-1)
  - [Dictionaries](#dictionaries)
    - [`iter()`](#iter)
    - [`copy()`](#copy-2)
    - [`get()`](#get)
    - [`items()`](#items)
    - [`keys()`](#keys)
    - [`pop()`](#pop-2)
    - [`popitem()`](#popitem)
    - [`setdefault()`](#setdefault)
    - [`update()`](#update-1)
    - [`values()`](#values)
- [Modules](#modules)
  - [`pickle`](#pickle)
    - [`dump()`](#dump)
    - [`load()`](#load)
  - [`random`](#random)
    - [`randrange()`](#randrange)
    - [`choice()`](#choice)
    - [`choices()`](#choices)
    - [`sample()`](#sample)
    - [`random()`](#random-1)
    - [`uniform()`](#uniform)
  - [`time`](#time)
    - [`sleep()`](#sleep)
    - [`time()`](#time-1)
  - [`math`](#math)
    - [`ceil()`](#ceil)
    - [`floor()`](#floor)
    - [`gcd()`](#gcd)
    - [`isclose()`](#isclose)
    - [`trunc()`](#trunc)
    - [`exp()`](#exp)
    - [`log()`](#log)
    - [`pow()`](#pow-1)
    - [`sqrt()`](#sqrt)
    - [`sin()`](#sin)
    - [`cos()`](#cos)
    - [`tan()`](#tan)
    - [`acos()`](#acos)
    - [`asin()`](#asin)
    - [`atan()`](#atan)
    - [`degrees()`](#degrees)
    - [`radians()`](#radians)
  - [`numpy`](#numpy)
    - [`numpy.array`](#numpyarray)
    - [`numpy.arange`](#numpyarange)
    - [`numpy.linspace`](#numpylinspace)
    - [`numpy.eye`](#numpyeye)
    - [`numpy.diag`](#numpydiag)
    - [`numpy.zeros`](#numpyzeros)
    - [`numpy.ones`](#numpyones)
    - [`numpy.ndarray.shape`](#numpyndarrayshape)
- [Files](#files)
  - [`read()`](#read)
  - [`write()`](#write)
  - [`tell()`](#tell)
  - [`seek()`](#seek)
- [Data model (Dunder or magic methods)](#data-model-dunder-or-magic-methods)

<!-- 















$$$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\  $$$$$$$$\ 
$$  __$$\ $$  _____|$$  _____|$$  _____|$$  __$$\ $$  _____|$$$\  $$ |$$  __$$\ $$  _____|
$$ |  $$ |$$ |      $$ |      $$ |      $$ |  $$ |$$ |      $$$$\ $$ |$$ /  \__|$$ |      
$$$$$$$  |$$$$$\    $$$$$\    $$$$$\    $$$$$$$  |$$$$$\    $$ $$\$$ |$$ |      $$$$$\    
$$  __$$< $$  __|   $$  __|   $$  __|   $$  __$$< $$  __|   $$ \$$$$ |$$ |      $$  __|   
$$ |  $$ |$$ |      $$ |      $$ |      $$ |  $$ |$$ |      $$ |\$$$ |$$ |  $$\ $$ |      
$$ |  $$ |$$$$$$$$\ $$ |      $$$$$$$$\ $$ |  $$ |$$$$$$$$\ $$ | \$$ |\$$$$$$  |$$$$$$$$\ 
\__|  \__|\________|\__|      \________|\__|  \__|\________|\__|  \__| \______/ \________|

-->


# PYTHON CALL REFERENCE
**Quick reference to some common classes, functions and methods of Python and its popular modules, without examples.**

For quick reference, each description only has one sentence, see the documentations provided for more details.

Some sections does not fully explain all the parameters provided.

***Written by Hoang Tran Nhat Minh,***

Hanoi University of Science and Technology,

Data Science and Artificial Intelligence - K65.

<!-- 















$$$$$$$$\ $$\   $$\ $$\   $$\  $$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\  
$$  _____|$$ |  $$ |$$$\  $$ |$$  __$$\\__$$  __|\_$$  _|$$  __$$\ $$$\  $$ |$$  __$$\ 
$$ |      $$ |  $$ |$$$$\ $$ |$$ /  \__|  $$ |     $$ |  $$ /  $$ |$$$$\ $$ |$$ /  \__|
$$$$$\    $$ |  $$ |$$ $$\$$ |$$ |        $$ |     $$ |  $$ |  $$ |$$ $$\$$ |\$$$$$$\  
$$  __|   $$ |  $$ |$$ \$$$$ |$$ |        $$ |     $$ |  $$ |  $$ |$$ \$$$$ | \____$$\ 
$$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$\   $$ |     $$ |  $$ |  $$ |$$ |\$$$ |$$\   $$ |
$$ |      \$$$$$$  |$$ | \$$ |\$$$$$$  |  $$ |   $$$$$$\  $$$$$$  |$$ | \$$ |\$$$$$$  |
\__|       \______/ \__|  \__| \______/   \__|   \______| \______/ \__|  \__| \______/ 
                                                                                       
-->

# Built-in Functions
**Doc: <https://docs.python.org/3/library/functions.html>**

## `abs()`
```py
abs(x)
```
Return the absolute value of a number.

## `bin()`
```py
bin(x)
```
Convert an integer number to a binary string prefixed with “`0b`”.

## `complex()`
```py
class complex([real[, imag]])
```
Return a complex number with the value `real` + `imag`*1j or convert a string or number to a complex number.

## `dict()`
```py
class dict(**kwarg)
```
```py
class dict(mapping, **kwarg)
```
```py
class dict(iterable, **kwarg)
```
Create a new dictionary.

## `dir()`
```py
dir([object])
```
With an argument, attempt to return a list of valid attributes for that `object`.

## `divmod()`
```py
divmod(a, b)
```
Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.

## `enumerate()`
```py
enumerate(iterable, start=0)
```
Return an enumerate object.

## `eval()`
```py
eval(expression[, globals[, locals]])
```
The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace.

## `float()`
```py
class float([x])
```
Return a floating point number constructed from a number or string `x`.

## `format()`
```py
format(value[, format_spec])
```
Convert a value to a “formatted” representation, as controlled by `format_spec`.

## `frozenset()`
```py
class frozenset([iterable])
```
Return a new `frozenset` object, optionally with elements taken from `iterable`. 

## `help()`
```py
help([object])
```
Invoke the built-in help system.

## `hex()`
```py
hex(x)
```
Convert an integer number to a lowercase hexadecimal string prefixed with “`0x`”.

## `input()`
```py
input([prompt])
```
The function reads a line from input, converts it to a string (stripping a trailing newline), and returns that. 

## `int()`
```py
class int([x])
```
```py
class int(x, base=10)
```
Return an integer object constructed from a number or string `x`, or return `0` if no arguments are given.

## `isinstance()`
```py
isinstance(object, classinfo)
```
Return `True` if the `object` argument is an instance of the `classinfo` argument, or of a (direct, indirect or virtual) subclass thereof.

## `issubclass()`
```py
issubclass(class, classinfo)
```
Return `True` if `class` is a subclass (direct, indirect or virtual) of `classinfo`. 

## `len()`
```py
len(s)
```
Return the length (the number of items) of an object.

## `list()`
```py
class list([iterable])
```
Rather than being a function, `list` is actually a mutable sequence type.


## `map()`
```py
map(function, iterable, ...)
```
Return an iterator that applies `function` to every item of `iterable`, yielding the results. 

## `max()`
```py
max(iterable, *[, key, default])
```
```py
max(arg1, arg2, *args[, key])
```
Return the largest item in an iterable or the largest of two or more arguments.


## `min()`
```py
min(iterable, *[, key, default])
```
```py
min(arg1, arg2, *args[, key])
```


## `oct()`
```py
oct(x)
```
Convert an integer number to an octal string prefixed with “`0o`”.


## `open()`
```py
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
Open `file` and return a corresponding file object.

## `ord()`
```py
ord(c)
```
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.

## `pow()`
```py
pow(base, exp[, mod])
```
Return `base` to the power `exp`; if mod is present, return base to the power exp, modulo `mod` (computed more efficiently than `pow(base, exp) % mod`). 

## `print()`
```py
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
Print `objects` to the text stream `file`, separated by `sep` and followed by `end`.

## `range()`
```py
class range(stop)
```
```py
class range(start, stop[, step])
```
Rather than being a function, `range` is actually an immutable sequence type.

## `reversed()`
```py
reversed(seq)
```
Return a reverse iterator.

## `round()`
```py
round(number[, ndigits])
```
Return `number` rounded to `ndigits` precision after the decimal point. 


## `class()`
```py
class set([iterable])
```
Return a new `set` object, optionally with elements taken from `iterable`.

## `slice()`
```py
class slice(stop)
```
```py
class slice(start, stop[, step])
```
Return a slice object representing the set of indices specified by `range(start, stop, step)`.

## `sorted()`
```py
sorted(iterable, *, key=None, reverse=False)
```
Return a new sorted list from the items in `iterable`.

## `str()`
```py
class str(object='')
```
```py
class str(object=b'', encoding='utf-8', errors='strict')
```
Return a `str` version of `object`.

## `sum()`
```py
sum(iterable, /, start=0)
```
Sums `start` and the items of an `iterable` from left to right and returns the total.

## `super()`
```py
super([type[, object-or-type]])
```
Return a proxy object that delegates method calls to a parent or sibling class of type, useful for accessing inherited methods that have been overridden in a class.

## `tuple()`
```py
class tuple([iterable])
```
Rather than being a function, `tuple` is actually an immutable sequence type.

## `type()`
```py
class type(object)
```
```py
class type(name, bases, dict, **kwds)
```
With one argument, return the type of an object. 

## `zip()`
```py
zip(*iterables)
```
Make an iterator that aggregates elements from each of the iterables.

<!-- 















$$$$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\  $$$$$$\  
\__$$  __|\$$\   $$  |$$  __$$\ $$  _____|$$  __$$\ 
   $$ |    \$$\ $$  / $$ |  $$ |$$ |      $$ /  \__|
   $$ |     \$$$$  /  $$$$$$$  |$$$$$\    \$$$$$$\  
   $$ |      \$$  /   $$  ____/ $$  __|    \____$$\ 
   $$ |       $$ |    $$ |      $$ |      $$\   $$ |
   $$ |       $$ |    $$ |      $$$$$$$$\ \$$$$$$  |
   \__|       \__|    \__|      \________| \______/ 
                                                    

-->

# Built-in Types
**Doc: <https://docs.python.org/3/library/stdtypes.html>**

<!-- 















 $$$$$$\    $$\               $$\                               
$$  __$$\   $$ |              \__|                              
$$ /  \__|$$$$$$\    $$$$$$\  $$\ $$$$$$$\   $$$$$$\   $$$$$$$\ 
\$$$$$$\  \_$$  _|  $$  __$$\ $$ |$$  __$$\ $$  __$$\ $$  _____|
 \____$$\   $$ |    $$ |  \__|$$ |$$ |  $$ |$$ /  $$ |\$$$$$$\  
$$\   $$ |  $$ |$$\ $$ |      $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
\$$$$$$  |  \$$$$  |$$ |      $$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  |
 \______/    \____/ \__|      \__|\__|  \__| \____$$ |\_______/ 
                                            $$\   $$ |          
                                            \$$$$$$  |          
                                             \______/           
-->
## Strings

### `capitalize()`
```py
str.capitalize()
```
Return a copy of the string with its first character capitalized and the rest lowercased.

### `center()`
```py
str.center(width[, fillchar])
```
Return centered in a string of length `width`.

### `count()`
```py
str.count(sub[, start[, end]])
```
Return the number of non-overlapping occurrences of substring `sub` in the range [`start`, `end`].

### `endswith()`
```py
str.endswith(suffix[, start[, end]])
```
Return `True` if the string ends with the specified `suffix`, otherwise return `False`.

### `find()`
```py
str.find(sub[, start[, end]])
```
Return the lowest index in the string where substring `sub` is found within the slice `s[start:end]`, else return `-1`.

### `index()`
```py
str.index(sub[, start[, end]])
```
Like `find()`, but raise `ValueError` when the substring is not found.

### `join()`
```py
str.join(iterable)
```
Return a string which is the concatenation of the strings in `iterable`.

### `lower()`
```py
str.lower()
```
Return a copy of the string with all the cased characters converted to lowercase.


### `lstrip()`
```py
str.lstrip([chars])
```
Return a copy of the string with leading characters removed.

### `replace()`
```py
str.replace(old, new[, count])
```
Return a copy of the string with all occurrences of substring `old` replaced by `new`.

### `rfind()`
```py
str.rfind(sub[, start[, end]])
```
Return the highest index in the string where substring `sub` is found, such that `sub` is contained within `s[start:end]`.

### `rindex()`
```py
str.rindex(sub[, start[, end]])
```
Like `rfind()` but raises `ValueError` when the substring `sub` is not found.

### `rstrip()`
```py
str.rstrip([chars])
```
Return a copy of the string with trailing characters removed.

### `split()`
```py
str.split(sep=None, maxsplit=-1)
```
Return a list of the words in the string, using `sep` as the delimiter string.

### `splitlines()`
```py
str.splitlines([keepends])
```
Return a list of the lines in the string, breaking at line boundaries.

### `startswith()`
```py
str.startswith(prefix[, start[, end]])
```
Return `True` if string starts with the `prefix`, otherwise return `False`.

### `strip()`
```py
str.strip([chars])
```
Return a copy of the string with the leading and trailing characters removed.

### `title()`
```py
str.title()
```
Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

### `upper()`
```py
str.upper()
```
Return a copy of the string with all the cased characters converted to uppercase.

<!-- 















 $$$$$$\             $$\               
$$  __$$\            $$ |              
$$ /  \__| $$$$$$\ $$$$$$\    $$$$$$$\ 
\$$$$$$\  $$  __$$\\_$$  _|  $$  _____|
 \____$$\ $$$$$$$$ | $$ |    \$$$$$$\  
$$\   $$ |$$   ____| $$ |$$\  \____$$\ 
\$$$$$$  |\$$$$$$$\  \$$$$  |$$$$$$$  |
 \______/  \_______|  \____/ \_______/ 
                                       
                                       
-->


## Sets

### `issubset()`
```py
issubset(other)
```
```py
set <= other
```
Test whether every element in the set is in other.

### `issuperset()`
```py
issuperset(other)
```
```py
set >= other
```
Test whether every element in other is in the set.

### `union()`
```py
union(*others)
```
```py
set | other | ...
```
Return a new set with elements from the set and all others.

### `intersection()`
```py
intersection(*others)
```
```py
set & other & ...
```
Return a new set with elements common to the set and all others.

### `difference()`
```py
difference(*others)
```
```py
set - other - ...
```
Return a new set with elements in the set that are not in the others.

### `symmetric_difference()`
```py
symmetric_difference(other)
```
```py
set ^ other
```
Return a new set with elements in either the set or other but not both.

### `copy()`
```py
copy()
```
Return a shallow copy of the set.

### `update()`
```py
update(*others)
```
```py
set |= other | ...
```
Update the set, adding elements from all others.

### `intersection_update()`
```py
intersection_update(*others)
```
```py
set &= other & ...
```
Update the set, keeping only elements found in it and all others.

### `difference_update()`
```py
difference_update(*others)
```
```py
set -= other | ...
```
Update the set, removing elements found in others.

### `symmetric_difference_update()`
```py
symmetric_difference_update(other)
```
```py
set ^= other
```
Update the set, keeping only elements found in either set, but not in both.

### `add()`
```py
add(elem)
```
Add element `elem` to the set.

### `remove()`
```py
remove(elem)
```
Remove element `elem` from the set or raise `KeyError` if `elem` is not contained in the set.

### `discard()`
```py
discard(elem)
```
Remove element `elem` from the set if it is present.

### `pop()`
```py
pop()
```
Remove and return an arbitrary element from the set or raises `KeyError` if the set is empty.

<!--















$$$$$$$$\                  $$\                     
\__$$  __|                 $$ |                    
   $$ |$$\   $$\  $$$$$$\  $$ | $$$$$$\   $$$$$$$\ 
   $$ |$$ |  $$ |$$  __$$\ $$ |$$  __$$\ $$  _____|
   $$ |$$ |  $$ |$$ /  $$ |$$ |$$$$$$$$ |\$$$$$$\  
   $$ |$$ |  $$ |$$ |  $$ |$$ |$$   ____| \____$$\ 
   $$ |\$$$$$$  |$$$$$$$  |$$ |\$$$$$$$\ $$$$$$$  |
   \__| \______/ $$  ____/ \__| \_______|\_______/ 
                 $$ |                              
                 $$ |                              
                 \__|                              
-->

## Tuples

### `count()`
```py
count(x)
```
Total number of occurrences of `x`.

### `index()`
```py
index(x[, i[, j]])
```
Index of the first occurrence of `x` (at or after index `i` and before index `j`)

<!-- 















$$$$$$$\   $$$$$$\ $$$$$$$$\  $$$$$$\         $$$$$$\ $$$$$$$$\ $$$$$$$\  $$\   $$\  $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\\__$$  __|$$  __$$\       $$  __$$\\__$$  __|$$  __$$\ $$ |  $$ |$$  __$$\\__$$  __|
$$ |  $$ |$$ /  $$ |  $$ |   $$ /  $$ |      $$ /  \__|  $$ |   $$ |  $$ |$$ |  $$ |$$ /  \__|  $$ |   
$$ |  $$ |$$$$$$$$ |  $$ |   $$$$$$$$ |      \$$$$$$\    $$ |   $$$$$$$  |$$ |  $$ |$$ |        $$ |   
$$ |  $$ |$$  __$$ |  $$ |   $$  __$$ |       \____$$\   $$ |   $$  __$$< $$ |  $$ |$$ |        $$ |   
$$ |  $$ |$$ |  $$ |  $$ |   $$ |  $$ |      $$\   $$ |  $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\   $$ |   
$$$$$$$  |$$ |  $$ |  $$ |   $$ |  $$ |      \$$$$$$  |  $$ |   $$ |  $$ |\$$$$$$  |\$$$$$$  |  $$ |   
\_______/ \__|  \__|  \__|   \__|  \__|       \______/   \__|   \__|  \__| \______/  \______/   \__|   
                                                                                                       
-->
# Data Structures
**Doc: <https://docs.python.org/3/tutorial/datastructures.html>**

<!-- 















$$\       $$\             $$\               
$$ |      \__|            $$ |              
$$ |      $$\  $$$$$$$\ $$$$$$\    $$$$$$$\ 
$$ |      $$ |$$  _____|\_$$  _|  $$  _____|
$$ |      $$ |\$$$$$$\    $$ |    \$$$$$$\  
$$ |      $$ | \____$$\   $$ |$$\  \____$$\ 
$$$$$$$$\ $$ |$$$$$$$  |  \$$$$  |$$$$$$$  |
\________|\__|\_______/    \____/ \_______/ 

-->

## Lists

### `append()`
```py
list.append(x)
```
Add an item to the end of the list.

### `extend()`
```py
list.extend(iterable)
```
Extend the list by appending all the items from the iterable.

### `insert()`
```py
list.insert(i, x)
```
Insert an item at a given position.

### `remove()`
```py
list.remove(x)
```
Remove the first item from the list whose value is equal to `x`.

### `pop()`
```py
list.pop([i])
```
Remove the item at the given position in the list, and return it; if no index is specified, it will be the last item in the list.

### `index()`
```py
list.index(x[, start[, end]])
```
Return zero-based index in the list of the first item whose value is equal to `x` or raise a `ValueError` if there is no such item.

### `count()`
```py
list.count(x)
```
Return the number of times x appears in the list.

### `sort()`
```py
list.sort(*, key=None, reverse=False)
```
Sort the items of the list in place.

### `reverse()`
```py
list.reverse()
```
Reverse the elements of the list in place.

### `copy()`
```py
list.copy()
```
Return a shallow copy of the list.

<!-- 















$$$$$$$\  $$\             $$\     $$\                                         $$\                     
$$  __$$\ \__|            $$ |    \__|                                        \__|                    
$$ |  $$ |$$\  $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$\  $$$$$$\   $$$$$$$\ 
$$ |  $$ |$$ |$$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\  \____$$\ $$  __$$\ $$ |$$  __$$\ $$  _____|
$$ |  $$ |$$ |$$ /        $$ |    $$ |$$ /  $$ |$$ |  $$ | $$$$$$$ |$$ |  \__|$$ |$$$$$$$$ |\$$$$$$\  
$$ |  $$ |$$ |$$ |        $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |$$  __$$ |$$ |      $$ |$$   ____| \____$$\ 
$$$$$$$  |$$ |\$$$$$$$\   \$$$$  |$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |      $$ |\$$$$$$$\ $$$$$$$  |
\_______/ \__| \_______|   \____/ \__| \______/ \__|  \__| \_______|\__|      \__| \_______|\_______/ 
                                                                                                                                                                 
 -->


## Dictionaries

### `iter()`
```py
iter(d)
```
Return an iterator over the keys of the dictionary, which is a shortcut for `iter(d.keys())`.

### `copy()`
```py
copy()
```
Return a shallow copy of the dictionary.

### `get()`
```py
get(key[, default])
```
Return the value for `key` if `key` is in the dictionary, else `default`; if `default` is not given, it defaults to None, so that this method never raises a `KeyError`.

### `items()`
```py
items()
```
Return a new view of the dictionary’s items (`(key, value)` pairs). 

### `keys()`
```py
keys()
```
Return a new view of the dictionary’s keys.

### `pop()`
```py
pop(key[, default])
```
If `key` is in the dictionary, remove it and return its value, else return `default`; if `default` is not given and `key` is not in the dictionary, a `KeyError` is raised.

### `popitem()`
```py
popitem()
```
Remove and return a `(key, value)` pair from the dictionary, pairs are returned in LIFO (last-in, first-out) order.

> *Changed in version 3.7*: LIFO order is now guaranteed. In prior versions, popitem() would return an arbitrary key/value pair.

### `setdefault()`
```py
setdefault(key[, default])
```
If `key` is in the dictionary, return its value. If not, insert `key` with a value of `default` and return `default`. `default` defaults to None.

### `update()`
```py
update([other])
```
Update the dictionary with the key/value pairs from `other`, overwriting existing keys, then return `None`.

### `values()`
```py
values()
```
Return a new view of the dictionary’s values.


<!--















$$\      $$\  $$$$$$\  $$$$$$$\  $$\   $$\ $$\       $$$$$$$$\  $$$$$$\  
$$$\    $$$ |$$  __$$\ $$  __$$\ $$ |  $$ |$$ |      $$  _____|$$  __$$\ 
$$$$\  $$$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ /  \__|
$$\$$\$$ $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$$$$\    \$$$$$$\  
$$ \$$$  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$  __|    \____$$\ 
$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$\   $$ |
$$ | \_/ $$ | $$$$$$  |$$$$$$$  |\$$$$$$  |$$$$$$$$\ $$$$$$$$\ \$$$$$$  |
\__|     \__| \______/ \_______/  \______/ \________|\________| \______/ 
                                                                         
-->

# Modules


<!-- 















          $$\           $$\       $$\           
          \__|          $$ |      $$ |          
 $$$$$$\  $$\  $$$$$$$\ $$ |  $$\ $$ | $$$$$$\  
$$  __$$\ $$ |$$  _____|$$ | $$  |$$ |$$  __$$\ 
$$ /  $$ |$$ |$$ /      $$$$$$  / $$ |$$$$$$$$ |
$$ |  $$ |$$ |$$ |      $$  _$$<  $$ |$$   ____|
$$$$$$$  |$$ |\$$$$$$$\ $$ | \$$\ $$ |\$$$$$$$\ 
$$  ____/ \__| \_______|\__|  \__|\__| \_______|
$$ |                                            
$$ |                                            
\__|                                            

-->

## `pickle`
Doc: <https://docs.python.org/3/library/pickle.html>

```py
import pickle
```

### `dump()`
```py
pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
```
Write the pickled representation of the object `obj` to the open file object `file`.

### `load()`
```py
pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
```
Read the pickled representation of an object from the open file object `file` and return the reconstituted object hierarchy specified therein.


<!-- 















                                   $$\                         
                                   $$ |                        
 $$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\  $$$$$$\$$$$\  
$$  __$$\ \____$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  _$$  _$$\ 
$$ |  \__|$$$$$$$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ / $$ / $$ |
$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |
$$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$  |$$ | $$ | $$ |
\__|      \_______|\__|  \__| \_______| \______/ \__| \__| \__|
                                                               
-->

## `random`
Doc: <https://docs.python.org/3/library/random.html>


```py
import random
```

### `randrange()`
```py
random.randrange(stop)
```
```py
random.randrange(start, stop[, step])
```
Return a randomly selected element from `range(start, stop, step)`, which is equivalent to `choice(range(start, stop, step))`, but doesn’t actually build a range object; the positional argument pattern matches that of `range()`.

### `choice()`
```py
random.choice(seq)
```
Return a random element from the non-empty sequence `seq`; if `seq` is empty, raises `IndexError`.

### `choices()`
```py
random.choices(population, weights=None, *, cum_weights=None, k=1)
```
Return a `k` sized list of elements chosen from the `population` with replacement; if the `population` is empty, raises IndexError.

### `sample()`
```py
random.sample(population, k, *, counts=None)
```
Return a `k` length list of unique elements chosen from the `population` sequence or set. 

### `random()`
```py
random.random()
```
Return the next random floating point number in the range [0.0, 1.0).

### `uniform()`
```py
random.uniform(a, b)
```
Return a random floating point number `N` such that `a <= N <= b` for `a <= b` and `b <= N <= a` for `b < a`; the end-point value `b` may or may not be included.


<!-- 















  $$\     $$\                         
  $$ |    \__|                        
$$$$$$\   $$\ $$$$$$\$$$$\   $$$$$$\  
\_$$  _|  $$ |$$  _$$  _$$\ $$  __$$\ 
  $$ |    $$ |$$ / $$ / $$ |$$$$$$$$ |
  $$ |$$\ $$ |$$ | $$ | $$ |$$   ____|
  \$$$$  |$$ |$$ | $$ | $$ |\$$$$$$$\ 
   \____/ \__|\__| \__| \__| \_______|
                                        
-->
## `time`
Doc: <https://docs.python.org/3/library/time.html>

```py
import time
```

### `sleep()`
```py
time.sleep(secs)
```
Suspend execution of the calling thread for the given number of seconds.

### `time()`
```py
time.time() → float
```
Return the time in seconds since the epoch as a floating point number.

<!-- 















                         $$\     $$\       
                         $$ |    $$ |      
$$$$$$\$$$$\   $$$$$$\ $$$$$$\   $$$$$$$\  
$$  _$$  _$$\  \____$$\\_$$  _|  $$  __$$\ 
$$ / $$ / $$ | $$$$$$$ | $$ |    $$ |  $$ |
$$ | $$ | $$ |$$  __$$ | $$ |$$\ $$ |  $$ |
$$ | $$ | $$ |\$$$$$$$ | \$$$$  |$$ |  $$ |
\__| \__| \__| \_______|  \____/ \__|  \__|

-->
## `math`
Doc: <https://docs.python.org/3/library/math.html>

```py
import math
```

### `ceil()`
```py
math.ceil(x)
```
Return the ceiling of `x`, the smallest integer greater than or equal to `x`.

### `floor()`
```py
math.floor(x)
```
Return the floor of `x`, the largest integer less than or equal to `x`.

### `gcd()`
```py
math.gcd(*integers)
```
Return the greatest common divisor of the specified integer arguments. 

### `isclose()`
```py
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
```
Return `True` if the values `a` and `b` are close to each other and `False` otherwise.

### `trunc()`
```py
math.trunc(x)
```
Return the `Real` value `x` truncated to an `Integral` (usually an integer).

### `exp()`
```py
math.exp(x)
```
Return `e` raised to the power `x`, where `e` = 2.718281… is the base of natural logarithms.

### `log()`
```py
math.log(x[, base])
```
With one argument, return the natural logarithm of `x` (to base `e`); with two arguments, return the logarithm of `x` to the given `base`.

### `pow()`
```py
math.pow(x, y)
```
Return `x` raised to the power `y`.

### `sqrt()`
```py
math.sqrt(x)
```
Return the square root of x.

### `sin()`
```py
math.sin(x)
```
Return the sine of `x` radians.

### `cos()`
```py
math.cos(x)
```
Return the cosine of `x` radians.

### `tan()`
```py
math.tan(x)
```
Return the tangent of `x` radians.

### `acos()`
```py
math.acos(x)
```
Return the arc cosine of `x`, in radians.

### `asin()`
```py
math.asin(x)
```
Return the arc sine of `x`, in radians.

### `atan()`
```py
math.atan(x)
```
Return the arc tangent of x, in radians.

### `degrees()`
```py
math.degrees(x)
```
Convert angle `x` from radians to degrees.

### `radians()`
```py
math.radians(x)
```
Convert angle `x` from degrees to radians.

<!--
                                     
 












                                    
$$$$$$$\  $$\   $$\ $$$$$$\$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ / $$ / $$ |$$ /  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$ |
\__|  \__| \______/ \__| \__| \__|$$  ____/  \____$$ |
                                  $$ |      $$\   $$ |
                                  $$ |      \$$$$$$  |
                                  \__|       \______/ 

-->

## `numpy`
Doc: <https://numpy.org/doc/stable/>

I will not copy nor explain their documentation here. In my opinion, the doc of `numpy` is a bit long but it is really clear and specific, and you will have to seek for help on their doc as long as you work on data related fields.

If you are searching for infomation for the final exam, please search at the Appendix.

```py
import numpy
```

### `numpy.array`
```py
numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
```

### `numpy.arange`
```py
numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
```


### `numpy.linspace`
```py
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
```


### `numpy.eye`
```py
numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)
```


### `numpy.diag`
```py
numpy.diag(v, k=0)
```


### `numpy.zeros`
```py
numpy.zeros(shape, dtype=float, order='C', *, like=None)
```


### `numpy.ones`
```py
numpy.ones(shape, dtype=None, order='C', *, like=None)
```


### `numpy.ndarray.shape`
```py
ndarray.shape
```

<!--















$$$$$$$$\ $$$$$$\ $$\       $$$$$$$$\  $$$$$$\  
$$  _____|\_$$  _|$$ |      $$  _____|$$  __$$\ 
$$ |        $$ |  $$ |      $$ |      $$ /  \__|
$$$$$\      $$ |  $$ |      $$$$$\    \$$$$$$\  
$$  __|     $$ |  $$ |      $$  __|    \____$$\ 
$$ |        $$ |  $$ |      $$ |      $$\   $$ |
$$ |      $$$$$$\ $$$$$$$$\ $$$$$$$$\ \$$$$$$  |
\__|      \______|\________|\________| \______/ 
                                                                                 
-->

# Files
Doc: <https://docs.python.org/3/tutorial/inputoutput.html>

## `read()`
```py
f.read([size])
```
Read a file’s contents, return it as a string (in text mode) or bytes object (in binary mode); when `size` is omitted or negative, the entire contents of the file will be read and returned.

## `write()`
```py
f.write(string)
```
Write the contents of `string` to the file, return the number of characters written.

## `tell()`
```py
f.tell()
```
Return an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

## `seek()`
```py
f.seek(offset[, whence])
```
Change the file object’s position; the position is computed from adding `offset` to a reference point; the reference point is selected by the `whence` argument; a `whence` value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point; `whence` can be omitted and defaults to 0.

<!--















$$$$$$$\   $$$$$$\ $$$$$$$$\  $$$$$$\        $$\      $$\  $$$$$$\  $$$$$$$\  $$$$$$$$\ $$\       
$$  __$$\ $$  __$$\\__$$  __|$$  __$$\       $$$\    $$$ |$$  __$$\ $$  __$$\ $$  _____|$$ |      
$$ |  $$ |$$ /  $$ |  $$ |   $$ /  $$ |      $$$$\  $$$$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |      
$$ |  $$ |$$$$$$$$ |  $$ |   $$$$$$$$ |      $$\$$\$$ $$ |$$ |  $$ |$$ |  $$ |$$$$$\    $$ |      
$$ |  $$ |$$  __$$ |  $$ |   $$  __$$ |      $$ \$$$  $$ |$$ |  $$ |$$ |  $$ |$$  __|   $$ |      
$$ |  $$ |$$ |  $$ |  $$ |   $$ |  $$ |      $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      
$$$$$$$  |$$ |  $$ |  $$ |   $$ |  $$ |      $$ | \_/ $$ | $$$$$$  |$$$$$$$  |$$$$$$$$\ $$$$$$$$\ 
\_______/ \__|  \__|  \__|   \__|  \__|      \__|     \__| \______/ \_______/ \________|\________|

-->

# Data model (Dunder or magic methods)
Doc: <https://docs.python.org/3/reference/datamodel.html>

This section is of a table form to avoid confusion and... tiredness.

| This dunder method... | Means |
|-----------------------|-------|
|`object.__doc__`| docstring
|`object.__name__`| name
||
|`object.__lt__`| `<`
|`object.__le__`| `<=`
|`object.__ne__`| `!=`
|`object.__gt__`| `>`
|`object.__ge__`| `>=`
|`object.__dir__`| `dir()`
||
|`object.__add__(self, other)`| `+`
|`object.__sub__(self, other)`| `-`
|`object.__mul__(self, other)`| `*`
|`object.__truediv__(self, other)`| `/`
|`object.__floordiv__(self, other)`| `//`
||
|`object.__mod__(self, other)`| `%`
|`object.__divmod__(self, other)`| `divmod()`
|`object.__pow__(self, other[, modulo])`| `pow()`, `**`
||
|`object.__and__(self, other)`| `&`
|`object.__xor__(self, other)`| `^`
|`object.__or__(self, other)`| `\|`

