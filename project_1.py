#function
def level_fun(a,q):
    try:
        a = int(a)
    except:
        print("You have entered something unexpectable. Try starting with 'beginer' and proceed th the upper levels if needed")
        a=0
    if type(a) is int:
        level=a
    while level == a :
        name = str(a) + ".txt"
        try:
            file = open(name, encoding = 'utf-8')
        except:
            print("You have entered something unexpectable. Try starting with 'beginer' and proceed th the upper levels if needed")
            a = 0
        print(q[a])
        exp = input("yes/no: ")
        if exp == 'yes':
            if a in [0,1]:
                print("You are experiensed enough to proceed to the next level")
                confirmation = input("Press 'Enter' button to level up or 'stay' to see current level content")
                if confirmation == "stay":
                    print(file.read())
                    break
                else:
                    a+=1
                    name = str(a) + ".txt"
                    file = open(name, encoding = 'utf-8')
                    print(file.read())
            elif a==2:
                print(file.read())
        elif exp == "no":
            if a in [0,1]:
                print(file.read())
            elif a==2:
                print("Then I recomend you seeing previous level content")
                file = open("1.txt", encoding = 'utf-8')
                for line in file:
                    print(line)
        else:
            continue
        break
    file.close()
def abbr_fun(a):
    for line in a_file:
        line = line.strip()
        if line.lower().startswith(a.lower()+" "):
            return(line)
    a_file.close()
question=('Do you know basic stitches?','Do you know basic paterns, like "Magic ring"? ', 'For these patterns you need to know how to crochet "Magic ring". Do you?')
print("Welcome to 'start crochet' programe, happy to see you here!")
print("Crochay levels: \n beginer(0), \n basic(1), \n intermediate(2)")
# asking for user's input
level = input("Select your crochay level (just print a number from the brackets)")
level_fun(level,question)
while True:
    abbr = input("\nTo see abbreviations explanation enter abbreviation(like 'ch')\nif you don't need any explanation just press Enter: ")
    a_file=open("abbr.txt",  encoding = 'utf-8')
    if abbr=="":
        print("Hope it was helpful for you to start crocheting. Good luck in your future crochet projests!")
        break
    else:
        print(abbr_fun(abbr))


  
