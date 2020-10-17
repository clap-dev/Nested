
# Nested

Nested is a smart, lightweight, and iterative algorithm to parse *complexly* nested json. 

## Usage
```python
from nested import parse

data = {"rows":[{"elements":[{"distance":{"text":"227 mi","value":365468},"duration":{"text":"3 hours 54 mins","value":14064},"status":"OK"},{"distance":{"text":"94.6 mi","value":152193},"duration":{"text":"1 hour 44 mins","value":6227},"status":"OK"}]}]}
parsed_data = parse(data, 'text') #Replace "text" with the key that you are trying to parse
print(parsed_data)
```

## How does it work?

Nested works by the following,

Firstly, nested will load your json dictionary into a list, and pop the first index of the list. It will then check whether the popped item is a list, or a dict. If it is a list, it will extend the `items` list with the new list it has found, otherwise if it is a dict it will check if the key you are looking for is inside of the dict that has been found, and if it is, it will append the keys value to a results list. Now you may be asking, "What if it extends the list with a string or integer?", well, I've thought of that. As you can see, it uses `isinstance` to check if it is a dict or a list completely ignoring anything else. This way, it will not run into issues trying to parse you your values!
