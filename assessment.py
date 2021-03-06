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


class Student(object):
    """Class with first names, last names and addresses"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Exam(object):
    """Class with names and lists of questions"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        single_question = Question(question, correct_answer)
        self.questions.append(single_question)

    def administer(self):
        score = 0
        for question in self.questions:
            if Question.ask_and_evaluate(question) is True:
                score += 1
        return float(score)/float(len(self.questions))


class Quiz(Exam):
    """Class inheriting from exam, which modifies one method to return a boolean value instead of a float"""

    def administer(self):
        passing_score = len(self.questions)/2
        current_score = 0
        for question in self.questions:
            if Question.ask_and_evaluate(question) is True:
                current_score += 1
        if current_score >= passing_score:
            return True
        else:
            return False


class Question(object):
    """Class with questions and correct answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        self.user_guess = raw_input(self.question + "  ")
        if self.user_guess == self.correct_answer:
            return True
        else:
            return False


def take_test(exam_instance, student_instance):
    student_score = Exam.administer(exam_instance)
    print "You scored %s" % student_score
    student_instance.score = student_score


def example():
    sample_exam = Exam('sample exam')
    sample_exam.add_question('What is the method for adding an element to a set?', 'add()')
    sample_exam.add_question('What is the method for adding an element to a list?', 'append()')
    sample_exam.add_question('What is the method for adding an element to a touple?', 'not possible')
    sample_student = Student('Sue', 'Johnson', '601 Bay Street')
    take_test(sample_exam, sample_student)

example()
