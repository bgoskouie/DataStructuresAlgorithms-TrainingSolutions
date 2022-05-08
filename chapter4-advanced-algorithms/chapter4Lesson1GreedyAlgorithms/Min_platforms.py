# Problem Statement
# Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave. In other words, when a train is about to arrive, at least one platform must be available to accommodate it.

# You will be given arrival and departure times both in the form of a list. The size of both the lists will be equal, with each common index representing the same train. Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345

# Example:
# Input: A schedule of 6 trains:

# arrival = [900,  940, 950,  1100, 1500, 1800]
# departure = [910, 1200, 1120, 1130, 1900, 2000]
# Expected output: Minimum number of platforms required = 3

# The greedy approach:
# Sort the schedule, and make sure when a train arrives or depart, keep track of the required number of platforms. We will have iterator i and j traversing the arrival and departure lists respectively. At any moment, the difference (i - j) will provide us the required number of platforms.

# At the time of either arrival or departure of a train, if i^th arrival is scheduled before the j^th departure, increment the platform_required and i as well. Otherwise, decrement platform_required count, and increase j. Keep track of the max value of platform_required ever, as the expected result.

def min_platforms(arrivals_l, departures_l):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    def find_max(value, current_max):
        '''max_value = find_max(value, max_value)'''
        if value > current_max:
            return value
        else:
            return current_max
    # Sort both the lists.
    # Needed to sort the lists because a train that arrives later can depart earlier (see Test 2)
    arrivals_l.sort()
    departures_l.sort()
    platform_required = 1
    platform_required_max = 1
    # index to traverse on arrivals
    i = 1
    # index to traverse on departures
    j = 0
    last_arrival_time = arrivals_l[0]
    last_departrted = 0
    n = len(arrivals_l)
    if len(departures_l) != n:
        raise Exception(f"Exception on len(arrivals_l)={len(arrivals_l)} and len(departures_l)={len(departures_l)}")
    while i < n and j < n: # last_departrted = find_max(departures_l[j], last_departrted)
        print(f"i={i}, j={j}, platform_required={platform_required}, arrivals_l[i]={arrivals_l[i]}, departures_l[j]={departures_l[j]}, max={platform_required_max}")
        if arrivals_l[i] < departures_l[j]:
            i += 1
            platform_required += 1
            platform_required_max = find_max(platform_required, platform_required_max)
        else:
            j += 1
            platform_required -= 1
    return platform_required_max


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 310, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
