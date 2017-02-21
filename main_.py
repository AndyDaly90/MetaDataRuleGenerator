#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import Tkinter as tk
from tkinter import filedialog
from metaDataRules import *
import tkinter.messagebox as message
import openpyxl
import re


def display_setValue():
    result = MetaDataRules.setValue(form_id.get(), destination_field_id.get(), set_value.get())
    entry_box.insert(1.0, result)


def display_setConcat():
    result = MetaDataRules.concat(form_id.get(), destination_field_id.get(), first_field_id.get(), concat_val.get(),
                                  second_field_id.get())
    entry_box.insert(1.0, result)


def display_setDateUDT():
    result = MetaDataRules.stringToDate(d_field.get(), s_field.get())
    entry_box.insert(1.0, result)


def display_crossDB_insert():
    result = MetaDataRules.crossDbInsert(source_form_id, source_form, source_field_IDs,
                                         destination_form_id, destination_fieldIDs)
    entry_box.insert(1.0, result)


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        menu = tk.Menu(root)
        root.config(menu=menu)

        sub_process_string = tk.Menu(menu)
        sub_process_date = tk.Menu(menu)
        sub_process_cross_db = tk.Menu(menu)

        menu.add_cascade(label="String Process Rules", menu=sub_process_string)
        menu.add_cascade(label="Date Process Rules", menu=sub_process_date)
        menu.add_cascade(label="Cross Database Rules", menu=sub_process_cross_db)

        sub_process_string.add_command(label="Set Value", command=self.captureSetValue)
        sub_process_string.add_command(label="Concat", command=self.captureSetConcat)
        sub_process_string.add_separator()
        # sub_process_string.add_command(label="Exit", command=leave)

        sub_process_date.add_command(label="String to Date (UDT)", command=self.captureDate)

        sub_process_cross_db.add_command(label="Cross Database Insert", command=self.captureCrossDBInsert)

    def captureSetValue(self):
        window = tk.Toplevel(self)
        window.wm_title("Set Value")

        Label(window, text="Enter Form ID: ").grid(row=0)
        Label(window, text="Enter Destination Field ID: ").grid(row=1)
        Label(window, text="Enter Value to set: ").grid(row=2)

        global form_id
        global destination_field_id
        global set_value
        global entry_box

        form_id = Entry(window)

        destination_field_id = Entry(window)

        set_value = Entry(window)

        form_id.grid(row=0, column=1)

        destination_field_id.grid(row=1, column=1)

        set_value.grid(row=2, column=1)

        btn = Button(window, text="Create Rule", command=display_setValue)
        btn.grid(row=3, column=0)

        entry_box = Text(window, width=60, height=6)
        entry_box.grid(row=4, column=1)

    def captureSetConcat(self):
        window = tk.Toplevel(self)
        window.wm_title("Concatenation")

        Label(window, text="Enter Form ID: ").grid(row=0)
        Label(window, text="Enter Destination Field ID: ").grid(row=1)
        Label(window, text="Enter First Field ID: ").grid(row=2)
        Label(window, text="Enter Concatenation Value: ").grid(row=3)

        global form_id
        global destination_field_id
        global first_field_id
        global concat_val
        global second_field_id

        form_id = Entry(window)
        destination_field_id = Entry(window)
        first_field_id = Entry(window)
        concat_val = Entry(window)
        second_field_id = Entry(window)

        form_id.grid(row=0, column=1)

        destination_field_id.grid(row=1, column=1)

        first_field_id.grid(row=2, column=1)

        concat_val.grid(row=3, column=1)

        second_field_id.grid(row=4, column=1)

        btn = Button(window, text="Create Rule", command=display_setConcat)
        btn.grid(row=4, column=0)

        global entry_box
        entry_box = Text(window, width=60, height=6)
        entry_box.grid(row=4, column=1)

    def captureDate(self):
        window = tk.Toplevel(self)
        window.wm_title("Convert to UDT")

        Label(window, text="Enter Destination Field ID: ").grid(row=0)
        Label(window, text="Enter Source Field ID: ").grid(row=1)

        global d_field
        global s_field
        global entry_box

        d_field = Entry(window)
        s_field = Entry(window)

        d_field.grid(row=0, column=1)

        s_field.grid(row=1, column=1)

        btn = Button(window, text="Create Rule", command=display_setDateUDT)
        btn.grid(row=3, column=0)

        entry_box = Text(window, width=60, height=6)
        entry_box.grid(row=3, column=1)

    def captureCrossDBInsert(self):
        try:
            window = tk.Toplevel(self)
            window.wm_title("Cross Database Insert")
            root.fileName = filedialog.askopenfilename(filetypes=(("Excel Files", "*.xlsx"), ("All files", "*.*")))

            # This workbook object represents the excel file
            work_book = openpyxl.load_workbook(root.fileName)

            sheet1 = work_book.get_sheet_by_name('Sheet1')

            global source_field_IDs
            global destination_fieldIDs
            global source_form_id
            global destination_form_id
            global source_form
            global entry_box

            source_field_IDs = []

            destination_fieldIDs = []

            for i in range(2, sheet1.max_row):
                source_field_IDs.append(sheet1.cell(row=i, column=1).value)
                destination_fieldIDs.append(sheet1.cell(row=i, column=2).value)

            source_form_id = re.findall(r'\d+', source_field_IDs[1])[:1]
            destination_form_id = re.findall(r'\d+', destination_fieldIDs[1])[:1]

            source_form_id = source_form_id[0]

            destination_form_id = destination_form_id[0]

            source_form = "strCDA_" + source_form_id + "_"

            entry_box = Text(window, width=70, height=8)
            entry_box.grid(row=3, column=1)

            btn = Button(window, text="Create Rule", command=
            display_crossDB_insert)

            btn.grid(row=3, column=0)

            message.showinfo("Success", "The excel file has been loaded \n Select Create Rule")
            window.geometry('630x200+500+350')

        except EnvironmentError:
            message.showerror("Result", "There is an error with your file")


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("900x100")
    root.mainloop()
