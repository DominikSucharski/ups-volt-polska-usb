# ups-volt-polska-usb

Tested with [MICRO UPS 1200 2x7Ah](https://voltpolska.pl/zasilanie-awaryjne/micro-ups-1200-2x7ah-720-1200w-komputerowy-zasilacz-awaryjny.html)

## Instruction for windows

1. Download [hidapi](https://github.com/libusb/hidapi/releases)
2. Extract the archive
3. Copy the hidapi.dll and hidapi.lib files to the C:\Windows\System32 folder
4. Install python ([Python 3.10](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5))
5. Run **pip install hid** in powershell
6. Go to the folder with the ups_volt_polska.py file
7. Run **python .\ups_volt_polska.py** in powershell

Result:
```
PS E:\git\ups-volt-polska-usb> python .\ups_volt_polska.py
Connecting to the UPS via USB ...
b'\\\\?\\HID#VID_0001&PID_0000#6&xxxx
Mode: AC
Input:   220.1 V
Output:  220.1 V
Power:   008 %
Battery: 27.1 V / 27.1V
State of charge: 4/4
about    127.6 %
flags:   00001001
```
