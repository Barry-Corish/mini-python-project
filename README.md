# mini-python-project

# I set out to create a basic program which would provide an estimation on how long one would survive in a zombie apocalypse.

# I wanted to include a loop, iterations, conditionals and inputs which required both strings and numerical values. 

# Firstly, I printed a string which acts as a friendly introduction. This was very easy to do. 

# The first question to be asked is "Do you live in a big city?" 
# There are 4 possible answers available to this question - Yes, No, Define a "Big" city, and Exit
# If a user answered yes or no, they would be brought forward in the program and asked more questions. 
# If a user wanted the definition of a "big" city, I wanted a message to print out which provided the definition, but then I wanted the question to be immediately asked again, prompting the user to input Yes or No. 
# To complete this, I implemented a 'while loop', setting the answers "Yes" and "No" as a False control. Thus if a user answered "Yes" or "No", they exited the loop and proceeded to be asked the next appropriate question. 
# The definition of a big city was set as the True control. Thus if initiated, the user would remain in the loop and be stuck there until answering the question with a "Yes" or "No". 
# One does not have to type out the full sentence of "Define big" in order to initiate this True control. They simply just have to enter anything other than "Yes" or "No". 
# If a user answers "Exit", the program will be exited. 

# Whether you answered or no to the "big city" question, you will then be asked to input your age. 
# The final outputs, of which there is 8, will be decided by a combination of your age, your city, and in 2 special streams, there will be more questions asked. 

# There are 3 possible age brackets which I defined using the < & > operators. 
# I crudely defined <= 15 as being 'too' young. 
# >15, <60 is defined as being mature. Or the 'ideal age' in this context. 
# >= 60 is defined as being too old. 

# If answered Yes to living in a big city you are directed to input your age. 
# In general, living in a big city in a zombie apocalypse is deemed to be more dangerous than not living in a big city (i.e the countryside). Therefore all the final outputs from answering 'Yes' to the big city question will be more fatal than answering 'No'. 

# I had finished all of the code when I had spare time so I decided to make this stream of answers slightly more complex than the other stream. I did this by asking more questions depending on the age bracket. 

# If you inputted an age <15, you are asked if you have a big dog, no dog, or small dog. 
# By inputting one of the 3 given answers, you will receieve a final corresponding output giving you a prediction on how long you will survive and how you might die in the zombie apocalypse. 

# If you inputted an integer in the range of 15-60, you are asked for 3 more inputs. 
# These inputs are all integers and relating to questions about how athletic you are (denoted by: a), how resourceful you are (denoted by: b), and how capable you are of wielding an axe (denoted by: c). 
# I wanted to utilise some sort of mathematical computation in my program, and this seemed to be an appropriate way to do so. 
# The final output for this stream of "lives in big city and is mature" is given by a prediction of how many days you will survive. 
# This prediction is complicated by multiplying the 3 prior inputs : a*b*c. 

# All of the remaining streams were more basic as I was running out of time. 
# They amounted to just being based off a combination of whether you live in a big city or not, and your age bracket. 
# So the fate of the four following streams was based off of this: 
# Old and Living in a big city. 
# Young and not living in a big city. 
# Mature and not living in a big city. 
# Old and not living in a big city. 

# With more time, I would like to make these streams more complex. 
# I liked the idea of creating an exact prediction based off of numerical inputs. So I would have liked to create a more mathematical algorithm which would have incorporated more inputs, and used this to create a 'days remaining' prediction. 

# My program meets the requirements. 
# Upon launching the program you are presented with a menu with 3 core options. (Do you live in a big city? 1. Yes,  2. No,  3. Define Big)
# This menu also offers the oppurtunity to exit the program. 

# Building off of this, more menus are presented with more options. By completing the questions, the user will exit the program.