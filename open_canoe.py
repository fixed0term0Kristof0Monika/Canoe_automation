from py_canoe import CANoe
from time import sleep as wait

canoe_inst = CANoe()

# open CANoe configuration. Replace canoe_cfg with yours.
canoe_inst.open(canoe_cfg=r'C:/Users/Public\Documents/Vector/CANoe\Sample Configurations 16.2.55/CAN/Easy/Easy.cfg')

# print installed CANoe application version
canoe_inst.get_canoe_version_info()

wait(5)
# Start CANoe measurement
canoe_inst.start_measurement()
wait(5)
canoe_inst.set_signal_value('CAN', 1, 'LightState', 'FlashLight', 5)
 
wait(5)
# get signal value. Replace arguments with your message and signal data.
sig_val = canoe_inst.get_signal_value('CAN', 1, 'LightState', 'FlashLight')
print(sig_val)

wait(5)

# Stop CANoe Measurement
canoe_inst.stop_measurement()

wait(5)
# Quit / Close CANoe configuration
canoe_inst.quit()
