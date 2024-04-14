# Cipher X

A simple encryption method that you can use to write messages only you and your friends can read!

## encrypt.py

Contains all functions to encrypt a message

## plugboard

Swaps one character with another character
Input: "String", "lk, aj, lx" (first letter is letter in starting text, second letter is the final letter after plugboard)
Identifier: #

## horizontalRotor

Rotates all characters a set amount in the list
Input: "String", "integer" (positive for rotate right, negative for rotate left)
Identifier: $

## verticalRotor

Adds or subtracts from the decimal ASCII values of each character
Input: "String", "integer" (positive to add, negative to subtracts)
Includes intelligent rollover so no special characters get added
Identifier: %

[List of ASCII Values](https://miro.medium.com/v2/resize:fit:1400/1*rFEwJIMzpHHTb-MpoiLCAw.jpeg)
