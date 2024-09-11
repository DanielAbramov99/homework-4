pizza_slice: int = int(input("how many slices:"))
pizza_friend: int = pizza_slice // 4
pizza_left: int = pizza_slice % 4
print(f"pizza slices for each friend{pizza_friend}")
if pizza_slice != 0:
    print(f"pizza slices that left are:{pizza_left}")

pizza_slice: int = int(input("how many slices:"))
friends: int = int(input("how many friends:"))
pizza_friend: int = pizza_slice // friends
pizza_left: int = pizza_slice % friends
print(f"pizza slices for each friend{pizza_friend}")
if pizza_slice != 0:
    print(f"pizza slices that left are:{pizza_left}")
