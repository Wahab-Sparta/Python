import time

def stopwatch():
    started = False
    lap_times = {}
    lap_count = 1
    while not started:  #Will loop until the stopwatch has started
        start = input("Press Enter to start the Stopwatch. ")
        if start == "":
            start_time = round(time.time(), 3)
            date_and_time = time.ctime()
            print("Started!")
            started = True
    while started:  #Will loop until the stopwatch has ended
        stop_or_lap = input("Press Enter once more to stop the Stopwatch\n Or type 'lap' to add a lap timer: ").lower()
        if stop_or_lap == "lap":
            lap_time = round(time.time() - start_time, 3)
            print(lap_time)
            lap_times["Lap "+str(lap_count)] = lap_time
            lap_count += 1
        elif stop_or_lap == "":
            end_time = round(time.time(), 3)
            final = round(end_time - start_time,3)
            print("Finished!")
            print(f"Your elapsed time was: {final}. Your lap times were: {lap_times}")
            with open("Python_Time/time_log.txt", "a") as f:
                if lap_times:
                    f.write(f"{date_and_time}\nLap Times: {lap_times}\nFinal time: {final}\n\n")
                else:
                    f.write(f"{date_and_time}\nFinal time: {final}\n\n")
            started = False

stopwatch()