def run_timing():
    add = 0
    count = 0

    while True:
        run_time = input("Enter 10 km run time: ")
        if not run_time:
            break
        add += float(run_time)
        count += 1

    average = add / count
    print(f"Average of {average}, over {count} runs")

run_timing()