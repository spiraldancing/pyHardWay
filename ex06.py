#!/usr/bin/env python3

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

not_funny = False
funny = True
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % not_funny)
print(joke_evaluation % funny)

not_funny = funny
print(joke_evaluation % not_funny)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
