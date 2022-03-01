# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 21:26:05 2022

@author: ttu2hc
"""
import tkinter as tk
import os
from tkinter import *
from tkinter import messagebox

class rootframe():
    def __init__(self):
        self.rootpath = r""
        self.result = []
        self.SearchInput = tk.StringVar(value = "")
        #self.root = tk.Tk()
        self.root = Toplevel()
        self.root.title('Simple Files Search')

        #Folder frame
        self.RootFolderFrame = tk.Frame(master = self.root)
        self.RootFolderFrame.grid(row = 0, column = 0, sticky = "nw")
        
        self.RootFolderLabel = tk.Label(master = self.RootFolderFrame
                                   , text='Root Folder Path')
        self.RootFolderLabel.grid(row = 0, column = 0, sticky = "nw")
        
        #global RootFolderEntry
        self.RootFolderEntry = tk.Entry(master = self.RootFolderFrame
                                   , width=80)
        self.RootFolderEntry.insert(0, 'Please select the root folder')
        self.RootFolderEntry.grid(row = 1, column = 0, sticky = "nw")
        
        self.RootFolderBut = tk.Button(master = self.RootFolderFrame
                                     , text='...'
                                     , command=self.folderselect
                                     , width=2
                                     , height=1)
        self.RootFolderBut.grid(row = 1, column = 1, sticky = "nw")
        
        #File or Folder
        self.SelectFrame = tk.Frame(master = self.root)
        self.SelectFrame.grid(row = 2, column = 0, sticky = "nw")
        #global SelectVar
        self.SelectVar = tk.IntVar(value=1)
        self.FileCheckBox = tk.Radiobutton(master = self.SelectFrame
                                      , text="File"
                                      , variable= self.SelectVar
                                      , value = 1
                                      , command = self.sel)
        self.FileCheckBox.grid(row = 0, column = 0, sticky = "nw")
        self.FolderCheckBox = tk.Radiobutton(master = self.SelectFrame
                                        , text="Folder"
                                        , variable= self.SelectVar
                                        , value = 2
                                        , command = self.sel)
        self.FolderCheckBox.grid(row = 0, column = 1, sticky = "nw")
        
        #Search Input frame
        self.InputDataFrame = tk.Frame(master = self.root)
        self.InputDataFrame.grid(row = 3, column = 0, sticky = "nw")
        
        self.InputDataLabel = tk.Label(master = self.InputDataFrame
                                   , text='Find what')
        self.InputDataLabel.grid(row = 0, column = 0, sticky = "nw")
        
        #global InputDataEntry
        self.InputDataEntry = tk.Entry(master = self.InputDataFrame
                                 , textvariable= self.SearchInput
                                 , width=80)
        self.InputDataEntry.insert(0, '')
        self.InputDataEntry.grid(row = 1, column = 0, sticky = "nw")
        
        #Output frame
        self.OutputFrame = tk.Frame(master = self.root)
        self.OutputFrame.grid(row = 4, column = 0, sticky = "nw")
        
        self.OutputLabel = tk.Label(master = self.OutputFrame
                                   , text='Output')
        self.OutputLabel.grid(row = 0, column = 0, sticky = "nw")
        
        #global OutputEntry
        self.OutputEntry = tk.Entry(master = self.OutputFrame
                                   , width=80)
        self.OutputEntry.insert(0, '')
        self.OutputEntry.grid(row = 1, column = 0, sticky = "nw")
           
        #Start button
        self.StartFrame = tk.Frame(master = self.root)
        self.StartFrame.grid(row = 5, column = 0, sticky = "nw")
        
        self.SearchBut = tk.Button(master = self.StartFrame
                                     , text='Search'
                                     , command=self.searchfunc
                                     , width=5
                                     , height=2)
        self.SearchBut.grid(row = 0, column = 0, sticky = "nw")
        
    def start(self) -> None:
        try:
            self.root.mainloop()
            return
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
            
    def folderselect(self) -> None:
        try:
            self.rootpath = filedialog.askdirectory()
            self.RootFolderEntry.delete(0, 'end')
            self.RootFolderEntry.insert(tk.END, self.rootpath)
            return
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

    def sel(self) -> None:
        temp = self.SelectVar.get()
        return
     
    def searchfunc(self) -> None:
        SearchData  = self.SearchInput.get()
        if SearchData == "" or "*" in SearchData:
            messagebox.showerror("Error", "Error input")
            return
        else:     
             if self.SelectVar.get() == 1:
                 for root, dirs, files in os.walk(self.rootpath):
                     for name in files:
                         #FindIndex = name.rfind('.')
                         #filetype = name[FindIndex:]
                         if SearchData in name:
                             temppath = os.path.join(root, name)
                             self.result.append(temppath)
             elif self.SelectVar.get() == 2:
                 for root, dirs, files in os.walk(self.rootpath):
                     for name in dirs:
                         if SearchData in name:
                             temppath = os.path.join(root, name)
                             self.result.append(temppath)
             else:
                 messagebox.showerror("Error", "Unknow Error")
             resultpath = r""
             #Write output
             try: 
                 resultpath = os.path.dirname(os.path.realpath(__file__))
                 resultpath = resultpath + '\Result.txt'
             except Exception as e:
                 messagebox.showerror("Error", str(e))
                 return
             with open(resultpath,'w',encoding="utf-8") as f:
                 try:
                     for line in self.result:
                         f.writelines(line)
                         f.writelines('\n')
                 except Exception as e:
                     messagebox.showerror("Error", str(e))
                 finally:
                     f.close()
             self.OutputEntry.delete(0, 'end')
             self.OutputEntry.insert(tk.END, resultpath)
             return