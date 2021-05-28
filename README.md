# FLL-td-extras
Testing utilities

# graph_data.py
Minimal robot output data visualizer

## Usage
```sh
python graph_data.py [path/to/robot/data/file] [call number] [independent var. number] [dependent var. number]
```
where: <br>
- **call number** : *within [0, n]* = function call to read data from
- **independent var. number** : *within [1, n]* = the position of the independent variable
- **dependent var. number** : *within [1, n]* = the position of the dependent variable

### Example
```sh
python graph_data.py test.dat 0 1 2
```
where:
- *test.dat* = path to data
- *0* = 1st function call
- *1* = the independent variable is the second number on any given line of the given function call
- *2* = the dependent variable is the second number on any given line of the given function call

# epsilon.py
Program for calculating staircase-ing error from robot output data

## Usage
```sh
python epsilon.py [path/to/robot/output/data/file]
```
