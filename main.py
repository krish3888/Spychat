from spy_detail import spy , Spy, ChatMessage  #importing from spy_detail.py file
from steganography.steganography import Steganography
from datetime import datetime
import csv
from colorama import Fore

old_status = ['\"galti,badi galti,engineering\"' , '\"attitude toh bachpan se hai jab paida huaa toh 2 saal mene kisi se baat nhi krri\"' , '\"papa ki pari\"' , '\"sleeping\"', '\"busy\"' , '\"Mujse baat mt krna mai apna bna leta hu\"']

def login():
    username=raw_input("enter username")
    password=raw_input("enter password")
    with open("login.csv", "rb") as login:  # opening login.csv file
        reader = csv.reader(login)  # Reading from file
        for row in reader:
            row = list(reader)  # typecasting to list
            c = 0  # counter
            for k in range(0, len(row)):  # travelling the list
                name = row[k][0]
                pswd = row[k][1]
                sal = row[k][2]
                age = row[k][3]
                rating = row[k][4]
                if name == username:  # checking for correct username
                    if password == pswd:  # checking for correct password
                        spyname = sal + " " + name
                        print 'Welcome !! ' + spyname + ". Your age is " + str(age) + ' and your rating is ' + str(rating)
                        spy_chat(spyname, age, rating)  # calling spy_chats
                        break
                    else:
                        c = 1  # if username is not correct c=1
                else:
                    c = 2  # if password is not correct c=2
                k = k + 1
        if c == 1:     # checking for counter's value
            print "Invalid username"
        elif c == 2:
            print "Invalid password"

friends = []  # List to loading friends
messages = []  # List to loading chats

def load_chats():
    with open('chats.csv') as chats_data:  # opening chats.csv file
        reader = list(csv.reader(chats_data))  # making this as a list
        for row in reader[1:]:  # traversal in the file content
            chat = Chats(time=row[0], sender=row[1], message=row[2], receiver=row[3])
            messages.append(chat)  # Appending the chats in  the list messages
load_chats()# loading chats

def load_frnd():
    with open('friends.csv', 'rb') as friend_data:
        reader =list(csv.reader(friend_data))
        for row in reader[1:]:
            spy = Spy(name=row[0], salutation=row[1], rating=(row[2]), age=row[3])
            friends.append(spy)
load_frnd()# loading Friends


def all_friends():  # function to show list of friends
    serial_no = 1  # counter to print serial numbers
    for frnd in friends:  # printing list of friends
        print str(serial_no) + ". " + frnd.name
        serial_no = serial_no + 1

def add_status(c_status):
    if c_status != None:
        print "Your current status is" + c_status
    else:
        print "You don't have any status currently "
    existing_status = raw_input("\nwant to select from old status? Y/N \n")
    if existing_status.upper() == "N":
        new_status = raw_input("enter your status: ")
        if len(new_status)>0:
            updated_status = new_status
            old_status.append(updated_status) #adding the new status in the status list
        else:
            print "enter a valid status"
    elif existing_status.upper() == "Y":
        serial_no = 1
        for status in old_status :  #printing old status
            print str(serial_no) + "-) " + status
            serial_no = serial_no + 1
        status_choice = input("enter your choice: ")
        updated_status = old_status[ status_choice-1 ]   #updating the status
    return updated_status

def add_friend():
    frnd = Spy('','',0,0.0)
    frnd.name = raw_input("enter the friend name: ")
    frnd.sal = raw_input("salutaion? Mr. or Ms.")
    frnd.age = input("friend age? ")
    frnd.rating = input("friend rating? ")
    frnd.is_online = True
    if len(frnd.name)>0 and 65>spy.age>16 and frnd.rating>spy.rating :
        with open('friends.csv', 'ab') as friend_data:
            writer = csv.writer(friend_data)
            writer.writerow([frnd.name, frnd.sal, frnd.rating, frnd.age, frnd.is_online])
            print "congrats...Now you have one more frirnd"
    else:
        print "friend cannot be added"
    return len(friends)

def select_frnd(): #function to select friend
    all_friends()
    print "Select your friend"
    user_selected_frnd = input("enter your choice: ")  #select friend
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index

def send_message():
    selected_friend = select_frnd()
    receiver = friends[selected_friend].name
    original_image = raw_input("what is the name of original image? ") #here take it as .PNG
    output_path = "secret.jpg"   #name of image
    secret_text = raw_input("what is your secret message? ")
    Steganography.encode(original_image,output_path,secret_text)
    print "message encoded"
    special_msg = ["EMERGENCY","selfish","SOS","BUSY" "SAVE ME","HELP","BE AWARE"]  # list of special messages
    message = secret_text.upper()
    sp = message.split(" ")  # spliting the message
    for word in sp:  # checking for special messages in our secret_text
        for i in special_msg:
            if word.upper() == i:
                print Fore.RED + "You have send  an emergence message \n"  # Printing message in red color
                print Fore.BLACK
    time = datetime.now()  # storing the current time
    with open('chats.csv', 'ab') as chats:  # opening file to append chats
        writer = csv.writer(chats)
        writer.writerow([time, spy, secret_text, receiver])  # writing chats to file
    print "Your secret message is ready"

def read_message():
    selected_friend = select_frnd()  # calling select_friend function
    output_path = raw_input("Which image you want to decode? ")  # the name of image to be decoded
    secret_text = Steganography.decode(output_path)  # calling decode()function to decode
    print "The decoded message is " + secret_text  # printing the secret text

def chat_history():  # function to print chat history
    selected_friend = select_frnd()  # calling select friend
    choice = friends[selected_friend].name
    for i in messages:  # checking for receiver's chats in the list
        if choice == i.receiver:
            print Fore.BLUE + "Time: " + i.time  # printing time in blue color
            print Fore.RED + "Receiver: " + i.receiver  # printing receiver in red color
            print Fore.BLACK + "Message: " + i.msg  # printing message in black color

def spy_chat(name,age,rating):  #start_chat function
    current_status = None
    choice= -1
    print "Here are your options " + spy.name.upper()
    while choice!=0: #implementing of loop
        choice = input("\n *What do you want to do?\n  0-Exit \n  1-add the status \n  2-add the friend  \n 3-All friend\n 4-send a secret message \n  5-read a personal message \n  6-read chat history\n 7-Logout\n ") #Displaying Menu
        #use of nested loop
        if choice == 0:
            print "exit"
        elif choice == 1:
            current_status = add_status(current_status)
            print "Updated status is -\n" + current_status
        elif choice == 2:
            friend_no=1
            no_of_frnd = add_friend()
            print "\nyou have " + str(no_of_frnd) + " friends"

        elif choice == 3:
            all_friends()
        elif choice == 4:
            send_message()
        elif choice == 5:
            read_message()
        elif choice==6:
            print chat_history()  # calling chat_history function
        elif choice == 7:  # logout option
            reply = raw_input("Are you sure you want to logout Y/N?? ")
            if reply.upper() == "Y":
                print Fore.MAGENTA + "You are logged out....\n"  # printing message of logout in magenta color
                print Fore.BLACK
                break
        elif choice == 0:  # exit
            print 'Exit'
        else:
            print " **Oooopss invalid input."


def signup():
    spy = Spy("", "", 0, 0.0)  # class for spydetails
    spy.name = raw_input('Enter your username: ')  # take name as input from user
    if spy.name.isspace():  # to check for space input
        print 'Enter a valid name '
    elif spy.name.isdigit():  # to check for digit input
        print 'Enter a valid name '
    elif len(spy.name) > 2:  # checking for length of the string name
        password=raw_input("Enter your password: ")
        print 'Welcome ' + spy.name + ' ' + 'glad to have you back with us.'  # concatenating strings
        spy.sal = raw_input('What should we call you (Mr.or Ms.): ')
        if spy.sal.upper() == 'MR.' or spy.sal.upper() == 'MS.':  # using if condition
            spy.name = spy.sal+" "+spy.name.upper()  #Using + for string concatenation
            print spy.name  #home work
            print "Alright "+spy.name+".I'd like to know a little bit more about you before we proceed...."  #home work
            spy.age = 0  #variable declaration ,integer type
            spy.rating = 0.0  #variable declaration for float number
            spy.age = input("What is your age?")
            if 65 > spy.age > 16:  # and operator is also a solution of this
                print "CONGRATS...You are eligible for spy."
            else:
                spy.rating = input("What is your rating?")
                if spy.rating >= 8.0:
                    print "GREAT SPY (*****)."  #5 star
                elif 8 > spy.rating > 5.0: #elif used for mare than one condition
                    print "GOOD SPY (***)"  #3 star
                elif 3.5 < spy.rating <= 5.0:
                    print "AVERAGE SPY.YOU CAN ALWAYS DO BETTER (*)." #1 star
                else:
                    print "WHO HIRED YOU?"
                spy_is_online = True #this is boolean
                print "Authentication complete.Welcome %s your age " \
                          "is" + str(spy.age) + "and rating is"+ str(spy.rating) + ".Proud to have " \
                          "you on board." #we can also use placeholders
                with open("login.csv", "ab")as login:     ## writing details in login file
                    writer = csv.writer(login)
                    writer.writerow([spy.name, password, spy.sal, spy.age, spy.rating, spy_is_online])

                spy_chat(spy.name, spy.age , spy.rating )

        else:
           print "Please check salutation."
    else:
        print "Ooopss please enter a valid name."

def welcome():
    f = datetime.now()  # calling function now() from datetime library
    print f.strftime("%b %d %Y %H:%M:%S")  # use of string time format
    print 'Hello...!! Welcome to SPYCHAT.'  # printing hello
    print 'Let\'s get started'
    spy_reply = raw_input('Are you a new user? Y/N ')  # asking the user if he is a new user or not
    if spy_reply.upper() == 'N':
        login()
    elif spy_reply.upper() == 'Y':
        signup()
    else:
        print "Invalid input"
welcome()
