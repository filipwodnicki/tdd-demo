# tdd-demo
Test-Driven Development (TDD) demo repo  
Filip Wodnicki 2021  

## Objective
The purpose of this repo is demonstrate Test-Driven development (TDD)  

Please see the [commit history](https://github.com/filipwodnicki/tdd-demo/commits/main) for TDD process and flow.  

### Scenario

The following scenario is used to write the demo code.  
```
Write a function using TDD that takes a matrix as an argument. This matrix represents an image of shape [10, 10, 3] with values encoded as 8-bit integers (values 0 to 255). The function should transform the image to grayscale. Finally, the function should normalize the image from 0 to 1 as floating point numbers. Then return the image.
```

## Solution
`demo.py` - scenario solution
`tests/test_demo.py` - testing solution

## Usage

### Install
In the command line, run: `pip install -r requirements.txt`  

### Run sample code
In the command line, run: `python demo.py`  

### Run tests
In the command line, run: `python -m unittest tests/*`  

## Final thoughts

* Was great to refresh on numpy dimensions and types.  
* TDD FTW!  

### Future
* Add CLI and perhaps popup with the image generated  
* fetch an actual image :) 
