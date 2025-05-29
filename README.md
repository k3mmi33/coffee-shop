
# Coffee Shop Domain Model

## Overview

This project models a Coffee Shop domain using object-oriented programming principles in Python. It includes three main entities: `Customer`, `Coffee`, and `Order`, with relationships and methods to manage orders and customers.

## Setup and Installation

1. Create a virtual environment and install dependencies using pipenv:

   ```bash
   pipenv install
   pipenv shell
   pipenv install pytest
   ```

2. Run tests with pytest:

   ```bash
   pytest
   ```

## Project Structure

- `customer.py`: Defines the `Customer` class.
- `coffee.py`: Defines the `Coffee` class.
- `order.py`: Defines the `Order` class.
- `debug.py`: Script for interactive testing of the classes.
- `tests/`: Directory containing pytest test files for each class.

## Usage

Run `debug.py` to see example usage and relationships:

```bash
python debug.py
```

## Features

- Validations on input data for all classes.
- Methods to create and manage orders.
- Aggregate methods like average price and number of orders.
- Class method to find the customer who spent the most on a specific coffee.
- Comprehensive tests using pytest.

## Author

Created as part of a coding assessment.