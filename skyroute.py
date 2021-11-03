from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
stations_under_construction = []
for letter, landmark in landmark_choices.items():
  landmark_string += f"{letter} - {landmark}\n"
def greet():
  print("Hi there and welcome to SkyRoute!")
  is_employee = input("If you are an employee please type in your personal number to make authorized entrance, if not pelase please enter: ")
  if is_employee == str(1111):
    number_of_stations = int(input("Please type in the number of stations that are under construction: "))
    progress_number = 1
    number_of_stations_stat = number_of_stations
    while number_of_stations > 0:
      add_a_station_as_under_construction = input(f"{progress_number}/{number_of_stations_stat} > Type in the name of the station that is under construction: ")
      stations_under_construction.append(add_a_station_as_under_construction)
      progress_number += 1
      number_of_stations -=1

  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)
def skyroute():
  greet()
  new_route()
  goodbye()
def set_start_and_end(start_point, end_point):
  if start_point:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == "b":
      get_start()
      get_end()
    elif change_point == "o":
      get_start()
    elif change_point == "d":
      get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()
    while start_point == end_point:
      print("Your origin and destination stations must be different. Please choose the stations again.")
      start_point = get_start()
      end_point = get_end()
  return start_point, end_point
def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices.keys():
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_start()
def get_end():
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices.keys():
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_end()
def new_route(start_point = None, end_point = None):
 start_point, end_point = set_start_and_end(start_point, end_point)
 shortest_route = get_route(start_point, end_point)
 if shortest_route is not None:
  shortest_route_string = "\n".join(shortest_route)
  print(f"The shortest metro route from {start_point} to {end_point} is:\n{shortest_route_string}")
 else:
   print(f"Unfortunately, there is currently no path between {start_point} and {end_point} due to maintenance.")
 again = (input("Would you like to see another route? Enter y/n: ")).lower()
 if again == "y":
   show_landmarks()
   new_route()
def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ").lower()
  if see_landmarks == "y":
    print(landmark_string)
def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      metro_system = get_active_stations() if stations_under_construction else vc_metro
      if len(stations_under_construction) > 0:
        possible_route = dfs(metro_system, start_station, end_station)
        if not possible_route:
          return None
      route = bfs(metro_system, start_station, end_station)
      if route is not None:
        routes.append(route)
  shortest_route = min(routes, key=len)
  return shortest_route
def goodbye():
  print("Thanks for using SkyRoute!")
def get_active_stations():
  updated_metro = vc_metro
  for station_under_construction in stations_under_construction:
    for current_station, neighbouring_stations in vc_metro.items():
      if current_station != station_under_construction:
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        updated_metro[current_station] = set([]) 
  return updated_metro
skyroute()

