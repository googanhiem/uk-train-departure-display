import os
import re

def loadConfig():
    data = {
        "journey": {},
        "api": {}
    }

    data["refreshTime"] = 60
    data["screenRotation"] = 2
    data["screenBlankHours"] = "1-5"
    data["dualScreen"] = False
    data["hoursPattern"] = re.compile("^((2[0-3]|[0-1]?[0-9])-(2[0-3]|[0-1]?[0-9]))$")
    data["journey"]["departureStation"] = "PAD"
    data["journey"]["destinationStation"] = ""
    data["journey"]["individualStationDepartureTime"] = False
    data["journey"]["outOfHoursName"] = "London Paddington"
    data["journey"]["stationAbbr"] = { "International": "Intl." }
    data["journey"]['timeOffset'] = "0"
    data["journey"]["screen1Platform"] = ""
    data["journey"]["screen2Platform"] = ""
    data["api"]["apiKey"] = "[INSERT-API-KEY-HERE]"
    data["api"]["operatingHours"] = "6-1"

    return data
    
