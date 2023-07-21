# Simple GUI to display the date and time 
# Written by Mason Lauderdale

import customtkinter as ctk
from time import strftime

class Clock():
    def __init__(self, master: ctk.CTk) -> None:

        #  GUI basics
        self.master = master  # Assign the actual ctk gui
        self.master.geometry('500x500')  # Default Resolution
        self.master.minsize(500,500)  # Min resolution size for readability sake
        self.master.resizable(True, True)  # Allows window resizeablility
        self.master.wm_title('Clock')  # Name of GUI
        self.master.wm_iconbitmap("clock.ico")

        #  Labels for the Time and Date
        self.time = ctk.CTkLabel(self.master, text=strftime("%I:%M:%S %p"), font=('Helvetica Bold', 40))
        self.date = ctk.CTkLabel(self.master, text=strftime("%A, %d %B %Y"), font=('Helvetica Bold', 40))

        #  Place Labels
        self.time.place(relx=0.5, rely=0.4, anchor='center')
        self.date.place(relx=0.5, rely=0.5, anchor='center')

        #  Button for Switching Time
        self.switchButton = ctk.CTkButton(self.master, text="Switch to 12 Hour Time", font=('Helvetica Bold', 30),
                                            command=self.switch, corner_radius=20)
        self.switchButton.place(relx=0.5, rely=0.7, anchor='center')

    #  displayDatetime() will continually update the date and the time 
    def displayDatetime(self):
        if self.switchButton._text == 'Switch to 24 Hour Time':  # So, if user is using 12 hour format
            self.time.configure(text=strftime("%I:%M:%S %p"))
            self.date.configure(text=strftime("%A, %d %B %Y"))
        else:
            self.time.configure(text=strftime("%H:%M:%S %p"))  # If user is using 24 hour format
            self.date.configure(text=strftime("%A, %d %B %Y"))
        self.time.after(1000, self.displayDatetime)  # Update the clock after 1000 ms, rerun the function to continually update

    # switch() will handle the button functionality, allowing user to switch time formats
    def switch(self): 
        if self.switchButton._text == 'Switch to 24 Hour Time':
            self.switchButton.configure(text='Switch to 12 Hour Time')
            self.displayDatetime()
            
        else:
            self.switchButton.configure(text='Switch to 24 Hour Time')
            self.displayDatetime()
            


if __name__ == '__main__':
    clock = ctk.CTk()
    gui = Clock(master=clock)

    gui.switch()
    clock.mainloop()