""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Home work 5
Problem 3:lightrail.py
Program description: the program developes a few functions that examine
rounte direction when taking the Seattle rail transit, number of stops riders
need.
"""


LINK_STATIONS = ("University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(station):
    '''
    Function -- is_valid_station
        Checks if a given string is a valid Seattle light rail station.
        Provided station must match a station name exactly. For example, "mount
        baker" would not be valid because the case doesn't match.
    Parameter:
        station -- The string to check
    Returns:
        True if a given string is a valid Seattle light rail station
        name, False otherwise.
    '''
    return station in LINK_STATIONS


def getIndex(element, tuple_list):
    '''
    Function -- indexCompare
        Given two words(elements) and a tuple(or list), check which
        element's index is before than another.
    Parameters:
        element - element
        tuple_list - tuple or list
    Returns:
        index that element in tuple or list.Otherwise, -1
    '''

    for i in range(len(tuple_list)):
        if element == tuple_list[i]:
            index_element = i
            return index_element
    return -1


def get_direction(start, end):
    '''
    Function -- get_direction
        Given start and end station names, determines if the direction is
        Northbound or Southbound.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        "Northbound" if the end station is north of the start station, or
        "Southbound" if the end station is south of the start station. If
        either station is invalid, or start and end stations are the same,
        return "No destination found".
    '''

    if is_valid_station(start) and is_valid_station(end) and start != end:
        if getIndex(start, LINK_STATIONS) < getIndex(end, LINK_STATIONS):
            return "Southbound"
        elif getIndex(start, LINK_STATIONS) > getIndex(end, LINK_STATIONS):
            return "Northbound"
    else:
        return "No destination found"


def get_num_stops(start, end):
    '''
    Function -- get_num_stops
        Calculates the number of stops from start to end.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        The number of stops from start to end. If either station is invalid
        or both stations are the same, return 0.
    '''

    if is_valid_station(start) and is_valid_station(end) and start != end:
        numStop = getIndex(start, LINK_STATIONS) - getIndex(end, LINK_STATIONS)
        numStop_abs = abs(numStop)
        return numStop_abs
    return 0
