# Nothing
## A functional NoneType

A basic Callable NoneType !

Use this object to write generic code pipelines
Makes your life easier when using the railway paradigm

Using Nothing lets you avoid errors like:

    - AttributeError: "NoneType" object has no attribute ...
    - TypeError: "NoneType" object is not callable
    - TypeError: bad operand type for unary ...: "NoneType"
    - TypeError: unsupported operand type(s) for ...: "NoneType" and ...
    - TypeError: type NoneType doesn't define __round__ method
    - TypeError: 'NoneType' object is not subscriptable
    - ...

Just define your code pipeline using Nothing when your function hits a problem and let the flow guide your logic towards the failing strategy without crashing

```python
from nothing import Nothing
from random import choice
from typing import *

def meaning() -> Union[Nothing, bool]:
    if choice([True, False]):
        return 42
    return Nothing

def action(number: Union[Nothing, int]) -> Union[Nothing, int]:
    return (number // 2) + 1

def apply(func: Union[Callable, Nothing], *args:Union[AnyType, Nothing]) -> Union[AnyType, Nothing]:
    return func(*args)

def functor(string:str) -> Callable:
    if string == "add":
        return lambda *args: sum(args)
    return Nothing

def pipeline():
    meaning_of_life = meaning()
    # do a bunch of operations with the value
    new_meaning = action(meaning_of_life)
    divider = functor("sub")
    final_result = divider(new_meaning, 3)
    if final_result is Nothing:
        return Nothing
    return final_result

if __name__ == "__main__":
    result = pipeline()
    if result is Nothing:
        print("Pipeline failed")
    print("Pipeline success !")
```