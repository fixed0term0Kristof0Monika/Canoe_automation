from open_canoeobj import Canoe
from read_from_excel import extractFromExcel, openExcelFile

import keyboard

#todo exception for errors -done
# default values for functions -done
#read from files the values -done
#seat test  and UDSbasic diagnostic open
# browse window for config selection - done
#test reports with interface -friday
# read/write system variables -done


if __name__ == "__main__":
    mycanoe = Canoe()
    mycanoe.open_Canoe()  
    # mycanoe.str_measur()
    
    # print("Import from file? ")
    # imp_file= input(" Y or N: ").upper()
         
    # if(imp_file == "Y"):
    #     file = openExcelFile()
    #     channel = extractFromExcel(file,"B2")
    #     chanel_nr = extractFromExcel(file,"B3")
    #     message = extractFromExcel(file,"B4")
    #     signal = extractFromExcel(file,"B5")
    #     value = extractFromExcel(file,"B6")
    #     print("Values from Excel: ", channel, chanel_nr, message, signal, value)
    #     mycanoe.set_signal(message, signal, value, channel, chanel_nr)
    #     print("\tSignal after change")
    #     mycanoe.get_signal(message, signal, channel, chanel_nr)
    # else: 
    
    # mycanoe.set_signal("EngineState", "EngineSpeed", 1234)
    # print("\tSignal after change")
    # mycanoe.get_signal("EngineState", "EngineSpeed",)
    # #system variables    
    # print("Operating with system variables")
    # mycanoe.set_syst_signal("Engine::EngineSpeedDspMeter", 20)
    # mycanoe.get_syst_signal("Engine::EngineSpeedDspMeter")
    
    # #handle TestModes
    # print("Start/Stop test cases")
    # mycanoe.send_diagnostic("Door", "DefaultSession_Start", False)
    # mycanoe.send_diagnostic("Door", '10 02')
    
    # handle environment variables
    print("Change environment variables")
    variable = "Env_DoipConnectVeh"
    print(mycanoe.get_EnvVar(variable))
    
    #connectivity with ethernet
    mycanoe.Connect_DOIP(variable)
    print("Now REad_DTC")
    mycanoe.Read_DTC()
    
    
    print("Press s to stop measurements and quit")
        #press key to stop measurement \ close application
    keyboard.wait('s')
    mycanoe.stop_measur()
    mycanoe.close_Canoe()
   
 