import hid

def main():
    # Config Start
    VENDOR_ID = 0x0001
    PRODUCT_ID = 0x0000
    BATT_V_MAX = 2 * 12.89 # 2 x 12V AGM battery https://footprinthero.com/lead-acid-battery-voltage-charts
    BATT_V_MIN = 21.0
    # Config End
    print("Connecting to the UPS via USB ...")
    device_list = hid.enumerate(VENDOR_ID, PRODUCT_ID)
    for device_item in device_list:
        # connect to device and get data
        print(device_item['path'])
        device = hid.Device(path=device_item['path'])
        device_params = device.get_indexed_string(3).split()
        device.close()
        if not device_params or len(device_params) < 8:
            print("Can't connect to device. Expected 8 parameters from UPS")
            print("device params:", device_params)
            break
        # mode
        if device_params[7][0] == "1":
            print("Mode: battery")
        else:
            print("Mode: AC")
        print("Input:\t", device_params[0].replace("(", ""), "V")
        # print("Unknown:", device_params[1])
        print("Output:\t", device_params[2], "V")
        print("Power:\t", device_params[3], "%")
        # print("Unknown:", device_params[4])
        battery_vol = float(device_params[5])
        print("Battery:", battery_vol, "V / 27.1V")
        if device_params[7][1] == "1":
            print("Warning - Low Battery !!!")
        if battery_vol >= 25.0:
            print("State of charge: 4/4")
        elif battery_vol >= 23.0: # exact value determined experimentally
            print("State of charge: 3/4")
        elif battery_vol >= 22.0: # exact value determined experimentally
            print("State of charge: 2/4")
        else:
            print("State of charge: 1/4 or less")
        print("about\t", round((battery_vol - BATT_V_MIN) / (BATT_V_MAX - BATT_V_MIN) * 100, 1), "%")
        # print("unknown:", device_params[6])
        print("flags:\t", device_params[7])
 
if __name__ == "__main__":
    main()
        
# device_params[7]:
# 00001001 - AC mode
# 10001001 - battery mode
# 11001001 - Low Battery
