from tkinter import Tk, Button, Label
from functools import partial
import operator
window = Tk()
window.config(background='black')
# window.minsize(width=500, height=200)

# global Flag. If flag is True = count everything
global flag
flag = False

# operators dict

stored_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    }

# Dict to put number in a right order. Because started with 9 in for loop creating buttons.
test_dict = {0: 9,
             1: 8,
             2: 7,
             3: 6,
             4: 5,
             5: 4,
             6: 3,
             7: 2,
             8: 1,
             9: 0
             }


def adding_numbers(button_id):
    """
    Takes number from a button. Adds it to the row.
    """
    number = buttons_array[button_id]['text']
    users_entry_number = test_dict[number]

    if text_entry['text'] == str(0) and users_entry_number != '0':
        # if start over removing zero. And doesn't allow to spam zeroes.
        text_entry.config(text=str(users_entry_number))
    else:
        text_entry.config(text=text_entry['text'] + str(users_entry_number))


def take_action(act_id):
    global flag
    """
    Takes a symbol of an action. Checks if action symbol already was used.
    Also, addition and substruction to a zero.
    """
    if flag:
        equal_action()

    if not text_entry['text'].endswith(' ') and text_entry['text'] != '0':
        text_entry.config(text=text_entry['text'] + f' {act_id} ')
        flag = True
    elif text_entry['text'] == '0':
        # We still can use '+' and '-' with zero;
        if act_id == '+' or act_id == '-':
            text_entry.config(text=text_entry['text'] + f' {act_id} ')
            flag = True


def start_over():
    """
    Ground zero. Cancel button.
    """
    text_entry.config(text='0')


def equal_action():
    """
    Counting. Action priority.
    """
    summary = 0
    result = text_entry['text'].split()
    counter_result = (stored_operators[result[1]](int(result[0]), int(result[2])))
    text_entry.config(text=str(counter_result))
    # try:
    #     int(result[-1])
    # except ValueError:
    #     del result[-1]

    # Checks if *+-/ . Changing both numbers and moves on.
    """
    Very effective code :)
    """
    # maximum = 0
    # number_counter = 0
    #
    # # * /
    # for zxc in range(len(result)):
    #
    #     if result[zxc] == '*' or result[zxc] == '/':
    #         if result[zxc] == '*':
    #             number_counter = int(result[zxc + 1]) * int(result[zxc - 1])
    #             result[zxc + 1] = number_counter
    #             result[zxc - 1] = number_counter
    #             # del result[zxc]
    #             # del result[zxc - 1]
    #         elif result[zxc] == '/':
    #             number_counter = int(result[zxc - 1]) / int(result[zxc + 1])
    #             result[zxc + 1] = number_counter
    #             result[zxc - 1] = number_counter
    #             # del result[zxc]
    #             # del result[zxc - 1]    # + -
    #         if number_counter > maximum:
    #             maximum = number_counter
    # for asd in range(len(result)):
    #     if result[asd] == '+' or result[asd] == '-':
    #         if result[asd] == '+':
    #             number_counter = int(result[asd + 1]) + int(result[asd - 1])
    #             result[asd + 1] = number_counter
    #             result[asd - 1] = number_counter
    #             # del result[asd]
    #             # del result[asd - 1]
    #         elif result[asd] == '-':
    #             number_counter = int(result[asd - 1]) - int(result[asd + 1])
    #             result[asd + 1] = number_counter
    #             result[asd - 1] = number_counter
    #             # del result[asd]
    #             # del result[asd - 1]
    #         if number_counter > maximum:
    #             maximum = number_counter
    # # text_entry.config(text=result)
    # text_entry.config(text=str(maximum))


# Header. Numbers storage
text_entry = Label(text='0', background='white', height=3)
text_entry.grid(column=0, row=0, columnspan=4, sticky='we')
text_entry.config(background='coral', font=("Arial", 16, 'bold'), fg='black')

"""
Buttons numbers rows
"""
buttons_array = []
row_counter = 1
column_counter = 2
for i in range(9, -1, -1):
    """
    Creates 9 buttons int numbers
    """
    temp_button = Button(text=i, background='white', width=8, height=3, font=('Arial', 12, 'bold'),
                         command=partial(adding_numbers, i))
    temp_button.grid(column=column_counter, row=row_counter, sticky='we')
    buttons_array.append(temp_button)

    column_counter -= 1
    if column_counter == -1:
        row_counter += 1
        column_counter = 2

buttons_array[-1].grid(column=1)

"""
Activity row
"""

action_buttons = []
activity = ['+', '-', '*', '/']
for i in range(4):
    act_button = Button(text=activity[i], background='white', width=8, height=3, font=('Arial', 12, 'bold'),
                        command=partial(take_action, activity[i]))
    act_button.grid(column=column_counter + 2, row=i + 1)

"""
Cancel button
"""
cancel_button = Button(text='C', background='white', width=8, height=3, font=('Arial', 12, 'bold'),
                       command=start_over)
cancel_button.grid(column=0, row=4)

"""
Equal button
"""
equal_button = Button(text='==', background='white', width=8, height=3, font=('Arial', 12, 'bold'),
                      command=equal_action)
equal_button.grid(column=2, row=4)

window.mainloop()
