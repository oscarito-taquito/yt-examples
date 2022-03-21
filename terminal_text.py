from modules.text_colors import TextColors

t = TextColors

while True:
    val  = input("Enter an integer: ")

    if val == 'exit':
        break

    if val.isdigit():
        print(f"{t.green}{val} is a integer!{t.end}")
    else:
        print(f"{t.red}{t.bold}'{val}' is NOT an integer.{t.end}")
