import os

directoryPath = os.path.dirname(os.path.realpath(__file__))
print("What would you like to do?")
choice = input("1.Write file to save locally. \n 2.Write file to save in database. \n 3. Edit file. \n")
print(choice)
if choice == '1':
    print("You are storing files locally")
    answer = input("Would you like to store it in " + directoryPath + "?")

    if answer.lower() in ['n', 'no']:
        path = input("Please enter path in which to store file: ")
        while not os.path.exists(path):
            print("Path does not exist")
            path = input("Please enter path in which to store file: ")
        os.chdir(path)
        print(os.getcwd())

    title = input("What would you like to name the file? ")+".txt"
    while os.path.isfile('./'+title):
        print("That file alrady exists.")
        title = input("What would you like to name the file? ")+".txt"
    file = open(title,'w');
    noteInfo = input("you may now write your notes. Enter '0' to close file.")
    while not noteInfo == '0':
        file.write(noteInfo +'\n')
        noteInfo = input("")
    file.close()
elif choice == '2':
    print("You are storing files in the database")
elif choice == '3':
    path = input("Please enter path in which the file is stored: ")
    while not os.path.exists(path):
        print("Path does not exist")
        path = input("Please enter path in which to store file: ")
    os.chdir(path)
    editName = input("What is the name of the file to edit? ")
    while not os.path.isfile('./'+editName +".txt"):
        print("That file doesn't exist in the current folder.")
        editName = input("What is the name of the file to edit?")
    with open(editName +".txt",'a') as file:
        noteInfo =input("you may now write your notes. Enter '0' to close file.")
        file.write('\n')
        while not noteInfo == '0':
            file.write(noteInfo +'\n')
            noteInfo = input("")
        file.close()
