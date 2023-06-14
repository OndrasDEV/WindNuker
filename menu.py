import os
from spammer import spam
from deleter import delete
from rgbprint import gradient_print,Color

def title():
    os.system("title Wind Nuker V1 (made by ondras)")

def clear():
    os.system("cls")
    
def logo():
    clear()
    gradient_print("""
    

██╗    ██╗██╗███╗   ██╗██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
██║    ██║██║████╗  ██║██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██║  ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║  ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║██████╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                              


    """, start_color=Color.white,end_color=Color.blue)
logo()


def menu():
    while True:
        logo()
        title()
        gradient_print("""
        [1] Webhook Spammer
        [2] Webhook Deleter
        [0] Exit
        """,start_color=Color.blue,end_color=Color.dark_blue)
        choice = int(input(">"))
        if choice == 1:
            clear()
            webhooklink = input("Enter Webhook Link: ")
            msg = input("What Message do you want to send: ")
            looplen = int(input("How many Times do you want to send the message?: "))
            spam(looplen,webhooklink,msg)
        elif choice == 2:
            clear()
            webhookaddr =input("Enter Webhook Link: ")
            delete(webhookaddr)
        clear()
menu()       





