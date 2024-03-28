import os
import tkinter as tk
from tkinter import filedialog, font, messagebox
from encrypt_function import encrypt_file, decrypt_file

# Global variable to store the file to encrypt/decrypt
store_file = str()


def open_file():
    '''Allows the user to choose a file within their directory with the limitation of only txt files.'''
    global store_file
    user = os.getenv('USERNAME')
    print("Choose a file!")
    user_choose_file: None
    user_choose_file = filedialog.askopenfilename(initialdir=f'C:\\Users\\{user}\\Documents',
                                                  title='Search for file to encrypt',
                                                  filetypes=[("Text files", "*.txt")])
    if user_choose_file == '' or user_choose_file == None:
        return None
    else:
        store_file = user_choose_file
        return store_file


def open_and_encrypt_file():
    '''Choose a file to encrypt and then provide confirmation to the user of this action.'''
    file_exist_or_not = open_file()
    if file_exist_or_not == None or file_exist_or_not == '':
        return
    else:
        message_box = messagebox.askyesno('Encrypt File Confirmation', f'Are you sure you want to encrypt {store_file}?')
        if message_box:
            encrypt_file(store_file)
            message_box_confirmation = messagebox.Message(master=window, message='File has been encrypted', title='Confirmation')
            message_box_confirmation.show()


def open_and_decrypt_file():
    '''Choose a file to decrypt and then provide confirmation to the user of this action.'''
    file_exist_or_not = open_file()
    if file_exist_or_not == None or file_exist_or_not == '':
        return
    else:
        message_box = messagebox.askyesno('Decrypt File Confirmation', f'Are you sure you want to decrypt {store_file}?')
        if message_box:
            decrypt_file(store_file)
            message_box_confirmation = messagebox.Message(master=window, message='File has been decrypted', title='Confirmation')
            message_box_confirmation.show()


def exit_gui_program():
    '''Will prompt the user with a message if they want to exit the program.'''
    message_box = messagebox.askyesno('Exit Program Confirmation', 'Are you sure you want to exit?')
    if message_box:
        window.destroy()


window = tk.Tk(className=' Encrypt File GUI')
window.geometry('600x300')


# Frame to store buttons, left side of screen
frame = tk.Frame(master=window)
frame.pack(side='left', anchor='nw')

# Choosing font and text to display to user
arial_font_bold = font.Font(family='Arial', size=12, weight='bold')
label = tk.Label(master=window,
                 font=arial_font_bold,
                 foreground='black',
                 height=2,
                 width=100,
                 text="Choose a file to encrypt")
label.pack()

# Button used to choose which file to encrypt
choose_file_to_encrypt = tk.Button(master=frame,
                        width=15,
                        height=3,
                        background='black',
                        activebackground='blue',
                        foreground='white',
                        text="Encrypt File",
                        command=open_and_encrypt_file)

# Position button north-west
choose_file_to_encrypt.pack(anchor='nw')

# Button used to choose which file to decrypt
choose_file_to_decrypt = tk.Button(master=frame,
                        width=15,
                        height=3,
                        background='black',
                        activebackground='blue',
                        foreground='white',
                        text="Decrypt File",
                        command=open_and_decrypt_file)

choose_file_to_decrypt.pack()

# Button used to exit the GUI
exit_gui = tk.Button(master=frame,
                        width=15,
                        height=3,
                        background='black',
                        activebackground='blue',
                        foreground='white',
                        text="Exit",
                        command=exit_gui_program)

exit_gui.pack()

# Adding vertical lines to make the buttons look more organized
vertical_line = tk.Frame(master=window, width=2, bg='dark blue')
vertical_line.pack(anchor='nw', side='left', fill='y', padx=1)

# Prints a list of all of the modules apart of the tkinter package
# user = os.getenv('USERNAME')
# path = fr'C:\Users\{user}\AppData\Local\Programs\Python\Python312\Lib\tkinter'

# testing = os.listdir(path)
# for element in testing:
#     print(element)