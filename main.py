mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
mission_totals = len(mission_names)
print("Total number of missions:", mission_totals)
success_totals = sum(mission_success)
print("Number of successful missions:", success_totals)
percentage_of_success = (success_totals/mission_totals) * 100
print(f"Success rate: {percentage_of_success:.2f}%")
print("Missions launched before the year 2000:")
for i in range(len(mission_names)):
    if mission_years[i] < 2000:
        print(f"{mission_names[i]}")
