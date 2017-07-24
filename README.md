# Simple-Test-Generator
This test generator performs all actions by calling "takeAction". It implements a random test generator, but it only runs tests of "infinite" length, it never resets. This tester, given 60 seconds of testing time, will consistently produce a failed test for the following TSTL:
```python
pool: <int> 2

<int> := <[1..8]>
~<int> += 1

property: (<int> != 3)
```
The approach is to generate semi-exhaustive tests while taking code coverage into account.

## Usage
```python
python simple_test_gen.py
tstl simple.tstl
tstl_rt
```
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
