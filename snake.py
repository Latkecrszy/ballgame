tokenshop = [
    {"name": f"Auto Investor 1",
     "key": 1,
     "description:": f"Buys the next upgrade when available, toggle with eco!autobuy. (Note: Requires a 20% buffer.",
     "price": "stuff"},
    {"name": f"Auto Investor 1",
     "key": 2,
     "description": f"Buys the next upgrade when available, toggle with eco!autobuy. (Note: Requires a 20% buffer.",
    "price": "stuff"},
    {"name": f"Coupon Book 1",
     "price": "stuff",
     "description": f"Allows you to buy upgrades for 20% less."},
    {"name": "Pet Care 1", "price": 1,
     "description": "Will automatically feed your pet if you go 3 days without feeding them. Only works once a week."},
    {"name": "Pet Care 2", "price": 1,
     "description": "Your pets become more self-sufficent, and can go 4 days without eating."},
    {"name": "Pet Care 3", "price": 2, "description": "Earn double XP and money from fetch, dig, and play."},
    {"name": "Pet Care 4", "price": 2,
     "description": "Your pets learn to feed themselves. They no longer need to eat."},
    {"name": "Pet Care 5", "price": 3, "description": "Triple XP and money from fetch, dig, and play."}]
for item in tokenshop:
    available = 0
    name = item["name"]
    price = item["price"]
    print(item)
    if 'description' in item.keys():
        print(item['key'])
        print("it's here")
        print(item['description'])
        break
