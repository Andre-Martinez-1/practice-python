#Programming code - Programming code is a set of written computer instructions, guided by rules, using a computer programming language. It might help to think of the computer instructions as a detailed, step-by-step recipe for performing tasks. The instructions tell computers and machines how to perform an action. Programming code may also be referred to as source code or scripts.
'''
Programming languages - Programming languages are similar to human spoken languages in that they both use syntax and semantics. Programming languages are used to write computer programs.  Some common programming languages include Python, Java, C, C++, C#, and R.

Syntax - Syntax is a set of rules for how statements are constructed in both human and computer languages. Programming syntax includes rules for the order of elements in programming instructions, as well as the use of special characters and their placements in statements. This concept is similar to the syntax rules for grammar and punctuation in human language.

Semantics - Semantics refers to the intended meaning or effect of statements, or collections of words, in both human and computer languages. Semantic errors are also referred to as logical errors.

Computer program - A computer program is a step-by-step list of instructions that a computer follows to reach an intended goal. It is important to be clear and precise about the actions a computer program is supposed to perform because computers will do exactly what they are instructed to do. Computer programs can be long, complex, and accomplish a variety of tasks. They are often developed by computer programmers and software engineers, but anyone can learn to create them. Computer programs may involve a structured development cycle. They can be written in a wide variety of programming languages, such as Python, Java, C++,  R, and more. The completed format of a program is often a single executable file.

Script - Scripts are usually shorter and less complex than computer programs. Scripts are often used to automate specific tasks. However, they can be used for complex tasks if needed. Scripts are often written by IT professionals, but anyone can learn to write scripts. Scripts have a shorter, less structured development cycle as compared to the development of complex computer programs and software. Scripts can be written in a variety of programming languages, like Python, Javascript, Ruby, Bash, and more. Some scripting languages are interpreted languages and are only compatible with certain platforms.

Automation - Automation is used to replace a repetitive manual step with one that happens automatically. 

Output - Output is the end result of a task performed by a function or computer program. Output can include a single value, a report, entries into a database, and more. 

Input - Input is information that is provided to a program by the end user. Input can be text, voice, images, biometrics, and more.   

Functions - A function is a reusable block of code that performs a specific task.

Variables - Variables are used to temporarily store changeable values in programming code. 

expression - a combination of numbers, symbols, or other values that produce a result when evaluated

data types - classes of data (e.g., string, int, float, Boolean, etc.), which include the properties and behaviors of instances of the data type (variables)

variable - an instance of a data type class, represented by a unique name within the code, that stores changeable values of the specific data type

implicit conversion - when the Python interpreter automatically converts one data type to another

explicit conversion - when code is written to manually convert one data type to another using a data type conversion function:

str() - converts a value (often numeric) to a string data type

int() - converts a value (usually a float) to an integer data type

float() - converts a value (usually an integer) to a float data type

We looked at a few examples of built-in functions in Python, but being able to define your own functions is incredibly powerful. We start a function definition with the def keyword, followed by the name we want to give our function. After the name, we have the parameters, also called arguments, for the function enclosed in parentheses. A function can have no parameters, or it can have multiple parameters. Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters. Lastly, we put a colon at the end of the line.

After the colon, the function body starts. It’s important to note that in Python the function body is delimited by indentation. This means that all code indented to the right following a function definition is part of the function body. The first line that’s no longer indented is the boundary of the function body. It’s up to you how many spaces you use when indenting -- just make sure to be consistent. So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.


In the Functions segment, you learned how to define and call functions, utilize a function’s parameters, and return data from a function. You also learned how to differentiate and convert between different data types utilizing variables. Plus, you learned a few best practices for writing reusable and readable code. 

Terms
return value - the value or variable returned as the end result of a function

parameter (argument) -  a value passed into a function for use within the function

refactoring code - a process to restructure code without changing functionality

Knowledge
The purpose of the def() keyword is to define a new function. 

Best practices for writing code that is readable and reusable:

Create a reusable function - Replace duplicate code with one reusable function to make the code easier to read and repurpose.

Refactor code - Update code so that it is self-documenting and the intent of the code is clear.

Add comments - Adding comments is part of creating self-documenting code. Using comments allows you to leave notes to yourself and/or other programmers to make the purpose of the code clear.

Comparison Operators with Equations
The following examples demonstrate how to use comparison operators with the data types int (integers, whole numbers) and float (number with a decimal point or fractional value). Comparison operators return Boolean results. As you learned previously, Boolean is a data type that can hold only one of two values: True or False.  

The comparison operators include: 

==    (equality) 

!=     (not equal to) 

>       (greater than)

<      (less than)

>=    (greater than or equal to)

<=    (less than or equal to)


PART 1: Equality == and Not Equal To != Operators
In Python, you can use comparison operators to compare values. When a comparison is made, Python returns a Boolean result: True or False. Note that Boolean data types are not string data types (Boolean True is not equal to the string "True").  

To check if two values are the same, use the equality operator: == 

To check if two values are not the same, use the not equal to operator: != 

We just covered the if statement, which executes code if an evaluation is true and skips the code if it’s false. But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement. The else statement follows an if block, and is composed of the keyword else followed by a colon. The body of the else statement is indented to the right, and will be executed if the above if statement doesn’t execute.

We also touched on the modulo operator, which is represented by the percent sign: %. This operator performs integer division, but only returns the remainder of this division operation. If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%5 would return 0, as there is no remainder.

Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!

Study Guide: Conditionals
This study guide provides a quick-reference summary of what you learned in this lesson and serves as a guide for the upcoming practice quiz.  

In the Conditionals segment, you learned about the built-in Python operators used for comparing values and the logical operators for making complex comparisons. You also learned how to use operators in if-else-elif blocks. 

 

Knowledge
Comparison operators with numerical values
Comparison expressions return a Boolean result (True or False). 

x == y        If x is equal to y, return True. Else, return False.

x != y         If x is not equal to y, return True. Else, return False.

x < y          If x is less than y, return True. Else, return False.

x <= y        If x is less than or equal to y, return True. Else, return False.

x > y          If x is greater than y, return True. Else, return False.

x >= y        If x is greater or equal to y, return True. Else, return False.

Comparison operators with strings
Comparison expressions with strings also return a Boolean result (True or False).

"x" == "y"  If the words are the same, return True. Else, return False.

"x" != "y"   If the words are not the same, return True. Else, return False.

When used with strings, the following comparison expressions will alphabetize the strings.

"x" < "y"   	If string "x"  has a smaller Unicode value than string "y", return True.  Else, return False.

"x" <= "y" 	If the Unicode value for string "x" is smaller than or equal to the Unicode value of string "y", return True. Else, return False.

"x" > "y"    	If string "x" has a larger Unicode value than string "y", return True. Else, return False.

"x" >= "y"  	If the Unicode value for string "x" is greater than or equal to the Unicode value of string "y", return True. Else, return False.

Logical operators
Logical operators are used to combine comparison expressions and also return Boolean results (True or False).

comparison1 and comparison2 

Returns a True result if both comparison1 and comparison2 are true. 

If they are not both true, return False.

comparison1 or comparison2 

Returns a True result if either comparison1 and/or comparison2 are True. 

If neither comparison is true, return False.

not comparison1

Returns the inverse Boolean value of the comparison. 

Returns a True result if comparison1 is false. 

If comparison1 is true, then returns False.



'''