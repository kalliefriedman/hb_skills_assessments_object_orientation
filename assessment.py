"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   -Encapsulation: Data lives close to its functionality, which becomes particularly useful when building larger programs
   -Abstraction: We only need to understand what a method does in order to use it, and allows us to disociate this from how the method does it
   -Polymorphism: Allows us to make different interchangable types of an object (interchangabability of components)

2. What is a class?
    -A class is a container which allows a coder to group functions and data and place them inside, accessible with the . operator.

3. What is an instance attribute?
    -An instance attribute is specific data which can be stored which is applicable to only that particular intstance of an object.


4. What is a method?
    -A method is a function which can be called on a particular class, store inside that class's container.

5. What is an instance in object orientation?
    -A member of a given class that has specified values rather than variables

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    -The difference is that the attribute on the class is shared by all instances. The attribute on an instance is unique to that instance.
    -An example would be for a class of cakes. All cakes might share texture (class attributes), but ingredients, color, shape, etc. would vary between different instances of cake (instance attributes)

"""


# Parts 2 through 5:
# Create your classes and class methods

Part 2: Classes and Init Methods

Directions: Make Python classes that could store each of the following three pieces of data. Use the dictionaries below as examples to guide you in creating class definitions for the following objects. Define an __init__ method to allow callers of this class to provide initial values for each attribute.

class Student(object):
    """A member of class with first names, last names and addresses"""

Students can have first and last names and addresses. Here are two example students. Write a class that can store data such as this:

{'first_name': 'Jasmine',
 'last_name': 'Debugger',
 'address': '0101 Computer Street'}

{'first_name': 'Jaqui',
 'last_name': 'Console',
 'address': '888 Binary Ave'}
Question

Questions include a question and a correct answer. Here are two example questions. Write a class that can store data such as this:

{'question': 'What is the capital of Alberta?',
 'correct_answer': 'Edmonton'}

{'question': 'Who is the author of Python?',
 'correct_answer': 'Guido Van Rossum'}
Exam

Notice that an Exam should have an attribute called questions. Simply initialize the questions attribute as an empty list in the body __init__ function. We’ll deal with adding questions to the exam later on in this assignment. Your __init__ function should take a name for the exam as a parameter.

A Note on Attributes
Though we’ve mainly seen attributes that are strings or integers, remember: attributes can also be lists and many other data types. In the case of our questions attribute, we’ll have a list of Question objects.

For example, here are two exams. Make a class that could store data like this:

{'name':'Midterm',
 'questions': [

    {'question':'What is the capital of Alberta?',
     'correct_answer': 'Edmonton'},

    {'question': 'Who is the author of Python?',
     'correct_answer': 'Guido Van Rossum' }

  ]
}

{'name':'Final',
 'questions': [

    {'question':"Who is Ubermelon's competition?",
     'correct_answer': 'Sqysh'},

    {'question': "What is Balloonicorn's favorite color?",
     'correct_answer': 'Sparkles'}

  ]
}
Part 3: Methods

Add a method to the Exam class which takes a question and a correct_answer as parameters, makes a Question from those, and adds it to the exam’s list of questions.

For example

$ python -i assessment.py
>>> exam = Exam('midterm')
>>> exam.add_question(
...     'What is the method for adding an element to a set?',
...     '.add()')
Add a method to the Question class that prints the question to the console and prompts the user for an answer. It should return True or False depending on whether the correct answer matches the user’s answer.

For example

$ python -i assessment.py
>>> question = Question(
...     'What is the method for adding an element to a set?',
...     '.add()')
>>> question.ask_and_evaluate()
What is the method for adding an element to a set? > .add()
True
Add a method to the Exam class which administers all of the exam’s questions, and returns the user’s score (as a decimal percentage) at the end.

So, building on our code from problem 2, here’s how the Exam class should work.

$ python -i assessment.py
>>> exam = Exam('midterm')
>>> exam.add_question(
...     'What is the method for adding an element to a set?',
...     '.add()')
>>> exam.administer()
What is the method for adding an element to a set? > .add()
1.0
Hint
Here’s some pseudocode for the administer method.

Inside the Exam.administer method, you’ll need to first initialize a variable called score; set it to zero.

Next, loop through each of the questions in the exam.

For each question, call the question’s method from Problem #2 — ask_and_evaluate.

If the return value of ask_and_evaluate is True, increment the score.

After the last question has been administered, calculate and return the percentage score.

Part 4: Create an actual exam!

Create functions, not methods!
Part 4 doesn’t require you to modify the class definitions you’ve created in the previous 3 parts of this assignment. Simply use the classes you’ve defined.

Write a function, take_test, that takes an Exam and a Student as parameters, administers the exam, and assigns the score to the student instance as a new attribute called score. This function should also print a message to the screen indicating the score.
Write a function, example, which does the following:
Creates an exam
Adds a few questions to the exam
These should be part of the function; no need to prompt the user for questions.
Creates a student
Administers the test for that student using the take test function you just wrote
Part 5: Inheritance

A “quiz” is like an exam — it’s a set of questions that students are prompted to answer. However, whereas exams are given a raw score (or more conveniently, a percentage score), quizzes are pass/fail: if you answered at least half of the questions correctly, you pass the quiz. When you call the administer method on a quiz, it should only return True if you passed or False if you failed.

Think about how we could solve this requirement: we have an Exam class and we want to have a Quiz class that is similar.

Write code to solve this problem. Incorporate as many of the “design” parts of the class lectures as you feel comfortable with.
