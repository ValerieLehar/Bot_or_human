# Valerie Lehar
# 261205467 
#Short program to identify if a response is from a human or a bot

print("Is the person your chatting to a bot or a human? \
Let's find out together!")
bot = "You just talked to a bot"
human = "You just talked to a fellow human"

#Availability test
time = float(input("What time did you recive your response \
(type a float based on the 24 hours system)"))
if 2 <= time <= 5: #Humans need sleep therfore these are unavailable hours
    print(bot)

#Response time test
else: 
    minute = float(input("How long did it take to get your \
response? (Please answer in minutes)"))
    if minute < 0.15: #to fast of a response time for a human
        print(bot)

#speed typing test  
    else: 
        words = int(input("What is the number of words in the \
message you recieved?"))
        words_per_minute = words/minute
        if words_per_minute < 66: #Average typing speed slower than 66 
            print(human)
       
#Typo test       
        else: 
            typos = int(input("How many typos are in the response\
 you recieved? (grammatical errors, spelling mistakes, etc.)"))
            if typos > 0: #computers make no typos therfore >0 is proof of human
                print(human)
            
#Wang et al test            
            else: 
                wang_test = int(input("Ask the responder how many 't' \
there are in 'eeooeotetto' and type their answer?"))
                if wang_test == 3:
                    print(human)
                else:
                    print(bot)