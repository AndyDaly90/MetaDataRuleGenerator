from Tkinter import *
import Tkinter as tk
from metaDataRules import *


def display_setValue():
    result = MetaDataRules.setValue(form_id.get(), destination_field_id.get(), set_value.get())
    e2.insert(1.0, result)


def display_setConcat():
    result = MetaDataRules.concat(form_id.get(), destination_field_id.get(), first_field_id.get(), concat_val.get(),
                                  second_field_id.get())
    e2.insert(1.0, result)


def display_setDateUDT():
    result = MetaDataRules.stringToDate(d_field.get(), s_field.get())
    e2.insert(1.0, result)


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        menu = tk.Menu(root)
        root.config(menu=menu)

        sub_process_string = tk.Menu(menu)
        sub_process_date = tk.Menu(menu)

        menu.add_cascade(label="String Process Rules", menu=sub_process_string)
        menu.add_cascade(label="Date Process Rules", menu=sub_process_date)

        sub_process_string.add_command(label="Set Value", command=self.captureSetValue)
        sub_process_string.add_command(label="Concat", command=self.captureSetConcat)
        sub_process_string.add_separator()
        # sub_process_string.add_command(label="Exit", command=leave)

        sub_process_date.add_command(label="String to Date (UDT)", command=self.captureDate)

    def captureSetValue(self):
        t = tk.Toplevel(self)
        t.wm_title("Window")

        Label(t, text="Enter Form ID: ").grid(row=0)
        Label(t, text="Enter Destination Field ID: ").grid(row=1)
        Label(t, text="Enter Value to set: ").grid(row=2)

        form_id = Entry(t)
        destination_field_id = Entry(t)
        set_value = Entry(t)

        form_id.grid(row=0, column=1)
        global form_id

        destination_field_id.grid(row=1, column=1)
        global destination_field_id

        set_value.grid(row=2, column=1)
        global set_value

        btn = Button(t, text="Create Rule", command=display_setValue)
        btn.grid(row=3, column=0)

        e2 = Text(t, width=60, height=6)
        global e2
        e2.grid(row=4, column=1)

    def captureSetConcat(self):
        t = tk.Toplevel(self)
        t.wm_title("Window")

        Label(t, text="Enter Form ID: ").grid(row=0)
        Label(t, text="Enter Destination Field ID: ").grid(row=1)
        Label(t, text="Enter First Field ID: ").grid(row=2)
        Label(t, text="Enter Concatenation Value: ").grid(row=3)

        form_id = Entry(t)
        destination_field_id = Entry(t)
        first_field_id = Entry(t)
        concat_val = Entry(t)
        second_field_id = Entry(t)

        form_id.grid(row=0, column=1)
        global form_id

        destination_field_id.grid(row=1, column=1)
        global destination_field_id

        first_field_id.grid(row=2, column=1)
        global first_field_id

        concat_val.grid(row=3, column=1)
        global concat_val

        second_field_id.grid(row=4, column=1)
        global second_field_id

        btn = Button(t, text="Create Rule", command=display_setConcat)
        btn.grid(row=4, column=0)

        e2 = Text(t, width=60, height=6)
        global e2
        e2.grid(row=4, column=1)

    def captureDate(self):
        t = tk.Toplevel(self)
        t.wm_title("Window")

        Label(t, text="Enter Destination Field ID: ").grid(row=0)
        Label(t, text="Enter Source Field ID: ").grid(row=1)

        d_field = Entry(t)
        s_field = Entry(t)

        d_field.grid(row=0, column=1)
        global d_field

        s_field.grid(row=1, column=1)
        global s_field

        btn = Button(t, text="Create Rule", command=display_setDateUDT)
        btn.grid(row=3, column=0)

        e2 = Text(t, width=60, height=6)
        global e2
        e2.grid(row=3, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("700x100")
    root.mainloop()
