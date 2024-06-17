import xmlrpc.client
import time
server_url = 'http://10.4.9.69:8150/'
proxy = xmlrpc.client.ServerProxy(server_url, allow_none=True)




def chat(variable_value):
    proxy.chat(variable_value)

def chat2(variable_value):
    proxy.chat2(variable_value)

def chat3(variable_value):
    proxy.chat3(variable_value)

def chat4(variable_value):
    proxy.chat4(variable_value)


def process_line(line):
    if line.startswith("all w"):
        proxy.w()
        proxy.w2()
        proxy.w3()
        proxy.w4()
    elif line.startswith("all a"):
        proxy.a()
        proxy.a2()
        proxy.a3()
        proxy.a4()
    elif line.startswith("all d"):
        proxy.d()
        proxy.d2()
        proxy.d3()
        proxy.d4()
    elif line.startswith("all s"):
        proxy.s()
        proxy.s2()
        proxy.s3()
        proxy.s4()
    elif line.startswith("all chat:"):
        variable_value = line.split(":", 1)[1].strip()  # Extract the value after "all chat:"
        proxy.chat(variable_value)
        time.sleep(1)
        proxy.chat2(variable_value)
        time.sleep(1)
        proxy.chat3(variable_value)
        time.sleep(1)
        proxy.chat4(variable_value)
    elif line.strip() == "w":
        proxy.w()
    elif line.strip() == "a":
        proxy.a()
    elif line.strip() == "d":
        proxy.d()
    elif line.strip() == "s":
        proxy.s()
    elif "chat" in line:
        variable_value = line.split(":")[1]
        chat(variable_value)
    elif "chat2" in line:
        variable_value = line.split(":")[1]
        chat2(variable_value)
    elif "chat3" in line:
        variable_value = line.split(":")[1]
        chat3(variable_value)
    elif line.strip() == "w2":
        proxy.w2()
    elif line.strip() == "a2":
        proxy.a2()
    elif line.strip() == "d2":
        proxy.d2()
    elif line.strip() == "s2":
        proxy.s2()
    elif line.strip() == "w3":
        proxy.w3()
    elif line.strip() == "a3":
        proxy.a3()
    elif line.strip() == "d3":
        proxy.d3()
    elif line.strip() == "s3":
        proxy.s3()
    elif line.strip() == "d4":
        proxy.d4()
    elif line.strip() == "a4":
        proxy.a4()
    elif line.strip() == "w4":
        proxy.w4()
    elif line.strip() == "s4":
        proxy.s4()
    elif line.strip() == "chat4":
        variable_value = line.split(":")[1]
        chat4(variable_value)

    

    


def send_command(command):
    try:
        # Send the command to the server and get the response
        response = proxy.handle_command(command)

        # Print the response from the server
        print("Server Response:", response)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    while True:
        # Get input command from the user
        command = input("Enter command (w, a, s, d, chat:message): ").lower()

        # Exit the loop if the command is 'exit'
        if command == 'exit':
            break

        try:
            if command == "all w":
                proxy.w()
                proxy.w2()
                proxy.w3()
                proxy.w4()
            elif command == "all a":
                proxy.a()
                proxy.a2()
                proxy.a3()
                proxy.a4()
            elif command == "all d":
                proxy.d()
                proxy.d2()
                proxy.d3()
                proxy.d4()
            elif command == "all s":
                proxy.s()
                proxy.s2()
                proxy.s3()
                proxy.s4()
            elif command.startswith("all chat:"):
              variable_value = command.split(":", 1)[1].strip()  # Extract the value after "all chat:"
              proxy.chat(variable_value)
              time.sleep(1.5)
              proxy.chat2(variable_value)
              time.sleep(1.5)
              proxy.chat3(variable_value)
              time.sleep(1.5)
              proxy.chat4(variable_value)
            elif command.startswith("chat:"):
              variable_value = command.split(":")[1]
              proxy.chat(variable_value)
            elif command.startswith("chat2:"):
             variable_value = command.split(":")[1]
             proxy.chat2(variable_value)
            elif command.startswith("chat3:"):
             variable_value = command.split(":")[1]
             proxy.chat3(variable_value)
            elif command.startswith("chat4:"):
               variable_value = command.split(":")[1]
               proxy.chat4(variable_value)
            elif command == "w":
                proxy.w()
            elif command == "w2":
                proxy.w2()
            elif command == "w3":
                proxy.w3()
            elif command == "s":
                proxy.s()
            elif command == "s2":
                proxy.s2()
            elif command == "s3":
                proxy.s3()
            elif command == "d":
                proxy.d()
            elif command == "d2":
                proxy.d2()
            elif command == "d3":
                proxy.d3()
            elif command == "a":
                proxy.a()
            elif command == "a2":
                proxy.a2()
            elif command == "a3":
                proxy.a3()
            elif command == "a4":
                proxy.a4()
            elif command == "d4":
                proxy.d4()
            elif command == "w4":
                proxy.w4()
            elif command == "s4":
                proxy.s4()
            elif command == "exit":
                break
            elif command.endswith(".txt"):
                with open(command) as f:
                    for line in f:
                        process_line(line)
            else:
                print("Invalid command. Please enter a valid command.")
        except Exception as e:
            print("An error occurred:", str(e))