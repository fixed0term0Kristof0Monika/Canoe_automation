
from py_canoe import CANoe
from time import sleep as wait
import tkinter.filedialog
import tkinter as tk
import win32com.client
 
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
            print(self.canoe_inst.get_signal_value(channel, can_nr, message, signal))
        except:
            if( channel not in ["CAN", "Ethernet"]):
                print("The channel is not good, try CAN or Ethernet!")
            elif(can_nr not in [1, 2]):
                print("Can only has 2 channel numbers 1 and 2!")
            elif(message not in ["EngineState", "LightState"]):
                print("Incorrect message, CAN only has EngineState and LightState!")
            elif(signal not in ["EngineSpeed", "FlashLight", "HeadLight", "OnOff"]):
                print("Wrong signal, try EngineSpeed, FlashLight, HeadLight or OnOff")
        
        
    
    #set signal
    def set_signal(self, message, signal, value, channel= "CAN", can_nr = 1):  #default values: channel / can_nr
        #can_nr, value integers; messages str
        try:
            self.canoe_inst.set_signal_value(channel, can_nr, message, signal, value)
            wait(5)
        except:
            if( channel not in ["CAN", "Ethernet"]):
                print("The channel is not good, try CAN or Ethernet!")
            elif(can_nr not in [1, 2]):
                print("Can only has 2 channel numbers 1 and 2!")
            elif(message not in ["EngineState", "LightState"]):
                print("Incorrect message, CAN only has EngineState and LightState!")
            elif(signal not in ["EngineSpeed", "FlashLight", "HeadLight", "OnOff"]):
                print("Wrong signal, try EngineSpeed, FlashLight, HeadLight or OnOff") 
            elif( not isinstance(value, int)):
                print("The value is not good, not an integer")
                
    def set_syst_signal(self, sys_var_name, value ):
        try:
            self.canoe_inst.set_system_variable_value(sys_var_name, value)
        except:
            if(not isinstance(sys_var_name, str) ):
                print("Wrong system variable namespace or name, \ntry Engine or Lights insted with its name eg. EngineSpeedEntry")
            elif(not isinstance(value, int)):
                print("Value is not a valid integer!")
            
    def get_syst_signal(self, sys_var_name):
        try:
            self.canoe_inst.get_system_variable_value(sys_var_name)
        except:
             if(not isinstance(sys_var_name, str)):
                print("Wrong system variable namespace or name, \ntry Engine or Lights insted with its name eg. EngineSpeedEntry")
    
    def send_diagnostic(self,diag_ecu_qualifier_name , request, request_in_bytes = True):
        self.canoe_inst.send_diag_request(diag_ecu_qualifier_name, request, request_in_bytes)
    #stop measurements
    def stop_measur(self):
        wait(5)
        self.canoe_inst.stop_measurement()
        
    #close CANoe
    def close_Canoe(self):
        wait(5)
        self.canoe_inst.quit()
        
