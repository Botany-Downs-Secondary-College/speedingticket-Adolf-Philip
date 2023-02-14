warrant_list = {"John Doe": True, "Jane Doe": False, "Bob Smith": False}

ticket_list = []

while True:
  name = input("Enter the driver's name (or 'N' to quit): ")
  
  if name == "N":
    print("\nSummary Information:")
    print("Driver\tSpeed Over Limit\tFine\tTotal Fine")
    total_fine = 0
    for ticket in ticket_list:
      print("{}\t{}\t\t\t${}\t${}".format(ticket["name"], ticket["speed_over_limit"], ticket["fine"], ticket["fine"]))
      total_fine += ticket["fine"]
    print("\nTotal Fine: ${}".format(total_fine))
    break
  
  if name in warrant_list and warrant_list[name]:
    print("{}, Arrest Warrant!".format(name))
    continue

  speed_limit = int(input("Enter the speed limit: "))
  speed = int(input("Enter the driver's speed: "))

  if speed > speed_limit:
    speed_over_limit = speed - speed_limit
    if speed_over_limit <= 20:
      fine = 100
    elif speed_over_limit <= 30:
      fine = 200
    else:
      fine = 300
    ticket_list.append({"name": name, "speed_over_limit": speed_over_limit, "fine": fine})
    print("Fine: ${}".format(fine))
  else:
    print("No fine.")


