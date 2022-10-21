print("\nHello!")
print("Welcome to the Zombie Apocalypse Survival predictor.")
print("Please answer the following questions and based off your answers, I will predict how long you will last in a zombie apocalypse")


control = True

while control:
    print("\nQuestion: Do you live in a big city/subarban area? Yes / No / Define big / Exit")
    

    var1_bigcity = input()

    #YOU DO LIVE IN A BIG CITY
    if var1_bigcity == "Yes":
        control = False

        print("Question: How old are you?")
        var2_age = int(input("Please enter your age: "))

        #Young in a big city 
        #3 different outcomes depending on if you have a big dog, small dog or no dog
        if (var2_age <= 15): 
            print("\n========================================================================")
            print("\nOof, that's pretty young to be on your own in the big city.")
            var_dog = (input("\nDo you have a big dog that can protect you? Yes / No / I have a small dog, will that do? "))

            if(var_dog == "Yes"):
                print("\n========================================================================")
                print("\nWell at least that is something")
                print("SURVIVAL PREDICTION: You'll survive as long as the dog does")
            
            elif(var_dog == "No"):
                print("\n ==================================================================")
                print("\nWell that is unfortunate. It's not looking good for you champ!")
                print("SURVIVAL PREDICTION: Eaten by a zombie within 2 weeks!!!")
            
            else:
                print("\n ==================================================================")
                print("\nSmall dogs are an inconvience even in the normal world.")
                print("You and your weak dog stand no chance.")
                print("SURVIVAL PREDICTION: You and your dog will make a nice snack for a zombie within a week!!! ")
            
    
        #Mature in a big city
        #Perform multiplication to determine how many days you'll survive
        elif (var2_age < 60): 
            
            print("\nOn a scale from 1-10, please answer the following questions:")

            a = int(input("How athletic are you? "))
            b = int(input("How resourceful are you? "))
            c = int(input("How capable are you of wielding an axe? "))

            print("\n========================================================================")
            print("\nBased on your answers I predict you will last the following number of days in the big city: ")
            print(a*b*c)
            
        #Old in a big city
        #Just one outcome
        else:
            print("\n ==================================================================")
            print("\nYour dodgy knees and achy joints will betray you. \nShould have retired to the countryside sooner.")
            print("\nSURVIVAL PREDICTION: Fatal fall when running away from a zombie swarm. Dead within a week ! ")

    #YOU DON'T LIVE IN A BIG CITY
    elif var1_bigcity == "No":
        control = False
        
        print("Question: How old are you?")
        var3_age = int(input("Please enter your age: "))


        #Young in the countryside
        #Just one outcome
        if (var3_age <= 15):
            print("\n ==================================================================")
            print("\nAlone in the countryside isn't ideal for a child. You'll get bored. You'll get hungry. You'll go wandering into the city in search of action.")
            print("\nSURVIVAL PREDICTION: Boredom will kick in after 2 weeks!")
            print("Curiosity will indeed kill the cat when you go searching for action in the city.")
            print("(If it wasn't clear, you're the cat, and a zombie is the curiosity)")

        #Mature in countryside
        #Just one outcome
        elif (var3_age < 60):
            print("\n ==================================================================")
            print("\nYouthful and isolated! You hit the jackpot")
            print("\nSURVIVAL PREDICTION: Enjoy a long and prosperous life :)")


        #Old in the countryside
        else: 
            print("\n ==================================================================")
            print("\nRetiring to the countryside has its benefits")
            print("\nSURVIVAL PREDICTION: You might not get eaten by zombies, but no doctors, medicine and TV Bingo might see you to an earlier grave than wanted.")
            print("I predict 5 more years of an enjoyable peaceful life :)")

    elif var1_bigcity == "Exit":
        control = False
        print("Thank You")

    #Define what a big city is
    else:
        print("\n ==================================================================")
        print("\nA big city has a population of 50,000+ people within walking distance of one another \n \n")