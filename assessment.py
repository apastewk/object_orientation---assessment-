"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    Encapsulation: Encapsulation is data being bundled together into one which
                   prevents data from being accidentally changed.

    Abstraction: Don't really care how something works, just that it does, so we
                 can hide information from the user to reduce complexity 

    Polymorphism: Easy to create interchangeable components. Objects have the 
                  capacity to take on different forms when accessed by the same
                  method.  
                  
2. What is a class?
    
    A class lets you structure your program in a particular way.  It is the act 
    of a 'thing'.  The thing can be a list, file, string, etc. 

3. What is an instance attribute?

    Instance attributes are attributes that are directly related (unique) to an
    object.   

4. What is a method?

    A method is similar to a function and is associated with instances and 
    classes.  A method will always have at least one parameter, 'self'.

5. What is an instance in object orientation?

    An instance is a particular list, string, file, etc.  It is an individual
    instance of a class.  

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute owned by a class.  They are shared by all 
   instances if an instance attribute is not specified but the attribute is not 
   unique to them, it belongs to the parent class.  Instance attributes are 
   unique to each instance, it's like having a post-it note with an attribute on  
   it directly placed on the instance.   

"""


# Parts 2 through 5:
# Create your classes and class methods


# Part 2/3

class Student(object):
    """Stores student information."""

    def __init__(self, first_name, last_name, address):
        """Initialize an instance of Student class."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address 


class Question(object):
    """Stores questions and their correct answer."""
    
    def __init__(self, question, correct_answer):
        """Initialize an instance of Question class."""

        self.question = question 
        self.correct_answer = correct_answer 

    def ask_and_evaluate(self):
        """Prompts the user to answer the question and returns True or False."""

        user_answer = raw_input(self.question)
        if user_answer == self.answer.lower():
            print "That is correct!"
            return True 
        else:
            print "Sorry, that is incorrect."
            return False 


class Exam(object):
    """Stores information to create the actual exam."""

    def __init__(self, name):
        """Initialize an instance of Exam class."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Makes a question and adds to the exam's list of questions."""

        question_instance = Question(question, correct_answer)
        self.questions.append(question_instance)

    def administer(self):
        """Administer exam with all questions."""

        score = 0

        for question_instance in self.questions:
            instance_answer = question_instance.ask_and_evaluate()
            if instance_answer == True:
                score += 1
        
        return score 



# Part 4

def take_test(exam, student):
    """Administers the exam and assigns the score."""

    score = exam.administer 
    student.score = score

def example():
    """Creates and administers an exam."""

    example_exam = Exam("Oscars Exam")

    example_exam.add_question("What movie won Best Picture in 2016? ", "Spotlight")
    example_exam.add_question("Who won Best Actor in 2014? ", "Matthew McConaughey")
    example_exam.add_question("Who won Best Support Actress in 2015? ", "Patricia Arquette")

    example_student = Student("Maggie", "Cameron", "1514 Pupple Ave.")

    example_student.score = example_exam.administer()

    print example_student.score



# Part 5

class Quiz(Exam):
    """Quizzes are pass/fail grading."""

    def administer(self):

        score = super(Quiz, self).administer()

        passing_mark = len(questions) / 2
        if score > passing_mark:
            print "You passed!"
            return True

        print "You failed!"
        return False





