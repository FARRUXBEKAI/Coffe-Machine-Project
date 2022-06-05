#!/usr/bin/env python
# coding: utf-8

# # 5/06/2022
# 
# # Python asoslari
# 
# # Coffee Machine Project
# 
# # Muallif: Farrux Sotivoldiyev

# * Bu project asosan lug'at bilan ishlashga qaratilgan.

# In[1]:


# COFFE MACHINE

import time

base = {
    "water" : 1000,
    "milk" : 1100,
    "coffee" : 50,
    "cream" : 75,
    "money" : 100
}

ingredients = {
    "cappuccino" : {
        "water" : 100,  
        "milk" : 100,
        "coffee" : 5
    },
    
    "espresso" : {
        "water" : 75,
        "milk" : 100,
        "coffee" : 7,
        "cream" : 25
    },

    "latte" : {             
        "milk" : 180,    
        "coffee" : 5
    }
}

money = {
    "half" : 0.5,
    "one" : 1,
    "five" : 5,
    "ten" : 10
}

coins = {
    "half" : 10,
    "one" : 10,
    "five" : 7,
    "ten" : 5
}

price = {
    "espresso" : 2.5,
    "latte" : 2,
    "cappuccino" : 4.5
}

# coffee making time
def stopwatch(seconds):
                while seconds:
                    mins, secs = divmod(seconds, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins,secs)
                    print(timeformat,end='\r')
                    time.sleep(1)
                    seconds -= 1
                print(f"Your coffee is ready. Enjoy!")

# menu 
def menu():
    print("Menu : ")
    for i,j in price.items():
        print(f"{i.capitalize()} : {j} $")
    return input("Choose coffee (espresso/latte/cappuccino) : ").lower()

# money size
def money_size():
    print("Please deposit money in these units:")
    for i,j in money.items():
        print(f"{i.capitalize()} : {j} $")

# money back
def money_back(y,x,t=0):
    y -= price[x]
    t = y
    # 10$
    ten1,five1,one1,half1 = 0,0,0,0
    while y >= money["ten"] and coins["ten"] > 0:
        coins["ten"] -= 1
        ten1 += 1
        y -= 10
    # 5$
    while y >= money["five"] and coins["five"] > 0:
        coins["five"] -= 1
        five1 += 1
        y -= 5
    # 1$
    while y >= money["one"] and coins["one"] > 0:
        coins["one"] -= 1
        one1 += 1
        y -= 1
    # 0.5$
    while y >= money["half"] and coins["half"] > 0:
        coins["half"] -= 1
        half1 += 1
        y -= 0.5
    
    if y == 0:
        base["money"] += price[x]
        return f"Your return: 0.5$->{half1}🪙  1$->{one1}🪙  5$->{five1}🪙  10$->{ten1}🪙"

    else:
        if "n"==input(f"Do you agree we can give you {t-y}$ ? y/n: "):
            coins["ten"] += ten1
            coins["five"] += five1
            coins["one"] += one1
            coins["half"] += half1
            
            return 0
        else:
            base["money"] -= (price[x]+ y)
            return "ok"

# sorting money
def sorting_money(coins1):
    for i in coins1:
        if i==0.5:
            coins["half"] += 1 
        elif i==1:
            coins["one"] += 1
        elif i==5:
            coins["five"] += 1
        else: 
            coins["ten"] += 1

print("     COFFE\n   CHarge Up\n")

# main
def main():
    while True:
        # get money
        count = 0
        y = 1
        while y != 0:
            x = menu()
            y = len(ingredients[x])
            for i in ingredients[x]:
                if ingredients[x][i] <= base[i]:
                    base[i]-= ingredients[x][i]
                    y -= 1
            if count==2:
                return "Coffee is over or log in again!!!"
            elif y != 0:
                count += 1
                print(f"{x.upper()} is over, choose a different type of coffee!")
        else:   
                print(f"{price[x]} $ from you")
                money_size()
                
                # add money
                coins1 = []
                y = float(input(">>> "))
                coins1.append(y)
                while price[x] > y:
                    p = float(input(">>> "))
                    coins1.append(p)
                    y += p

                # money back
                l = money_back(y,x)

                # sorting money
                sorting_money(coins1)
                if l:
                    print(l)
                    print("Your coffee will be ready in 60 seconds ...")
                    stopwatch(60)

        if "n"==input("Would you like more coffee? y/n: "):
            print(f"Database information:{base}")
            print("Thank you for choosing us!")
            break

main()

