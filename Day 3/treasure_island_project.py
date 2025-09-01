print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ / 
*******************************************************************************
''')

print("🏝️ Welcome to **Treasure Island**! 🏝️")
print("✨ Your mission is simple but daring: **Find the hidden treasure!** ✨")

cross_road = input("\nYou’re at a crossroad. Do you want to go **Left** ⬅️ or **Right** ➡️ ?\n").lower()

if cross_road == "left":
    print("\n🌊 You’ve reached a mysterious lake. "
          "There’s an island in the middle... 🏝️")

    choice = input("Do you want to 🚤 **'wait'** for a boat or 🏊 **'swim'** across?\n").lower()

    if choice == "wait":
        print("\n⛵ The boat takes you safely to the island! Phew! 🙌")
        print("\n🏠 You see a house with **3 magical doors**: 🚪 Red, 🚪 Blue, 🚪 Yellow.")
        door = input("Which one will you choose? (red/blue/yellow)\n").lower()

        if door == "red":
            print("\n🔥 The room bursts into flames! You got roasted! Game Over 💀")
        elif door == "blue":
            print("\n🦍 Beasts jump out and devour you! Game Over 💀")
        elif door == "yellow":
            print("\n🎉 The door creaks open... and inside lies a trunk of treasure! 🪙💎✨")
            print("🏆 Congratulations, **YOU WIN!** 🎊")
        else:
            print("\n🤔 That’s not even a door… Game Over 💀")

    elif choice == "swim":
        print("\n🦈 Uh-oh! Sharks circle around you… SNAP! Game Over 💀")
    else:
        print("😵 Wrong choice… Game Over.")

elif cross_road == "right":
    print("\n🕳️ Oh no! You fall into a deep hole. Game Over 💀")

else:
    print("\n🤷 Incorrect choice… The jungle consumes you. Game Over 💀")

