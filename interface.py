from tkinter import *
from tkinter import scrolledtext
from client import send, take_msg as receive_msg, DISCONNECT_MESSAGE
import threading

root = Tk()

# name
root.title("Chat App")
root.geometry("500x570+100+30")

# for logo
icon = PhotoImage(file='img.png')
root.iconphoto(True, icon)

# bg color
root.config(background="#A0A4C5")

# label
label = Label(root, text="   Messages and calls are end to end encrypted  ",
              font=('Arial', 9, 'bold'),
              bg="#e3c607",
              fg="#450335")
label.pack(padx=108, pady=20)

# textarea
DisplayText = scrolledtext.ScrolledText(root, state=DISABLED,
                                        wrap=WORD, bg="white",
                                        font=("Arial", 10, "bold"))
DisplayText.pack(fill=BOTH, expand=True)

# input area
InputText = scrolledtext.ScrolledText(root, wrap=WORD, height=1,
                                      fg="white", bg="#450335",
                                      font=("Arial", 15, "bold"))
InputText.pack(pady=15, fill=X)


# send button
def FuncSendText():
    UserInput = InputText.get("1.0", END).strip()
    if UserInput:
        send(UserInput)
        DisplayText.config(state=NORMAL)
        DisplayText.insert(END, "You: " + UserInput + "\n")
        InputText.delete("1.0", END)
        DisplayText.config(state=DISABLED)


SendButton = Button(root, text="Send \U0001F680",
                    font=("Georgia", 17),
                    command=FuncSendText,
                    fg="white", bg="#450335")

SendButton.pack(side=RIGHT)


# disconnect button
def SuncDisText():
    send(DISCONNECT_MESSAGE)
    root.quit()


DisconnectButton = Button(root, text="Disconnect \U0001F480",
                          font=("Georgia", 17),
                          command=SuncDisText,
                          fg="white", bg="#450335")

DisconnectButton.pack(side=RIGHT)


# function to receive messages
def receive_messages():
    while True:
        msg = receive_msg()
        if msg:
            DisplayText.config(state=NORMAL)
            DisplayText.insert(END, msg + "\n")
            DisplayText.config(state=DISABLED)


# start a thread to receive messages
thread = threading.Thread(target=receive_messages)
thread.daemon = True
thread.start()

root.mainloop()
