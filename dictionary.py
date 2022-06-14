nations = {"USA": "Washington DC",
           "Japan": "Tokyo",
           "Nigeria": "Lagos",
           "Togo": "Lome",
           }

nations.pop("Togo")
# nations.clear()
nations.keys()

# print(nations.keys())
print(nations.values())
print(nations.items())

for i in nations:
    print(i, end=" ")
