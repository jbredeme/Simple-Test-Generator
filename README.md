# Simple-Test-Generator
This test generator performs all actions by calling "takeAction". This implementation of a random test generator generates semi-exhaustive tests while taking code coverage into account. This tester, given 60 seconds of testing time, will consistently produce a failed test for the following TSTL:
```python
pool: <int> 2

<int> := <[1..8]>
~<int> += 1

property: (<int> != 3)
```

## Usage
```python
python simple_test_gen.py
tstl simple.tstl
tstl_rt
```

## Example Output
<img src="https://github.com/jbredeme/Simple-Test-Generator/blob/master/scrnsht.png" width="256">

## Dependencies
* [Python 2.7.x](https://www.python.org/) - Implementation language.

## Author
* **Jarid Bredemeier**

## Resources
* [Template Scripting Testing Language Tool]
* [An introduction to property-based testing]
* [Change history for Coverage]

[Template Scripting Testing Language Tool]: https://github.com/agroce/tstl
[An introduction to property-based testing]: http://fsharpforfunandprofit.com/posts/property-based-testing/
[Change history for Coverage]: https://coverage.readthedocs.io/en/coverage-4.3.4/changes.html
