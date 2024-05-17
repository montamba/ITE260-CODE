import time

def MAT152():
    ques = ("#1.What is simple interest ?",
     "#2.How do you calculate simple interest?",
     "#3.What is maturity value?",
      "#4.How do you calculate the compound interest?",
      "#5.Can compound interest make you rich?")
    choi = (("A)An interest is calculated on the principal or original, amount of loan", "B)An interest can almost calculate everything", "C)An interest can show a correlation to the variable", "D)An interest can make five digits"),
    ("A)Multiply by itself", "B)Multiply the principal amount by the interest rate and time", "C)Multiply the variable", "D)Multiply the principal interest"),
    ("A)The maturity value is the amount due and payable to the holder of an financial obligation", "B) the maturity value contains a large amount of an value", "C) maturity value can hold a bigger amount of storage", "D) maturity value contains a bigger wages to hold"),
    ("A)Multiplying its variable in order to compete","B)Multiplying its correlation","C)Multiplying the initial amount by one plus by the annual interest rate raised to the number of compound periods minus 1","D)Multiplying its compound to its amount of due"),
    ("A)Yes","B)No not at all","C)None","D)None of the above"))
    ans = ("A", "B", "A", "C","A")
    return ques, choi, ans
    
def ITE260():
    q = ("#1. What language designed by Guido Van Rossum?","#2.HTML stands for?",'#3.What is for loop?',"#4. What is a list?","#5. What is a algorithm?")
    c=(("A.HTML","B)Python","C.CSS","D.Kali Linux"),
    ("A. Hyper Text Makeup Language","B. Hyper Tax Marking Language","C. Hyper Text Markup Language","D. Hyper Tax Markup Language"),
    ("A. It is used to iterate over a sequence, which could be a list, tuple, array, or str","B. It is used to iretate over an sequence of the list","C. It is used to literate an sequence to ang array",
    "D.It is used to obliterate a sequence in order to make a list"),
     ("A. a sequence of several variables, grouped together under a single name",
"B. a sequence of several various of numbers that grouped together under a single name",
"C. a sequence of several variables that grouped together under a double name",
"D. a sequence of several variables that grouped together and stays in brackets"),
("A. a procedure used for solving a problem or performing a computation",
"B. a procedure used for listing elements",
"C. a procedure used for delete a one variable",
"D. a procedure cannot be program if you debug a program"))  
    a = ("B","C","A","A","A")
    return q, c ,a

highest = []    
    
def game():
    guess = []
    score = 0
    index = 0
    
    try:

        player = int(input("enter a game\n1.Mat152\n2.ITE260\nchoose a number only: "))
        if player == 1:
            question, choices, answer = MAT152()
        elif player == 2:
            question, choices, answer = ITE260()
        else:
            print("Invalid")
            game()
    except:
        print("number only")
        game()
    for q in question:
        print("----------------------------------")
        print(q)
        for c in choices[index]:
            print(c)
        user = str(input("Letters only: ")).upper()
        
        guess.append(user)
        
        if user == answer[index]:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            
        index += 1

    print("------Correction-------")
        
    n = 0    
    for g in guess:
        if g == answer[n]:
            print(f"{g} Correct!")
        else: 
            print(f"{g} Incorrect! {answer[n]}")
               
        n += 1

    out = len(guess)
    
    highest.append(score)
        
    print(f"your score:{score}/{out}")
    print("highest: ", max(highest))
    
    play = str(input("Do you want to continue?(Y/N)? " )).upper()
    
    if play == "Y" or play == "YES":
        time.sleep(2)
        print("RESTARTING.....")
        game()
    elif play == "N" or play == "NO":
        print("DO YOU WANT TO LOGIN OR QUIT?")
    
users={} 
 
def signup():
    user = input("Username: ")
    pas = input("Password: ")
    time.sleep(1)
    print("Make sure that you remember your password!")
    print("Finish!")
    users[user] = pas
    
def login():
    user=input("ENTER YOUR NAME: ")
    pas=input("ENTER YOUR PASSWORD: ")
    time.sleep(1)
    print("CHECKING...........")
    time.sleep(2)
    if user in users and users[user]==pas:
        print("SUCCESS!")
        time.sleep(2)
        game()
    else:
        print("NOT MATCHED!")
        
     
print("=====================================\n==|                               |==\n==|   QUIZ FOR BSIT FRESHMEN!     |==\n==|                               |==\n======================================")
time.sleep(2)
print("Loading.......")

time.sleep(3)

while True:
    try:
        user= int(input("1.SIGNIN?\n2.LOGIN?\n3.VIEW ACC\n4.QUIT\nNumber only: "))
        if user == 1:
            time.sleep(2)
            signup()
        elif user == 2:
            time.sleep(2)
            login() 
        elif user == 3:
            print("**********************")
            pppp=0
            if len(users) == 0:
                print("No Users yet")
            else:
                for ser in users:
                    pppp += 1
                    print(pppp,ser)
            print("**********************")   
            
        elif user == 4:
            print("THANK YOU FOR PLAYING!") 
            break
              
        else:
            print("ERROR!")
    except:
        print("Number only")