#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                   #QUIZ GAME START----
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random

print("__Welcome! in Quiz Game__".center(180))

name=input("Your Name:")

print("Thankyou! Dear", name)

print("="*98)

print("\n__Choose Your Quiz Type__\n\n".center(100))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                  #TYPES OF QUIZ QUSTIONS:--
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
type={
    1:"Python Programming\n",
    
      2:"General Knowledge\n",
    
      3:"Web Developement\n",
    
      4:"Human Body\n"
      }
for key,value in type.items():
    
    print(key,":",value.center(80))
    
print("\n"+"-"*200)

n=int(input("\n\nYour Choise-: ".center(180)))
#=====================================================================================================

                                                       #PYTHON PROGRAMMING QUIZ QUESTIONS:

#=====================================================================================================
if (n==1):
    
    print("\n\n--PYTHON  PROGRAMMING--\n\n".center(180))
    
    Python_Programming_quiz=[
        {
            "Question": "\nWho created Python ?\n",
            
            "options": ["a) Guido van Rossum\n",
                        "b) Dennis Ritchie\n",
                        "c) Bjarne Stroustrup\n",
                        "d) Mark Zuckerberg\n"],
            "answer":"a"},
        
        {
            "Question": "\n\nFunction बनाने के लिए कौन-सा keyword use होता है?\n",
            
            "options": ["a) func\n",
                    "b) function\n",
                    "c) def\n",
                    "d) define\n"],
            "answer": "c"},
         
        {
            "Question": "\n\nNumpy का full form क्या है?\n",
            
            "options": ["a) Numerical Python\n", "b) Number Python\n", "c) Numeric Python\n", "d) None\n"],
            "answer": "a"},
        
        {
            "Question": "\n\nlist एक mutable data structure है?\n",
            
            "options": ["a) True\n", "b) False\n"],
            "answer": "a"},
       
        {
            "Question": "\n\nPython is a plateform independent programming language:\n ",
            
            "options": ["a) True\n", "b) False\n"],
            "answer": "a"}
        
        ]
    score=0
    random.shuffle(Python_Programming_quiz)
    for quiz in Python_Programming_quiz:
        print("\n"+quiz["Question"].center(80))
        for option in quiz["options"]:
            print(option.center(180))
        user_ans=input("Enter Your Answer(a/b/c/d):").lower()
        if(user_ans==quiz["answer"]):
            print("\nRight")
            score+=1
            print("="*98)
        else:
            print("\n\nWrong")
    print("\nQuiz Completed")
    print("Your Score =",score,"/",len(Python_Programming_quiz))
    print("="*98)
#=====================================================================================================
    
                                                          #GENERAL KNOWLEDGE QYUIZ---
    
#=====================================================================================================
    
elif (n==2):
    print("\n\n--GENERAL  KNOWLEDGE--\n\n".center(100))
    gk_questions=[
    {
        "question": "\n\nWhat is the capital of India?\n",
        
        "options": ["a) Mumbai\n", "b) Delhi\n", "c) Bangalore\n", "d) Kolkata\n"],
        "answer": "b",
        
    },
    {
        "question": "\n\n भारत में कुल कितने राज्य हैं?\n",
        
        "options": ["a) 26\n", "b) 28\n", "c) 29\n", "d) 30\n"],
        "answer": "b",
        
    },
     {
        "question": "\n\nविश्व का सबसे बड़ा महासागर कौन सा है?\n",
        
        "options": ["a) Atlantic\n", "b) Indian\n", "c) Pacific\n", "d) Arctic\n"],
        "answer": "c",
        
    },
    {
        "question": "\n\nमहात्मा गांधी भारत के राष्ट्रपिता hai?\n",
        
        "options": ["a) True\n", "b) False\n"],
        "answer": "a",
        
        
    },
    {
        "question": "\n\n एशिया विश्व का सबसे बड़ा महाद्वीप है?\n",
        
        "options": ["a) True\n", "b) False\n"],
        "answer": "a",
        
    }]
    score=0
    random.shuffle(gk_questions)
    for quiz in gk_questions:
        print("\n"+quiz["question"])
        for option in quiz["options"]:
            print(option.center(180))
        user_ans=input("Enter Your Answer(a/b/c/d):").lower()
        if(user_ans==quiz["answer"]):
            print("Right")
            score+=1
            print("="*99)
        else:
            print("Wrong")
    print("\nQuiz Completed")
    print("Your Score =",score,"/",len(gk_questions))
    print("="*98)

    
#=====================================================================================================

                                                                          #WEB  DEVELOPEMENT---
    
#=====================================================================================================
    
elif (n==3):
    print("--WEB DEVELOPEMENT--".center(180))
    web_quiz = [
    {
        "question": "\n\nWhat does HTML stand for?\n",
        
        "options": ["a)Hyper Text Markup Language\n",
                    "b)High Text Machine Language\n",
                    "c)Hyper Transfer Markup Language\n",
                    "d)Home Tool Markup Language\n"],
        "answer": "a"
        
    },

    {
        "question": "\n\nWhich language is used to create the structure of a web page?\n",
        
        "options": ["a)Python\n",
                    "b)HTML\n",
                    "c)Java\n",
                    "d)C++\n"],
        "answer": "b"
        
    },

    {
        "question": "\n\nWhat does CSS stand for?\n",
        
        "options": ["a)Computer Style Sheets\n",
                    "b)Creative Style Sheets\n",
                    "c)Cascading Style Sheets\n",
                    "d)Colorful Style Sheets\n"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhich language is used to style web pages?\n",
        
        "options": ["a)HTML\n",
                    "b)CSS\n",
                    "c)Python\n",
                    "d)SQL\n"],
        "answer": "b"
        
    },

    {
        "question": "\n\nWhat is the primary purpose of JavaScript?\n",
        
        "options": ["a)Database Management\n",
                    "b)Styling Web Pages\n",
                    "c)Adding Interactivity\n",
                    "d)Server Management\n"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhich HTML tag is used to create a paragraph?\n",
        
        "options": ["a) <p>\n",
                    "b) <h1>\n",
                    "c) <div>\n",
                    "d) <br>\n"],
        "answer": "a"
        
    },

    {
        "question": "\n\nWhich HTML tag is used for a line break?\n",
        
        "options": ["a) <p>\n",
                    "b) <br>\n",
                    "c) <hr>\n",
                    "d) <lb>\n"],
        "answer": "b"
        
    },

    {
        "question": "\n\nWhich CSS property is used to change the background color of an element?\n",
        
        "options": ["a) color\n",
                    "b) background-color\n",
                    "c) font-size\n",
                    "d) border\n"],
        "answer": "b"
        
    },

    {
        "question": "\n\nWhat is the file extension for a JavaScript file?\n",
        
        "options": ["a) .html\n",
                    "b).css\\ n",
                    "c) .js\n",
                    "d) .py\n"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhich technologies are commonly used in Frontend Web Development?\n",
        
        "options": ["a) HTML, CSS, JavaScript\n",
                    "b) Python, SQL\n",
                    "c) Java, C++\n",
                    "d) PHP, MySQL\n"],
        "answer": "a"
        
    }]
    score=0
    random.shuffle(web_quiz)
    for quiz in web_quiz:
        print("\n"+quiz["question"].center(180))
        for option in quiz["options"]:
            print(option.center(180))
        user_ans=input("Enter Your Answer(a/b/c/d):").lower()
        if(user_ans==quiz["answer"]):
            print("Right")
            score+=1
            print("="*98)
        else:
            print("Wrong")
    print("\nQuiz Completed".center(180))
    print("Your Score =",score,"/",len(web_quiz))
    print("="*98)
#=====================================================================================================

                                                                                  #HUMAN  BODY  QUIZ ---
    
#=====================================================================================================
    
elif(n==4):
    print("__HUMAN  BODY__".center(180))
    body_quiz = [
    {
        "question": "\n\nWhich organ pumps blood throughout the body?\n",
        
        "options": ["a)Lungs", "b)Heart", "c)Liver", "d)Kidney"],
        "answer": "b"
        
    },

    {
        "question": "\n\nHow many bones are there in an adult human body?\n",
        
        "options": ["a)206", "b)186", "c)226", "d)246"],
        "answer": "a"
        
    },

    {
        "question": "\n\nWhich organ is responsible for breathing?\n",
        
        "options": ["a)Heart", "b)Brain", "c)Lungs", "d)Liver"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhich part of the body controls all activities?\n",
        
        "options": ["a)Heart", "b)Brain", "c)Kidney", "d)Stomach"],
        "answer": "b"
        
    },

    {
        "question": "\n\nWhat is the largest organ in the human body?\n",
        
        "options": ["a)Liver", "b)Brain", "c)Skin", "d)Lungs"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhich blood cells help fight infections?\n",
        
        "options": ["a)Red Blood Cells", "b)White Blood Cells", "c)Platelets", "d)Plasma"],
        "answer": "b"
        
    },

    {
        "question": "\n\nWhich organ helps digest food?\n",
        
        "options": ["a)Stomach", "b)Heart", "c)Lungs", "d)Brain"],
        "answer": "a"
       
    },

    {
        "question": "\n\nHow many chambers does the human heart have?\n",
        
        "options": ["a)2", "b)3", "c)4", "d)5"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhich part of the body contains the femur bone?\n",
        
        "options": ["a)Arm",
                    "b)Neck",
                    "c)Leg",
                    "d)Hand"],
        "answer": "c"
        
    },

    {
        "question": "\n\nWhat is the main function of the kidneys?\n",
        
        "options": ["a)Pump Blood",
                    "b)Filter Waste from Blood",
                    "c)Digest Food",
                    "d)Control Thoughts"],
        "answer": "b"
        
    }]
    score=0
    random.shuffle(body_quiz)
    for quiz in body_quiz :
        print("\n"+quiz["question"].center(180))
        for option in quiz["options"]:
            print(option.center(180))
        user_ans=input("Enter Your Answer(a/b/c/d):").lower()
        if(user_ans==quiz["answer"]):
            print("Right")
            score+=1
            print("="*99)
        else:
            print("Wrong")
    print("\nQuiz Completed".center(180))
    print("Your Score =",score,"/",len(body_quiz))
    print("="*98)
#======================================================================================================    
else:
    print("Invalid Choise")


                                                                                                    #CODE ENDED:--
                                                                                                                                    #written by: Archita Yadav..

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
