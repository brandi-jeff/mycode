#!/usr/bin/env python3

import html
import time

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():

    correct= html.unescape(trivia["correct_answer"])
    incorrect1= html.unescape(trivia["incorrect_answers"][0])
    incorrect2= html.unescape(trivia["incorrect_answers"][1])
    incorrect3= html.unescape(trivia["incorrect_answers"][2])
   
    print(trivia["question"])
    time.sleep(1)
   
    print(f"A. {incorrect1}\nB. {correct}\nC. {incorrect2}\nD. {incorrect3}")
    answer = input("Please choose the correct answer: ")

    if answer.capitalize() == "B":
        print("You are correct!")
    else: 
        print("Sorry. The correct answer was B.")


if __name__ == "__main__":
    main()
