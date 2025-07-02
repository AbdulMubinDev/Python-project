def add():
    print("Let's product add product....")
    while True:
        product =  input("Which product you want add in our store [Fruite] [vegetable] [Meat]: ")


def main():
    print("Welcome To Our Store 😊")

    while True:
        action_choise = input("Which action you like to do [Buy] or [Add]: ").lower()
        if action_choise in ['buy', 'add']:
            if action_choise == 'add':
                break
            elif action_choise == 'buy':
                break
        else:
            print(f'you {action_choise} action was not valid, Please chose between this two action [Buy] or [Add] ')


if __name__ == '__main__':
    main()