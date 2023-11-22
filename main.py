import input, backtracking_hs

def main():
    sets = input.ReadInputs()
    selected_players = backtracking_hs(sets, [], 11, 0)

    min = len(selected_players)
    print(f"Cantidad mínima: {min} (", end="")
    for i in range(min-1):
        print(f"{selected_players[i]}, ", end="")
    print(f"{selected_players[min-1]})")

if __name__ == "__main__":
    main()
