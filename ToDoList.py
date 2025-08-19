import time


tasks = [["Add a task!", 0]]

def showList():
    print("\nCurrent tasks: ")
    for i in range(len(tasks)):
        if tasks[i][1] == 1:
            print(f"{tasks[i][0]} -- ✅")
        if tasks[i][1] == 0:
            print(f"{tasks[i][0]} -- ⏱️")

# this stores each acceptable command and each for it can take
# used later to translate e.g. 'a' into 'add'.
cmds = {
    "add":["add","a"],
    "remove":["remove","rem","r"],
    "complete":["complete","comp","c"],
    "incomplete":["incomplete","inc","i"],
    "show":["show","s","disp"]
}

"""

add ITEM
remove ITEM_INDEX
complete ITEM_INDEX
incomplete ITEM_INDEX

"""


def concatenate(string):
    raw = []
    clean = string.split(" ")
    for word in clean:
        raw.append(word.strip(" [],\"'"))
    newString = "".join(raw)
    return newString

def updateList(command):

    """
    split command by word into an array:
    command will be: ["1st word", "2nd word", "3rd word", etc]
    """
    command = command.split(" ")
    content = ""

    """
    loop through the array of command contents, skipping the main command 
    and pushing everything else to 'content' variable
    """
    for i in range(1, len(command)):
        content += command[i]
        content += " "

    """
    Now that the parameters passed to the command are stored in :content: variable,
    we can set command to hold only the initial command
    """
    command = command[0].lower()


    #make a condensed version of content for analysis
    newContent = concatenate(content)
    newTask = []
    for i in range(len(tasks)):
        newTask.append(concatenate(str(tasks[i][0])))


    """
    Here we check the main command and use the passed parameter accordingly
    """
    if command in cmds["add"]:
        tasks.append([content, 0])
    elif command in cmds["remove"]:
        del tasks[int(content)-1]
    elif command in cmds["complete"]:
        tasks[int(content)-1][1] = 1
    elif command in cmds["incomplete"]:
        tasks[int(content)-1][1] = 0
    else:
        print("Invalid command")

print("\n########## ########## ########## ########## ##########")
disp = "#"
while True:

    showList()



    userCommand = input(f"\nTo-Do List -- #")

    updateList(userCommand)
