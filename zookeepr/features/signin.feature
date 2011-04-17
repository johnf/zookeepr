Feature: Sign In
  In order to go to the conferene
  As an attendee
  I need an acccount

  Scenario: Try to sign in a non-existent user
    When I go to "http://localhost:5000/person/signin"
    And I fill in "Email address:" with "johnf@inodes.org"
    And I fill in "Password:" with "moocow"
    And I press "Sign in"
    Then I should see "Your sign-in details are incorrect"
