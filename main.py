print("----> QUIZ GAME <----")


# Questions - 
questions = ["What does CPU stands for? ","What is GPU? ","What is RAM in PC? ","What is fastest storage hardware in PC? ","What is HDD stands for? ","Name the portable device in PC pheriperials? "]
answers = ['center processing unit','graphics processing unit','random access memory','SSD','hard disk drive','pen drive']


# Functions -
def checkAns(ans,actualAns):
    if(ans == actualAns):
        print("Great...")
        return '1'
    else:
        print('wrong!')
        return 0


def isplaying():
    playing = input("Wanna play my game? (y,n): ")
    if(playing is 'n'):
        print("Good Bye! Have a Nice Day.")
        quit()


# MAIN 
if __name__ == '__main__':    
    isplaying()
    print("Ok...Lets Move")

    score = 0
    for i in range(len(questions)):
        ans1 = input(questions[i])
        correctAns = checkAns(ans1, answers[i])
        if(correctAns=='1'):
            score+=1

    print(f"You have score {score} out of {len(answers)}.")