# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)

####
#### YOUR CODE HERE 
####
x=0
with open("romeo_and_juliet.txt", "r") as f:
    text=f.read()
    play=text.lower()
    number = play.count("juliet")
    print(number)



# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 
####

