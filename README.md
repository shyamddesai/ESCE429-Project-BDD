# TodoBDD: BDD Testing Framework for TodoManager API
TodoBDD is a behavior-driven testing (BDD) framework designed to validate the functionality of the TodoManager API. It uses scenario-based tests to ensure consistent behavior across API features, allowing easy integration of new scenarios and comprehensive test coverage.

## Features
- **Scenario-Based Testing**: Covers multiple scenarios for each API endpoint to ensure reliable behavior.
- **Automated Setup and Teardown**: Database reset between scenarios to maintain test independence.
- **Readable Test Syntax**: Written in Gherkin, making tests easy to understand and maintain.

## Setup
Install `behave` to enable BDD testing with Gherkin syntax:
```bash
pip install behave
```

## How to Run
To execute all tests, navigate to the root folder of the project and use:
```bash
behave
```

This command will run all scenarios defined in the `features` directory, providing a detailed report of each test's success or failure.
The database is reset before each scenario using `before_scenario()` in `environment.py` to allow scenarios to run independently and in any order.

## Directory Structure
- `features/`: Contains all `.feature` files defining scenarios for each API endpoint.
- `environment.py`: Configures setup and teardown for database management across scenarios.
- `steps/`: Includes step definitions implementing each scenario in Python.
