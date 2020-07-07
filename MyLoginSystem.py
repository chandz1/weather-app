# Imports
import smtplib
import random
import pickle
import os
os.system("CLS")

# Variables
usernames = ["sarath"]
passwords = ["sarath123"]
mails = ["sarathchandragodithi@gmail.com"]
verificationCode = random.randint(100000, 1000000)


# Functions
def saveFile():
    pickle.dump(usernames, open("usernames", "wb"))
    pickle.dump(passwords, open("passwords", "wb"))
    pickle.dump(mails, open("mails", "wb"))


def loadFile():
    global usernames
    global mails
    global passwords
    usernames = pickle.load(open("usernames", "rb"))
    mails = pickle.load(open("mails", "rb"))
    passwords = pickle.load(open("passwords", "rb"))


def Login():
    loadFile()
    Username = str(input("Enter Your Username: "))
    if Username.lower() in usernames:
        Password = str(input("Enter Your Password: "))
        if Password in passwords and passwords.index(Password) == usernames.index(Username.lower()):
            print("You have succesfully been logged in.")
        else:
            print("You have entered the wrong password.")
            print("\n\n\n")
            Login()
    else:
        print("You don't seem to have an account. Do you have an account?\n")
        accExistence = str(input())
        if accExistence.lower() == 'yes':
            print("\n")
            Login()
        elif accExistence.lower() == 'no':
            print("\n")
            createaccount()


def createaccount():
    global newMail
    newMail = str(input("Enter your Mail ID: "))
    if newMail.lower() in mails:
        print("This mail id is already in use. Kindly choose another one.")
        print("\n\n\n")
        createaccount()
    elif newMail.lower() not in mails:
        sendMail()
        userCode = int(input("Enter the verification code: "))
        if userCode == verificationCode:
            newUsername = str(input("Enter a username : "))
            if newUsername.lower() in usernames:
                print("This username has been taken.")
                print("\n")
            elif newUsername.lower() not in usernames:
                newPassword = str(input("Enter a password: "))
                confirmPassword = str(input("Reenter your password: "))
                if newPassword == confirmPassword:
                    usernames.append(newUsername.lower())
                    mails.append(newMail.lower())
                    passwords.append(newPassword)
                    savefile()
                    print("Your account has succesfully been created.")
                    print("\n")
                    Login()
                elif newPassword != confirmPassword:
                    print("The passwords you entered don't match.")
                    print("\n")
                    createaccount()
        elif userCode != verificationCode:
            print("You have entered the wrong verification code.")
            createaccount()


def sendMail():
    Email_Username = "pythonmailbot123@gmail.com"
    Email_Password = "python12345"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(Email_Username, Email_Password)

        subject = "Verification Code"
        body = "Here is your verification code ", verificationCode
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(Email_Username, newMail, msg)
        print("Mail has been sent.")
        print("\n\n")


# Program
saveFile()
accountExistence = str(input("Do you have an account? Enter Yes or No."))
if accountExistence.lower() == 'yes':
    Login()
elif accountExistence.lower() == 'no':
    wantToCreate = str(input("Do you want to make one? Enter Yes or No."))
    if wantToCreate.lower() == 'yes':
        createaccount()
    elif wantToCreate.lower() == 'no':
        print("Thank You.")
        exit()
