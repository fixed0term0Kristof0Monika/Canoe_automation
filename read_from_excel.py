from openpyxl import load_workbook
import tkinter.filedialog
import tkinter as tk


def openExcelFile():
    # root = tk.Tk()
    # root.withdraw()
    # file_path = tkinter.filedialog.askopenfilename()
    workbook =  load_workbook(filename= "Book1.xlsx")
    cell = workbook.active
    return cell
    
    
def extractFromExcel(cell,variable):
    return cell[variable].value
    
       


