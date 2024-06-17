import time
import subprocess
import cv2
import win32gui
import pyautogui
import pygetwindow as gw
from xmlrpc.server import SimpleXMLRPCServer
from pynput.keyboard import Key, Controller
import Functions.Functions1 as Functions1
import Functions.Functions2 as Functions2
import Functions.Functions3 as Functions3
import Functions.Functions4 as Functions4




def set_window_text(hwnd, text):
    win32gui.SetWindowText(hwnd, text)

def rename_tabs(Tab_name):
    hwnd_list = []
    win32gui.EnumWindows(lambda hwnd, lParam: lParam.append(hwnd) if win32gui.GetWindowText(hwnd).startswith(Tab_name) else True, hwnd_list)

    # Rename each window to a unique name
    for i, hwnd in enumerate(hwnd_list, start=1):
        new_tab_name = str(i)
        set_window_text(hwnd, new_tab_name + "Roblox")
        print(f"Tab for window starting with '{Tab_name}' ({hwnd}) renamed to '{new_tab_name}'")

def StartProccsess(BrowserPath, BrowserName, Game):
    print("Starting Firefox subprocess")
    StartProccsess = subprocess.Popen([BrowserPath, Game])

    time.sleep(5)

    window = gw.getWindowsWithTitle(BrowserName)[0]
    window.maximize()
    window.activate()
    time.sleep(2)

    button_image_path = "image.png"
    print("Loading button image")
    button_image = cv2.imread(button_image_path)
  
    button_image_path = "image.png"
    print("Loading button image")
    button_image = cv2.imread(button_image_path)

    while True:
      screen_width, screen_height = pyautogui.size()
      region = (0, 0, screen_width, screen_height)

      time.sleep(1)

      print("Searching for the button image on the screen")
      try:
        button_location = pyautogui.locateOnScreen(button_image_path, region=region, confidence=0.8)

        if button_location:
            button_center_x, button_center_y = pyautogui.center(button_location)
            print(f"Button found at ({button_center_x}, {button_center_y})")

            pyautogui.moveTo(button_center_x, button_center_y)
            pyautogui.click()
            print("Button clicked. Stopping the loop.")
            break  # Stop the loop once the button is found and clicked
        else:
            print("Button not found on the screen")
      except pyautogui.ImageNotFoundException:
          print("Button image not found. Retrying...")

def StartProccsess_Friend(BrowserPath, BrowserName, Friend):
    print("Starting Firefox subprocess")
    StartProccsess = subprocess.Popen([BrowserPath, Friend])

    time.sleep(10)

    window = gw.getWindowsWithTitle(BrowserName)[0]
    window.maximize()
    window.activate()
    time.sleep(2)

    button_image_path = "join.png"
    print("Loading button image")
    button_image = cv2.imread(button_image_path)
  
    button_image_path = "join.png"
    print("Loading button image")
    button_image = cv2.imread(button_image_path)

    while True:
      window.maximize()
      window.activate
      screen_width, screen_height = pyautogui.size()
      region = (0, 0, screen_width, screen_height)

      time.sleep(1)

      print("Searching for the button image on the screen")
      try:
        button_location = pyautogui.locateOnScreen(button_image_path, region=region, confidence=0.8)

        if button_location:
            button_center_x, button_center_y = pyautogui.center(button_location)
            print(f"Button found at ({button_center_x}, {button_center_y})")

            pyautogui.moveTo(button_center_x, button_center_y)
            pyautogui.click()
            print("Button clicked. Stopping the loop.")
            break  # Stop the loop once the button is found and clicked
        else:
            print("Button not found on the screen")
      except pyautogui.ImageNotFoundException:
          print("Button image not found. Retrying...")


    
def is_roblox_player_open():
    roblox_player_window = gw.getWindowsWithTitle('Roblox')
    is_open = len(roblox_player_window) > 0
    print(f"Is Roblox player open? {is_open}")
    return is_open


variable_value = "Your behavior is briefly being monitored under the Monitoring Program. To opt--out please contact Get prize. (get prize 769) via e-mail or Roblox messages."

keyboard = Controller()
server = SimpleXMLRPCServer(('0.0.0.0', 8150), allow_none=True)

Tab_name = 'Roblox'
tab = "placeholder"
server.register_function(Functions1.type_and_enter_1, 'chat')
server.register_function(Functions2.type_and_enter_2, 'chat2')
server.register_function(Functions3.type_and_enter_3, 'chat3')
server.register_function(Functions4.type_and_enter_4, 'chat4')
server.register_function(Functions1.w, 'w')
server.register_function(Functions1.s, 's')
server.register_function(Functions1.a, 'a')
server.register_function(Functions1.d, 'd')
server.register_function(Functions2.w_2, 'w2')
server.register_function(Functions2.s_2, 's2')
server.register_function(Functions2.a_2, 'a2')
server.register_function(Functions2.d_2, 'd2')
server.register_function(Functions3.w_3, 'w3')
server.register_function(Functions3.s_3, 's3')
server.register_function(Functions3.a_3, 'a3')
server.register_function(Functions3.d_3, 'd3')
server.register_function(Functions4.a_4, 'a4')
server.register_function(Functions4.d_4, 'd4')
server.register_function(Functions4.w_4, 'w4')
server.register_function(Functions4.s_4,'s4')









#start browsers
StartProccsess("C:\\Program Files\\Mozilla Firefox\\firefox.exe", "FireFoxRoblox", "https://www.roblox.com/games/168556275/Baseplate")
time.sleep(15)
StartProccsess_Friend("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "no", "https://www.roblox.com/users/5433026171/profile")
time.sleep(5)
StartProccsess_Friend("C:\\Users\\evana\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe", "VivaldiRoblox", "https://www.roblox.com/users/5433026171/profile")
time.sleep(5)
StartProccsess_Friend("C:\\Program Files (x86)\Microsoft\\Edge\\Application\\msedge.exe", "Edge", "https://www.roblox.com/users/5433026171/profile")
time.sleep(15)
rename_tabs(Tab_name)

print("Server is now serving forever")

server.serve_forever()
#while True:
    #print("performing to type and enter") 
    #type_and_enter(variable_value)
    #time.sleep(5)