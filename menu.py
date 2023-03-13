from colorama import Fore
import os
from spammer import spam
from deleter import delete

def clear():
    os.system("cls")
    
def logo():
    clear()
    print(Fore.CYAN,"""
    

██╗    ██╗██╗███╗   ██╗██████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
██║    ██║██║████╗  ██║██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██║  ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║  ██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║██████╔╝    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                              


    """)
logo()


def menu():
    while True:
        logo()
        print("[1] Webhook Spammer")
        print("[2] Webhook Deleter")
        print("[0] Exit")
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





