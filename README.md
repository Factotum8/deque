# Deque
It is training task.

## The task description
There is a double ended queue implementation.

## Example
```
$ python /deque/main.py
>> 4
>> 4
>> push_front 861
>> push_front -819
>> pop_back
861
>> pop_back
-819
```

## Install requirements
1. Python >= 3.9

## Sources
* /deque/deque/deque.py - main module with a algorithm logic.  
  Project submodules:
* /deque/main.py - provides a console tools for the deque.
* /deque/deque/tests/test_deque.py - packages tests.


## RUN TEST 
* cd into project dir
* run `python -m unittest discover ./deque/tests/`

## License
[LICENSE MIT](LICENSE)