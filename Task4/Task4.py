


def show_phone(args, contacts):
    if len(args) != 1:
        return "Oops, try again"
    name = args[0]

    if name not in contacts:
        return "Name doesn't exist"

    return contacts[name]


def change_contact(args, contacts):
    if len(args) != 2:
        return "Oops, try again"
    
    name, phone = args
    contacts[name] = phone

    return "Contact updated."


def parse_input(user_input):
    if user_input == '':
        return '', []


    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args
    
    

def add_contact(args, contacts):
    if len(args) != 2:
        return "Oops, try again"
        
    name, phone = args
    contacts[name] = phone

    return "Contact added."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
            

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == 'all':
            print(contacts)
        elif command == '':
            print('Invalid command.')
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
