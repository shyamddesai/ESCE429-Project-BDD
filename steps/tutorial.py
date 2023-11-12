# steps/calculator_steps.py
from behave import given, then, when


@given('the calculator is turned on')
def step_calculator_turned_on(context):
    # For simplicity, let's just initialize a calculator object
    context.calculator = Calculator()


@when('I add {num1:d} and {num2:d}')
def step_add_numbers(context, num1, num2):
    context.result = context.calculator.add(num1, num2)


@then('the result should be {expected_result:d}')
def step_check_result(context, expected_result):
    assert context.result == expected_result, f"Actual result: {context.result}, Expected result: {expected_result}"


class Calculator:
    def add(self, num1, num2):
        return num1 + num2
