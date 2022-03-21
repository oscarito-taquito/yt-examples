from modules.text_colors import TextColors

t = TextColors

while True:
    val = input("Enter an integer: ")
    if val == 'exit':
        break

    if val.strip().isdigit():
        print(f"{t.green}{val} is an integer!{t.end}")
    else:
        print(f"{t.red}{t.inverse}'{val}' is not an integer!{t.end}")
