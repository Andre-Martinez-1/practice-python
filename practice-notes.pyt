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

Study Guide: Week 2 Graded Quiz
It is time to prepare for the Week 2 graded quiz. Please review the following items from this week before starting the Week 2 Graded Quiz. If you would like to refresh your memory on these materials, please revisit the Study Guides located before each Practice Quiz in Week 2 : 
Study Guide: Expressions and Variables
, 
Study Guide: Functions
, and 
Study Guide: Conditionals
.  

Knowledge  
How to assign values to variables and use them in code

How to construct a function and use function parameters

How comparison and logical operators can be used, 

How comparison and logical operators behave with different data types

What type of results simple and complex comparisons produce

How to alphabetize strings using comparison operators

What must appear after the if and elif keywords

What the elif keyword does 

When an if,  elif, or else-statement will execute

How to use the floor division //  and modulo % operators and why

How to use logical operators with comparison operators to develop complex conditional statements within an if-elif-else block

Best practices for coding and their benefits

What “self-documenting code” means


There may be a few questions on the quiz that will ask you about either the output of a small block of code or the value of part of the code. Make sure to read the instructions carefully on those questions.

Anatomy of a While Loop
A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.  

Common Pitfalls With Variable Initialization
You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable without first initializing it, you'll run into a NameError. This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.

Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to initialize your variables before using them!

Infinite loops and Code Blocks
Another easy mistake that can happen when using loops is introducing an infinite loop. An infinite loop means the code block in the loop will continue to execute and never stop. This can happen when the condition being evaluated in a while loop doesn't change. Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.

In the Coursera code blocks, you may see an error message that reads "Evaluation took more than 5 seconds to complete." This means that the code encountered an infinite loop, and it timed out after 5 seconds. You should take a closer look at the code and variables to spot where the infinite loop is.

while Loops
A while loop executes the body of the loop while a specified condition remains True. They are commonly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.

Common Errors in while Loops
If you get an error message on a loop or it appears to hang, your debugging checklist should include the following checks:

Failure to initialize variables. Make sure all the variables used in the loop’s condition are initialized before the loop.

Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables. You can often prevent an infinite loop by using the break keyword or by adding end criteria to the condition part of the while loop.

 

while Loop Terms
while loop - Tells the computer to execute a set of instructions while a specified condition is True. In other words, while loops keep executing the same group of instructions until the condition becomes False.

infinite loop - Missing a method for exiting the loop, causing the loop to run forever.

break - A keyword that can be used to end a loop at a specific point. 

 

Math Concepts on the Practice Quiz
The coding problems on the upcoming practice quiz will involve a few math concepts. Don’t worry if you are rusty on math. You will have plenty of support with these concepts on the quiz. The following is a quick overview of the math terms you will encounter on the quiz:  

prime numbers - Integers that have only two factors, which are the number itself multiplied by 1. The lowest prime number is 2.

prime factors - Prime numbers that are factors of an integer. For example, the prime numbers 2 and 5 are the prime factors of the number 10 (2x5=10). The prime factors of an integer will not produce a remainder when used to divide that integer. 

divisor - A number (denominator) that is used to divide another number (numerator). For example, if the number 10 is divided by 5, the number 5 is the divisor.

sum of all divisors of a number - The result of adding all of the divisors of a number together.  

multiplication table - An integer multiplied by a series of numbers and their results formatted as a table or a list. For example:

                 4x1=4
                 4x2=8
                 4x3=12
                 4x4=16
                 4x5=20

                 For loops allow you to iterate over a sequence of values. Let's take the example from the beginning of the video:


FOR LOOPS                 
for x in range(5):

  print(x)

Similar to if statements and while loops, for loops begin with the keyword for with a colon at the end of the line. Just like in function definitions, while loops and if statements, the body of the for loop begins on the next line and is indented to the right. But what about the stuff in between the for keyword and the colon? In our example, we’re using the range() function to create a sequence of numbers that our for loop can iterate over. In this case, our variable x points to the current element in the sequence as the for loop iterates over the sequence of numbers. Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value. So range(5) will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.

Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4. Our for loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable x and the code within our loop body will execute for each iteration through the sequence. So for the first loop, x will contain 0, the next loop, 1, and so on until it reaches 4. Once the end of the sequence comes up, the loop will exit and the code will continue.

The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use for loops to iterate over a list of strings, such as usernames or lines in a file.

Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed. A for loop works well when you want to iterate over a sequence of elements.  

A Closer Look at the Range() Function
The in keyword, when used with the range() function, generates a sequence of integer numbers, which can be used with a for loop to control the start point, the end point, and the incremental values of the loop.  

Syntax:

123
for n in range(x, y, z):
    print(n)

The range() function uses a set of indices that point to integer values, which start at the number 0. The numeric values 0, 1, 2, 3, 4 correlate to ordinal index positions 1st, 2nd, 3rd, 4th, 5th. So, when a range call to the 5th index position is made using range(5) the index is pointing to the numeric value of 4.

Index Number

1st index

2nd index

3rd index

4th index

5th index

Value

0

1

2

3

4

The range() function can take up to three parameters:  range(start, stop, step) 

Start 
The first item in the range() function parameters is the starting position of the range. The default is the first index position, which points to the numeric value 0. This value is included in the range. 

Stop
The second item in the range() function parameters is the ending position of the range. There is no default index position, so this index number must be given to the range() parameters. For example, the line for n in range(4) will loop 4 times with the n variable starting at 0 and looping 4 index positions: 0, 1, 2, 3. As you can see, range(4) (meaning index position 4) ends at the numeric value 3. In Python, this structure may be phrased as “the end-of-range value is excluded from the range.” In order to include the value 4 in  range(4), the syntax can be written as range(4+1) or range(5). Both of these ranges will produce the numeric values 0, 1, 2, 3, 4. 

Step
The third item in the range() function parameters is the incremental step value. The default increment is +1. The default value can be overridden with any valid increment. However, note that the loop will still end at the end-of-range index position, regardless of the incremental value. For example, if you have a loop with the range: for n in range(1, 5, 6), the range will only produce the numeric value 1. This is because the incremental value of 6 exceeded the ending point of the range.

Key takeaways
The roles of the range(start, stop, step) function parameters are:

Start - Beginning of range

value included in range

default = 0

Stop - End of range

value excluded from range (to include, use stop+1)

no default

must provide the ending index number 

Step - Incremental value 

default = 1


'''