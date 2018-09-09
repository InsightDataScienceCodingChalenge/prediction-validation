# Insight Coding Challenge

### Author: Anvesh Kumar Perugu

## Challenge

* Calculating the average difference between the actual stock prices and predicted values over a specified sliding time window.

## Implementation Details

* Programming Language: Python
* Version: 3.6

## Algorithm

* Reading both the text files(actual.txt and predicted.txt) and storing each entry in a dictionary.
* Getting the minimum hour entry of the stock data
* Getting the maximum hour entry of the stock data
* Comparing both the dictionaries using sliding window with one hour duration and writing to the output file with the average error calculated.

## Execution detials

* Install Virtual environment and run the bash script from it and can install any other modules using pip install in virtual environment if required.
* Run shell script run.sh which will execute python main.py

## Test Details

* As mentioned, Some of the average error values are +/- 0.01 of the expected value due to rounding issue and for the same did not pass the test case.
