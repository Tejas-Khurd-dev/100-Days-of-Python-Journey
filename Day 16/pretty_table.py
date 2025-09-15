from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmainder", "Gastly"])
table.add_column("Type", ["Electric", "Fire", "Ghost"])

print(table.align)
print(table)

table.align = "l"
print(table)
print(table.align)
