from User import UserConfig
from User import UserInteract
import server_interact


def main():
    user_interact = UserInteract.UserInteract()
    user_interact.input_config()
    user_interact.output()

    user_interact.input_channel_info()
    serv_interact = server_interact.ServerInteract(user_interact)
    serv_interact.connect()

    cmd = input()

    while True:
        match cmd:
            case "JOIN":
                serv_interact.join_channel()


if __name__ == '__main__':
    main()
