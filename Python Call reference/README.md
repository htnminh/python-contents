# PYTHON CALL REFERENCE
**Quick reference to some common classes, functions and methods of Python and its popular modules, without examples.**

Each description only has one sentence, see the documentation for more details.

***Written by Hoang Tran Nhat Minh,***

Hanoi University of Science and Technology,

Data Science and Artificial Intelligence - K65.

# Built-in Functions and Methods
**Doc: <https://docs.python.org/3/library/functions.html#print>**

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
