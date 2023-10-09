import input, workout, schedule

def main():
    earn, energy = input.ReadInputs()
    matrix = workout.getWorkOut(earn, energy)
    schd = schedule.getSchedule(matrix)
    print(schd)

if __name__ == "__main__":
    main()
