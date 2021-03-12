Feature: NameGame

  @smoke_test
  Scenario: Sign In
    Given User is on "Home" page.
    And the user chooses a random person. If the chosen person is "correct", the user is moved to next screen to choose "next person", and the "tries", "correct" & "streak" increases. Else if the chosen person is "incorrect", the "tries" increases & "streak" sets to "zero" and the user has to choose again.


