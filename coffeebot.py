
orders = []
def coffee_bot():
    welcome_message()
    order_taking(orders)
    receipt(orders)

    name = input("\nVad heter du? ")

    print("\nTack, {}! Fortsätt till Upphämtning för din beställning!".format(name))

#Welcome Message, called in main function
def welcome_message():
    print("Välkommen till Kahls! \n\nMånadens specialerbjudanden är La Orquidea Micro-Lot och Impressionist Masterpiece Blend.")

#Order Taking, called in main function
def order_taking(orders):
    size = get_storlek()
    temp_type = get_temp()
    drink_type = get_drink_type()
    cup_type = get_cup()
    quantity = get_quantity()
    orders.append([quantity, size, temp_type, drink_type, cup_type])
    print("\n" + str(orders))
    print("\nAlright, that\'s {} {} {} {} {}!".format(quantity, size, temp_type, drink_type, cup_type))
    addon_prompt()

#For Additional Orders, called in Order Taking function
def addon_prompt():
    res = input("\nVill du lägga till en ny beställning? \n[a] Ja \n[b] Nej \n> ")
    res = res.lower()
    if res == "a":
        print("\nSuper! Tar din nya beställning!")
        return order_taking(orders)
    else:
        print("\nOkej, bearbetar dina beställningar nu!")

#Error Message, used for invalid input
def error_message():
    print("\nJag är ledsen. Jag förstår inte ditt val.\n\nVänligen ange motsvarande bokstav för ditt svar.")

#Order Summary, called in main function
def receipt(orders):
    total_orders = range(1, (len(orders)+1))
    print("\nDu har placerat " + str((len(orders))) + " order. Dina beställningar är: ")
    for order in orders:
        print(*order)

#Size Choice, called in Order Taking function
def get_storlek():
    res = input('\nVilken storlek vill du ha? \n[a] Liten \n[b] Medium \n[c] Stor \n> ')
    res = res.lower()
    if res == "a":
        return "Liten"
    elif res == "b":
        return "Medium"
    elif res == "c":
        return "Stor"
    else:
        error_message()
        return get_size()

#Drink Choice, called in Order Taking function
def get_drink_type():
    res = input("\nVilken typ av dryck vill du ha?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
    res = res.lower()
    if res == "a":
        return "Brewed Coffee"
    elif res == "b":
        return "Mocha"
    elif res == "c":
        return order_latte()
    else:
        error_message()
        return get_drink_type()

#Milk Component, called in Get_Drink_Type function
def order_latte():
    res = input("\nOch vilken typ av mjölk till din latte? \n[a] 2% mjölk \n[b] Non-fat mjölk \n[c] Soy mjölk \n> ")
    res = res.lower()
    if res == "a":
        return "Latte"
    elif res == "b":
        return "Non-fat Latte"
    elif res == "c":
        return "Soy Latte"
    else:
        error_message()
        return order_latte()

#Temp Choice, called in Order Taking function
def get_temp():
    res = input("\nVarm eller Iced? \n[a] Varm \n[b] Iced \n> ")
    res = res.lower()
    if res == "a":
        return "Varm"
    elif res == "b":
        return "Iced"
    else:
        error_message()
        return get_temp()

#Cup choice, called in Order Taking function
def get_cup():
    res = input("\nVilken typ av kopp vill du använda?\n[a] Dine-in Kopp \n[b] Takeaway Kopp \n[c] Din egen Återanvändbar Kopp \n> ")
    res = res.lower()
    if res == "a":
        return "i en dine-in kopp"
    elif res == "b":
        return "i en takeaway kopp."
    elif res == "c":
        return "i din egen återanvändbar kopp."
    else:
        error_message()
        return get_cup()

#Quantity choice, called in Order Taking function
def get_quantity():
    res = input("\nVad är kvantitet för denna beställning? > ")
    try:
        res = int(res)
        return res
    except ValueError:
        print("\nOops, felaktig input. Ange en värdemängd.")
        return get_quantity()

coffee_bot()
