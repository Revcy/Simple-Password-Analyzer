passwd_mark, quit_prompt = 0, ''

print('', 'Problems:', sep='\n')

while True:
    
    passwd = input('Enter your password for analysis: ')
    
    if ' ' in passwd:
        print("Your password have a space(-s). I think password can be without space(-s)")
        break
    elif passwd.isspace():
        print("Your password is empty")
        break

    if passwd.isalnum() and not(passwd.isdigit()) and not(passwd.isalpha()):
        print("Your input password have letters and digits, but doesn't have any char as _ * ")
        passwd_mark = 1
    else:
        passwd_mark = 1.5

    if passwd.isalpha() and passwd.islower():
        print("Your input password have only lower letters, but doesn't have digits")
        passwd_mark = 0.1
    elif passwd.isalpha() and passwd.isupper():
        print("Your input password have only upper letters, but doesn't digits")
        passwd_mark = 0.1
    elif passwd.isalpha():
        print("Your input password have only letters, but doesn't have digits")
        passwd_mark = 0.5

    if passwd.isdigit():
        print("Your input password have only digits, but doesn't have letters")
        passwd_mark = 0.5

    if passwd_mark == 1.5:
        print('Problems not found', '', 'Analysis: Very good password', sep='\n')
    elif passwd_mark == 1:
        print('', 'Analysis: Good password', sep='\n')
    elif passwd_mark == 0.5:
        print('', 'Analysis: Normal password', sep='\n')
    else:
        print('', 'Analysis: Bad password', sep='\n')

    print('')
    quit_prompt = input("You wanna quit (Yes[Да], No[Нет])? ").lower().strip()

    if quit_prompt == 'yes' or quit_prompt == 'да':
        break
    elif quit_prompt == 'no' or quit_prompt == 'нет':
        print('')
    else:
        print('Unknown input. Try again')
        print('')
        quit_prompt = input("You wanna quit (Yes[Да], No[Нет])? ").lower().strip()
