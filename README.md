# AlgorithmsAndDataStructures

This is a folder where that I will use as a container for files containing data structures and algorithms. The purpose is to be used by myself as a reference for other, more complex projects. Another purpose is to demonstrate my skills as a propgrammer when it comes to these two highly important topics in computer science.

## Python

### Finite State Machine Symbol Tokenizer

> A finite-state machine (FSM) or finite-state automaton (FSA, plural: automata), finite automaton, or simply a state machine, is a mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one state to another in response to some inputs; the change from one state to another is called a transition.[1] An FSM is defined by a list of its states, its initial state, and the inputs that trigger each transition. Finite-state machines are of two types—deterministic finite-state machines and non-deterministic finite-state machines.[2] A deterministic finite-state machine can be constructed equivalent to any non-deterministic one.

- [wikipedia](https://en.wikipedia.org/wiki/Finite-state_machine)

This finite state machine is designed to parse tokens from a programming language, as part of the design of a compiler. In other words, this file is one used to create a compiler.

Upon request I can share a private repository of a Finite State Machine Tokenizer, or FSM Tokenizer. I cannot display it in this repository because this repository is public and the FSM Tokenizer that I made was my solution to my final project in my college class Algorithms. Because of that, the professor asked us to _not_ publically share the code, to prevent plagiarism from other or future students. However, that was my final project for the class and I would like to show it off because I worked really hard on it, so if you are interested please contact me!

### Fibonacci Sequence

fibo(n) returns the fibonacci sequence of an integer, n.

The following are test cases of fibo(n):

> fibo(0) == 0
>
> fibo(1) == 1
>
> fibo(2) == 1
>
> fibo(3) == 2
>
> fibo(4) == 3
>
> fibo(5) == 5
>
> fibo(10) == 55

### Greatest Common Divisor using Euclid's Algorithm

My solution for a project involving finding an algorithm to find the greatest common divisor that has the fastest running time. That is we were tasked to find several definitions for a gcd function and to measure the running times of each. We found that the fastest gcd implementation uses euclid's algorithm. The running time for Euclid's Algorithm is O(n) as we learned in class.

### Find Duplicate and Find First Duplicate

My solution for one of the problems in Leetcode, Find duplicate which finds all of the duplicates in a given list. Find first duplicate finds the first duplicate in a list.

### Join(L) and Join(l,s)

My solution for the Leetcode problem join, which is defined as a function that takes in a List of characters and returns another string of all the characters joined together by spaces. So for example, join(["j", "o", "i", "n"]) would return "j o i n".

Similarily, join(["j", "o", "i", "n"], "\*") would return "j\*o\*i\*n"

### Military Time Converter

This is a Python function that simply converts a string that is formatted in standard time to military time.

### Maze

This is a function along with its helper functions that finds the shortest path to travel in a maze, which is represented in the form of a 2-dimensional list of positions, where the positions are tuples of integers ie, (0,0), (0, 10), (1, 1) and a maze is in the form of:

> [[(0, 0), (0, 1)] , [(1, 0), (1, 1)]]

Thus we can imagine that the maze it represents would graphicall look like this where the dots are the actual positions and the numbers are labels indicating their indeces in the maze's 2D list representation:

> 0 1
> 0 . .
> 1 . .

### Python Notes

This is a file I made to give myself notes on the Python programming language as a reference.

### Radius to Area

These are functions that calculate the following geometric formulas:

radiusToArea: finds a circle's area given its radius

baseAndHeightToArea: finds a triangle's area given its height and base length

lAndWtoArea: finds a rectangle's area given its length and width

### One Away
This is a problem that I have to credit the author from the book"Cracking the Code Interview" by Gayle Laakman McDowell, however the solution is all mine and it has passed every test case descirbed in the book's problem statement.
> "There are three types of edits that can be performed on strings: insert a character, remove a character,
> or replace a character. Given two strings write a function to see if they are one edit awy from being the same character." - Gayle Laakman McDowell

Test cases and their result in my implementation:
> pale, ple -> True
> pales, pale -> True
> pales, bale -> True
> pale, bake -> False

## Java

## Javascript

## C
