from behave import *


@given(u'User is on Registration page')
def step_impl(context):
    context.driver.get("https://thetestingworld.com/testings")
    # context.driver.find_element('xpath', '//input[@type=radio and @id=tab2]').click()


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element('name', 'fld_username').send_keys('abcd')
    # context.driver.find_element('name', '_txtUserName').send_keys('Rutuja')


@when(u'User enters email ID')
def step_impl(context):
    context.driver.find_element('name', 'fld_email').send_keys('abcd@gmail.com')


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element('name', 'fld_password').send_keys('abcd')
    # context.driver.find_element('name', '_txtPassword').send_keys('rutu')


@when(u'User clicks on Submit button')
def step_impl(context):
    context.driver.find_element('xpath', '//input[@type="submit" and @value="Sign up"]').click()


@then(u'User should get registered successfully')
def step_impl(context):
    print("registration Successful")


@when(u'User enters duplicate username')
def step_impl(context):
    context.driver.find_element('name', 'fld_username').send_keys('abcd')


@then(u'User should not get registered successfully')
def step_impl(context):
    print("Registration failed")
