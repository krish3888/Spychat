from spy_detail import spy , Spy , ChatMessage  #importing from spy_detail.py file
from steganography.steganography import Steganography
from datetime import datetime

def add_status(c_status):
    if c_status != None:
        print "Your current status is" + c_status
    else:
        print "You don't have any status currently "
    existing_status = raw_input("\n you want to select from old status? Y/N \n")
    if existing_status.upper() == "N":
        new_status = raw_input("enter your status: ")
        if len(new_status)>0:
            updated_status = new_status
            old_status.append(updated_status)  #adding the new status in the status list
        else:
            print "enter a valid status"
    elif existing_status.upper() == "Y":
        serial_no = 1
        for status in old_status :  #printing old status
            print str(serial_no) + ". " + status
            serial_no = serial_no + 1
        status_choice = input("enter your choice: ")
        updated_status = old_status[ status_choice-1 ]   #updating the status
    return updated_status

def add_friend():
    frnd = Spy('','',0,0.0)
    frnd.name = raw_input("what is your name? ")
    frnd.age = input("what is your age? ")
    frnd.rating = input("what is your rating? ")
    if len(frnd.name)>0 and 65>spy.age>16 and frnd.rating>spy.rating :
        friends.append(frnd)
    else:
        print "friend cannot be added"
    return len(friends)

def select_frnd(): #function to select friend
    print "select your friend"
    serial_no = 1
    for frnd in friends: #print friends list
        print str(serial_no) + " - " + frnd.name
        serial_no = serial_no + 1
    user_selected_frnd = input("enter your choice: ")  #select friend
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index

def send_message():
    selected_friend = select_frnd()
    original_image = raw_input("what is the name of original image? ") #here take it as .PNG
    output_path = "output.jpg"   #name of image
    secret_text = raw_input("what is your secret message? ")
    Steganography.encode(original_image,output_path,secret_text)
    print "message encoded"
    new_chat = ChatMessage(secret_text , True)
    friends[selected_friend].chats.append(new_chat)
    print "your secret message is ready"

def read_message():
    selected_friend = select_frnd()
    output_path =raw_input("which image you want to decode? ")
    secret_text = Steganography.decode(output_path)
    print "secret message is "+secret_text
    new_chat = ChatMessage(secret_text,False)
    friends[selected_friend].chats.append(new_chat)

def spy_chat(spy_name,spy_age,spy_rating):  #start_chat function
    current_status = None
    choice= -1
    print "Here are your options " + spy.name.upper()
    while choice!=0: #implementing of loop
        choice = input("\n *What do you want to do?\n  0-Exit \n  1-add the status \n  2-add the friend  \n  3-send a secret message \n  4-read a personal message \n  5-read chats from a user ")
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
            for k in friends:
                print str(friend_no)+"."+k['name']
                friend_no=friend_no+1
        elif choice == 3:
            send_message()
        elif choice == 4:
            read_message()
        elif choice == 5:
            print " **read chats from a user."
        else:                                    #for any invalid input
            print " **Oooopss invalid input."

f = datetime.now()
print f.strftime("%b %d %Y %H:%M:%S") #use of string time format
print "HELLO-WORLD"
print 'let\'s get started'
old_status = ['\"galti,badi galti,engineering\"' , '\"attitude toh bachpan se hai jab paida huaa toh 2 saal mene kisi se baat nhi krri\"' , '\"papa ki pari\"' , '\"sleeping\"', '\"busy\"' , '\"Mujse baat mt krna mai apna bna leta hu\"']
frnd1 = Spy('naman' , 'Mr' , 23, 2.9)
frnd2 = Spy('anand','Mr',18,6.9)
friends = [frnd1,frnd2]
spy_reply = raw_input("Are you a new user?(Y/N)")
if spy_reply.upper() == "N":  #Y should be in inverted coumma bcz both are string
    print "WELCOME back "+spy.name+ "age is "+ str(spy.age) + " having rating "+ str(spy.rating)  #convert non-string vriable to sring variable using str()
    spy_chat(spy.name ,spy.age, spy.rating)
elif spy_reply.upper() == "Y":  #.upper() is used to convert user's input into capital letter
    spy = Spy("","",0,0.0)
    spy.name = raw_input("enter your spy name")#spy_name is variable
    if spy.name.isspace():
        print "enter a valid name"
    elif spy.name.isdigit():
        print "Enter valid name."
    elif len(spy.name)>2: #checking length of sting
        print "WELCOME "+spy.name.upper()+".Glad to have you with us."
        salutation = raw_input("What should we call you (Mr.or Ms.) ")
        if salutation == "Mr." or salutation == "Ms.":  #if,else condition
            spy_name = salutation+" "+spy.name.upper()  #Using + for string concatenation
            print spy.name  #home work
            print "Alright "+spy_name+".I'd like to know a little bit more about you before we proceed...."  #home work
            spy.age = 0  #variable declaration ,integer type
            spy.rating = 0.0  #variable declaration for float number
            spy.age = input("What is your age?")
            if 65 > spy.age > 16:  # and operator is also a solution of this
                print "CONGRATS...You are eligible for spy."
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
                spy_chat(spy.name, spy.age , spy.rating )
            else:
                print "You are not eligible for spy."
        else:
            print "Please check salutation."
    else:
        print "Ooopss please enter a valid name."
else:
    print "Invalid entry."