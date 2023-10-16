
from py_canoe import CANoe
from time import sleep as wait
import tkinter.filedialog
import tkinter as tk
from win32com.client import *
from win32com.client.connect import *
 
#implementing a class which has the following modules:
#open CANoe by user input of the specific configuration file
#start the measurements
#the set signal method
# get signal method
# stop measurements
# close CANoe
#seat test for config path

 
class Canoe:
    
    def __init__(self):
        self.canoe_inst = CANoe()
                
    # module for opening CANoe
    def open_Canoe(self):
        root = tk.Tk()
        root.withdraw()
        file_path = tkinter.filedialog.askopenfilename()
        try:
            self.canoe_inst.open(canoe_cfg=file_path)
        except:
            print("Wrong file or the file is already open")
        
    # starting measurements
    def str_measur(self):
        wait(5)
        self.canoe_inst.start_measurement()
        
    #get signal 
    def get_signal(self, message, signal, channel= "CAN", can_nr = 1): #default values: channel / can_nr
        try:
            return self.canoe_inst.get_signal_value(channel, can_nr, message, signal)
        except:
            print("not good values")
        
        
    
    #set signal
    def set_signal(self, message, signal, value, channel= "CAN", can_nr = 1):  #default values: channel / can_nr
        #can_nr, value integers; messages str
        try:
            self.canoe_inst.set_signal_value(channel, can_nr, message, signal, value)
            wait(5)
        except:
           print(" not good values")
                
    def set_syst_signal(self, sys_var_name, value ):
        try:
            self.canoe_inst.set_system_variable_value(sys_var_name, value)
        except:
            if(not isinstance(sys_var_name, str) ):
                print("Wrong system variable namespace or name")
            elif(not isinstance(value, int)):
                print("Value is not a valid integer!")
            
    def get_syst_signal(self, sys_var_name):
        try:
           return self.canoe_inst.get_system_variable_value(sys_var_name)
        except:
             if(not isinstance(sys_var_name, str)):
                print("Wrong system variable namespace or name,")
    
    def send_diagnostic(self,diag_ecu_qualifier_name , request, request_in_bytes = True):
        return self.canoe_inst.send_diag_request(diag_ecu_qualifier_name, request, request_in_bytes)
    
    # Environment variables manipulation
    def get_EnvVar(self, var):
        try:
            return self.canoe_inst._CANoe__canoe_objects.get("Environment").GetVariable(var).Value
        except ValueError:
            print ("Couldn't find value")

    def set_EnvVar(self, var, value):
        # set the environment varible
        result = self.canoe_inst._CANoe__canoe_objects.get("Environment").GetVariable(var)
        result.Value = value
        wait(1)
        if( self.get_EnvVar(var) == value):
            print("Set to: ", self.get_EnvVar(var))
        else:
            raise ValueError("Value not corresponding")
            
    #Connectivity with ethernet 
    def Connect_DOIP(self, var):
        try:
            self.set_EnvVar(var, 1)
            wait(2)
            self.set_EnvVar(var, 0)   
        except AttributeError:
            print("Wrong value or Environment variable")
            
    # Reading DTC   
    def Read_DTC(self):
        try:
            self.set_EnvVar("Env_DoipConnectVeh", 1)
            wait(2)
            self.set_EnvVar("Env_DoipConnectVeh", 0)   
        except AttributeError:
            print("Wrong value or Environment variable")    
        rec= self.get_EnvVar("Env_DoipDirectReceive")   
        # put the received Diagnostic code into a list
        listOfDiag = splitDiagResponse(rec)
        print(listOfDiag)
        
    #RBEOL
    def RBEOL(self):
        try:
            self.set_EnvVar("Env_RBEOL", 1)
            wait(2)
            self.set_EnvVar("Env_RBEOL", 0)   
        except AttributeError:
            print("Wrong value or Environment variable")
        
    #RBEOL_unlock
    def RBEOL_unlock(self):
        try:
            self.set_EnvVar("Env_JLR_Prog_Unlock", 1)
            wait(2)
            self.set_EnvVar("Env_JLR_Prog_Unlock", 0)   
        except AttributeError:
            print("Wrong value or Environment variable")
     
            
        
    #stop measurements
    def stop_measur(self):
        wait(5)
        self.canoe_inst.stop_measurement()
        
    #close CANoe
    def close_Canoe(self):
        wait(5)
        self.canoe_inst.quit()
        

def splitDiagResponse(str_var):
    usefull_code = str_var[6:]
    firstSix = str_var[:6]
    
    if firstSix != "59027B":
        print("Error")
    else:
        if len(str_var)==6:
            print("No DTC")
            
        elif len(str_var)>6:
            mylist = []
            for i in range(0, len(usefull_code), 8):
                mylist.append(usefull_code[i:i+8])

            dict_code = []
            for i in mylist:
                dict_code.append(i[:6])
                dict_code.append(i[6:])
                
            final_list=[]
            for i in range(0, len(dict_code), 2):
                final_list.append(dict_code[i:i+2])
            
            return final_list  
            
    
