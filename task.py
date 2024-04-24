from behave import *
from selenium import webdriver

@given('I am on the Demo Login Page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.saucedemo.com/")

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def step_impl(context):
    username_field = context.browser.find_element_by_id('user-name')
    password_field = context.browser.find_element_by_id('password')
    login_button = context.browser.find_element_by_id('login-button')
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

# Implement other step definitions similarly

@then('I verify the App Logo exists')
def step_impl(context):
    assert context.browser.find_element_by_xpath('//img[@class="app_logo"]').is_displayed()

@step('I verify the Error Message contains the text "{text}"')
def step_impl(context, text):
    error_message = context.browser.find_element_by_xpath('//h3').text
    assert text in error_message

@step('I am on the inventory page')
def step_impl(context):
    # Implementation
    pass

# Implement other step definitions similarly

@step('I verify in Checkout overview page if the total amount for the added item is ${amount}')
def step_impl(context, amount):
    # Implementation
    pass

@step('Then Thank You header is shown in Checkout Complete page')
def step_impl(context):
    # Implementation
    pass


@step("I click the Login Button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click the Login Button')


@then("I am redirected to the Demo Main Page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I am redirected to the Demo Main Page')


@when("I fill the account information for account LockedOutUser into the Username field and the Password field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: When I fill the account information for account LockedOutUser into the Username field and the Password field')


@when("user sorts products from low price to high price")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user sorts products from low price to high price')


@step("user adds lowest priced product")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user adds lowest priced product')


@step("user clicks on cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user clicks on cart')


@step("user clicks on checkout")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user clicks on checkout')


@step("user enters first name John")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user enters first name John')


@step("user enters last name Doe")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user enters last name Doe')


@step("user enters zip code 123")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user enters zip code 123')


@step("user clicks Continue button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user clicks Continue button')


@then("I verify in Checkout overview page if the total amount for the added item is $8.63")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I verify in Checkout overview page if the total amount for the added item is $8.63')


@then("I verify in Checkout overview page if the total amount for the added item is $8.63")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I verify in Checkout overview page if the total amount for the added item is $8.63')


@when("user clicks Finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user clicks Finish button')


@then("I verify in Checkout overview page if the total amount for the added item is $8.63")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I verify in Checkout overview page if the total amount for the added item is $8.63')


@then("Thank You header is shown in Checkout Complete page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Thank You header is shown in Checkout Complete page')


@then("I verify in Checkout overview page if the total amount for the added item is $8.63")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I verify in Checkout overview page if the total amount for the added item is $8.63')


@then("I verify in Checkout overview page if the total amount for the added item is $8.63")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then I verify in Checkout overview page if the total amount for the added item is $8.63')
