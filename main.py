from User import UserConfig
from User import UserInteract
import server_interact
import threading

cmd = ""

def main():
    user_interact = UserInteract.UserInteract()
    user_interact.input_config()
    user_interact.output()

    user_interact.input_channel_info()
    serv_interact = server_interact.ServerInteract(user_interact.config)
    serv_interact.connect()
   # serv_interact.set_username()
    serv_interact.set_nickname(user_interact.nickname)
    signal = True
    def input1():
        while True:
            cmd = input()
            match cmd:#PONG, TOPIC, NAMES
                case "JOIN":
                    serv_interact.join_channel(user_interact.channel_name)
                case "SS":
                    print("Hi")
                case "USER":
                    serv_interact.set_username("Albert Korobit")
                case "CHNGNICK":
                    user_interact.change_nick()
                    serv_interact.set_nickname(user_interact.nickname)
                case "CHNGCHANNEL":
                    user_interact.change_channel()
                    serv_interact.join_channel(user_interact.channel_name)
                case "HELP":
                    print("THATS HELP, LOOK IN THE CODE")
                case "PRIVMSG":
                    serv_interact.write_private_msg()
                case "QUIT":
                    serv_interact.quit()
                    serv_interact.sock.close()
                    signal = False
                    break
                case "WRITE":
                    command = input("Write command:")
                    arg = input("Write argument:")
                    serv_interact.send_to_server(command, arg)
                case "":
                    print("Print \"HELP\"")

    def output():
        while signal:
            flag = True
            while flag:
                try:
                    data = serv_interact.get_response().decode()
                    print(data)
                    if "PING" in data:
                        serv_interact.send_to_server("PONG", ":" + data.split(":")[1])
                except TimeoutError:
                    flag = False

    th2 = threading.Thread(target=output, daemon=True)
    th1 = threading.Thread(target=input1)
    th1.start()
    th2.start()


if __name__ == '__main__':
    main()
