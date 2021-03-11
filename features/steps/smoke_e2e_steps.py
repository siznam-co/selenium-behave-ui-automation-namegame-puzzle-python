import time

from behave import *
from pageobjects.NameGame import NameGame


@given('User is on "{home}" Page.')
def step_impl(context, home):
    var = NameGame(context).go_to(home)
    assert var, "The user is not navigated to " + home + " screen."


@step(
    'the user chooses a random person. If the chosen person is "correct", the user is moved to next screen to choose '
    '"next person", and the "tries", "correct" & "streak" increases. Else if the chosen person is "incorrect", '
    'the "tries" increases & "streak" sets to "zero" and the user has to choose again.')
def step_impl(context):
    NameGame(context).click_random_person()