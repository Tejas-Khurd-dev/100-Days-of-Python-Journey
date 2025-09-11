enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

player_health = 10

def game():
    def potion():
        potion_strength = 2
        print(player_health)

    potion()
game()
