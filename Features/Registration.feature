Feature: Verifying Registration functionality

    @smoke
    Scenario: Registration with Valid Data
      Given  User is on Registration page
      When   User enters username
      And    User enters email ID
      And    User enters password
      And    User clicks on Submit button
      Then   User should get registered successfully

    @sanity @smoke
    Scenario: Registration with Duplicate username Data
      Given  User is on Registration page
      When   User enters duplicate username
      And    User enters email ID
      And    User enters password
      And    User clicks on Submit button
      Then   User should not get registered successfully