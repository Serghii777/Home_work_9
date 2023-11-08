def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

@input_error
def add_handler(name, phone, contacts):
    contacts[name] = phone
    return f"Contact '{name}' with phone number '{phone}' added successfully."

@input_error
def change_handler(name, phone, contacts):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for contact '{name}' changed to '{phone}'."
    else:
        raise KeyError(f"Contact '{name}' not found.")

@input_error    
def phone_handler(name, contacts):
    if name in contacts:
        return f"The phone number for '{name}' is '{contacts[name]}'."
    else:
        raise KeyError(f"Contact '{name}' not found.")

@input_error    
def show_all_handler(contacts):
    if contacts:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "No contacts found."
    
def exit_handler():
    return print("Good bye!")

def hello_handler():
    return 'Hello, how can I help you?'

@input_error    
def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").lower()
        if command.startswith("add"):
            _, name, phone = command.split()
            result = add_handler(name, phone, contacts)
        elif command.startswith("change"):
            _, name, phone = command.split()
            result = change_handler(name, phone, contacts)
        elif command.startswith("phone"):
            _, name = command.split()
            result = phone_handler(name, contacts)
        elif command == "show all":
            result = show_all_handler(contacts)
        elif command in ["good bye", "close", "exit"]:
            result = exit_handler()
            break
        elif command == "hello":
            result = hello_handler()
        else:
            result = "Invalid command. Please try again."
        print(result)  
 
if __name__ == "__main__":
    main()