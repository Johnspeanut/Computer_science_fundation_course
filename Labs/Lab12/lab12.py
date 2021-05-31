def generate_networ_dic(filename):
    '''
    Function -- def generate_networ_dic
        Create network dictionary based on txt file
    Parameter:
        filename -- filename that stores network information. With ".txt" extension.
    Returns:
        Dictionary that illustrates the network.
    '''
    dic = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line_new = line.strip()
                line_elements = line_new.split(" ")
                dic[line_elements[0]] = line_elements[1:]
        return dic
    except (FileNotFoundError, IOError):
        print("Wrong file or file path")


def write_dic_to_file(filename, dic):
    '''
    Function -- write_dic_to_file
        Write dictionary to .txt file
    Parameter:
        filename -- .txt format filename
        dic -- Dictionary with dwarve name as a key and his friends are in a list,which serve as value.
    '''
    with open(filename, 'w') as file:
        for key, value in dic.items():
            line = key
            for item in value:
                line += " " + item
            file.write(line + "\n")


def main():
    dic = generate_networ_dic("dwarves.txt")
    dwarve = input("Which of the 7 dwarves is logging in? ")
    run = True
    while run:
        choice = input("Choose from one of the options below:\nP: Print your friends list\nU <name>: Unfriend someone\nF <name>: Friend someone\nQ: Quit")
        choice_elements = choice.split(" ")
        if choice_elements[0] == "P":
            friend_lst = dic[dwarve]
            msg = "Your friends: "
            for item in friend_lst:
                item += ", "
                msg += item
            msg = msg[:-2]
            print(msg)
        elif choice_elements[0] == "U":
            friend_list = dic[dwarve]
            if choice_elements[1] == "everyone":
                friend_list = []
                print("Everyone is not your friend")
            elif choice_elements[1] in friend_list:
                friend_list.remove(choice_elements[1])
                print(choice_elements[1] + " has been unfriended")
            else:
                print("Please specify who you gonna unfriend")
            dic[dwarve] = friend_list
        elif choice_elements[0] == "F":
            friend_list = dic[dwarve]
            friend_list.append(choice_elements[1])
            dic[dwarve] = friend_list
        elif choice_elements[0] == "Q":
            write_dic_to_file("dwarves.txt",dic)
            run = False
        else:
            print("Please enter the correct option")


main()