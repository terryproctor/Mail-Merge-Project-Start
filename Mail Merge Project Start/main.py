#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names=[]
with open(r"Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    for name in  names_file.readlines():
        names.append(name.strip().replace("\n", ""))

for name in names:
    with open(r"Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter_start:
        letter_contents = letter_start.read().replace("[name]", name)
        with open(r"Mail Merge Project Start\Output\ReadyToSend\letter_" + name + ".txt", "w") as letter_name:
            letter_name.write(letter_contents) 