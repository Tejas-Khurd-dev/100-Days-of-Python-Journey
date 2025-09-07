travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
    "countries_to_visit" : {
        "India" : "Mumbai",
        "Switzerland" :  "Zermatt",
        "USA" : "Florida"
    }
}
print("***Nested Dictionary***")
print(travel_log)
print(travel_log["France"])
print(travel_log["France"][1])
print(travel_log["countries_to_visit"])
print(travel_log["countries_to_visit"]["India"], "\n")

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2], "\n")

print("***Nested List***")
nested_list = ["A", "B", ["C", "D"]]

print(nested_list)
print(nested_list[2])
print(nested_list[2][1])

