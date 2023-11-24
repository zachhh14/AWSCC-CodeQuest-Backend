import json
import os

options = {
    1 : 'Create Account',
    2 : 'View Account',
    3 : 'Search Account',
    4 : 'Edit Account',
    5 : 'Delete Account',
    6 : 'Exit',
}
    
link = './submissions/mini-project-02/data.json'

def show_options():
    for option in options:
        print(f'{option} - {options[option]}')

def get_accounts(website = None):
    with open(link, 'r') as f: 
        websites = json.load(f)

    if not website: 
        return websites
    
    if website not in websites:
        print("Website doesn't exists.")
        quit()
    
    return websites[website]
    
def add_account():
    print('Create Account')
    website = input('Enter name of website: ')
    id = 1
    email = input('Enter email: ')
    password = input('Enter password: ')

    request = {
        website: [{
            'id': id,
            'email': email,
            'password': hash(password), # hashing of password
        }]
    }

    accounts = get_accounts()

    if website in accounts:
        id = len(accounts[website]) + 1
        print(len(accounts[website]))
        accounts[website].append({
            'id': id, 
            'email': email, 
            'password': hash(password)
            })
    else:
        accounts.update(request)

    with open(link, 'w') as f:
        json.dump(accounts, f, indent=4)    
    
    os.system('cls')
    print('success, 200')


def view_accounts():
    websites = get_accounts()

    os.system('cls')

    for website in websites:
        print(f'Website: {website}')
        for account in websites[website]:
            print(f'\tID: {account['id']}')
            print(f'\tEmail: {account['email']}')
            print(f'\tPassword: {account['password']}')
            print()

def search_account():
    os.system('cls')
    print('Search Account')

    with open(link, 'r') as f:
        websites = json.load(f)

    print('Websites: ')
    for website in websites:
        print('- ',website)
    
    website_input = input('Which websites do you want to look? ')
    accounts = get_accounts(website_input)

    email_input = input('Input email: ')

    os.system('cls')
    for account in accounts:
        if(account['email'] == email_input):
            print(f'WEBSITE: {website_input}')
            print(f'\tID: {account['id']}')
            print(f'\tEmail: {account['email']}')
            print(f'\tPassword: {account['password']}')
            quit()

    print('There is no existing email in the system.')

def update_account():
    print('Edit Account')
    websites = get_accounts()
    print(f'Website:')
    for website in websites:
        print(f'{website}')

    website_input = input('Enter website:')

    accounts = get_accounts(website_input)

    for account in accounts:
        print(f'ID: {account['id']} Email: {account['email']}')
        print(f'      Password: {account['password']}')
    
    id = int(input('Enter the id you want to edit: ')) - 1

    field = input("'email' or 'password: ")
    
    field_new_value = input(f'Enter new {field}: ')
    
    if field == 'password':
        field_new_value = hash(field_new_value)

    websites[website_input][id][field] = field_new_value

    with open(link, 'w') as f:
        json.dump(websites, f, indent=4)

    print('success, 201')

    
def delete_account():
    websites = get_accounts()
    website_input = input('Enter website: ')

    accounts = get_accounts(website_input)
    
    for account in accounts:
        print(f'ID: {account['id']} Email: {account['email']}')
        print(f'      Password: {account['password']}')

    
    id = int(input('Enter the id you want to delete: ')) - 1
    websites[website_input].pop(id)

    if len(websites[website_input]) == 0:
        websites.pop(website_input)

    with open(link, 'w') as f:
        json.dump(websites, f, indent=4)
        
def check_input(choice):
    if choice not in options:
        print('Invalid input')
    if choice == 1:
        add_account()
    if choice == 2:
        view_accounts()
    if choice == 3:
        search_account()
    if choice == 4:
        update_account()
    if choice == 5:
        delete_account()
    

def main_menu():
    os.system('cls')
    print('Welcome to Password Manager App')
    show_options()
    input_option = int(input('What do you want to do?: '))
    check_input(input_option)

main_menu()



    