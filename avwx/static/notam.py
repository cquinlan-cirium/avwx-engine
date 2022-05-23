"""
NOTAM static values
"""

# Q Codes sourced from FAA apprendix
# https://www.faa.gov/air_traffic/publications/atpubs/notam_html/appendix_b.html

SUBJECT = {
    "AA": "Minimum altitude",
    "AC": "Class B, C, D, or E Surface Area",
    "AD": "Air defense identification zone",
    "AE": "Control area",
    "AF": "Flight information region",
    "AH": "Upper control area",
    "AL": "Minimum usable flight level",
    "AN": "Area navigation route",
    "AO": "Oceanic control area",
    "AP": "Reporting point",
    "AR": "ATS route",
    "AT": "Terminal control area",
    "AU": "Upper flight information region",
    "AV": "Upper advisory area",
    "AX": "Significant point",
    "AZ": "Aerodrome traffic zone",
    "CA": "Air/ground facility",
    "CB": "Automatic dependent surveillance - broadcast",
    "CC": "Automatic dependent surveillance - contract",
    "CD": "Controller-pilot data link communications",
    "CE": "En route surveillance radar",
    "CG": "Ground controlled approach system",
    "CL": "Selective calling system",
    "CM": "Surface movement radar",
    "CP": "Precision approach radar",
    "CR": "Surveillance radar element of precision approach radar system",
    "CS": "Secondary surveillance radar",
    "CT": "Terminal area surveillance radar",
    "FA": "Aerodrome",
    "FB": "Friction measuring device",
    "FC": "Ceiling measurement equipment",
    "FD": "Docking system",
    "FE": "Oxygen",
    "FF": "Fire fighting and rescue",
    "FG": "Ground movement control",
    "FH": "Helicopter alighting area/platform",
    "FI": "Aircraft de-icing",
    "FJ": "Oils",
    "FL": "Landing direction indicator",
    "FM": "Meteorological service",
    "FO": "Fog dispersal system",
    "FP": "Heliport",
    "FS": "Snow removal equipment",
    "FT": "Transmissometer",
    "FU": "Fuel availability",
    "FW": "Wind direction indicator",
    "FZ": "Customs/immigration",
    "GA": "GNSS airfield-specific operations",
    "GW": "GNSS area-wide operations",
    "IC": "Instrument landing system",
    "ID": "DME associated with ILS",
    "IG": "Glide path",
    "II": "Inner marker",
    "IL": "Localizer",
    "IM": "Middle marker",
    "IN": "Localizer",
    "IO": "Outer marker",
    "IS": "ILS Category I",
    "IT": "ILS Category II",
    "IU": "ILS Category III",
    "IW": "Microwave landing system",
    "IX": "Locator, outer",
    "IY": "Locator, middle",
    "LA": "Approach lighting system",
    "LB": "Aerodrome beacon",
    "LC": "Runway centre line lights",
    "LD": "Landing direction indicator lights",
    "LE": "Runway edge lights",
    "LF": "Sequenced flashing lights",
    "LG": "Pilot-controlled lighting",
    "LH": "High intensity runway lights",
    "LI": "Runway end identifier lights",
    "LJ": "Runway alignment indicator lights",
    "LK": "Category II components of approach lighting system",
    "LL": "Low intensity runway lights",
    "LM": "Medium intensity runway lights",
    "LP": "Precision approach path indicator",
    "LR": "All landing area lighting facilities",
    "LS": "Stopway lights",
    "LT": "Threshold lights",
    "LU": "Helicopter approach path indicator",
    "LV": "Visual approach slope indicator system",
    "LW": "Heliport lighting",
    "LX": "Taxiway centre line lights",
    "LY": "Taxiway edge lights",
    "LZ": "Runway touchdown zone lights",
    "MA": "Movement area",
    "MB": "Bearing strength",
    "MC": "Clearway",
    "MD": "Declared distances",
    "MG": "Taxiing guidance system",
    "MH": "Runway arresting gear",
    "MK": "Parking area",
    "MM": "Daylight markings",
    "MN": "Apron",
    "MO": "Stopbar",
    "MP": "Aircraft stands",
    "MR": "Runway",
    "MS": "Stopway",
    "MT": "Threshold",
    "MU": "Runway turning bay",
    "MW": "Strip/shoulder",
    "MX": "Taxiway",
    "MY": "Rapid exit taxiway",
    "NA": "All radio navigation facilities",
    "NB": "Nondirectional radio beacon",
    "NC": "DECCA",
    "ND": "Distance measuring equipment",
    "NF": "Fan marker",
    "NL": "Locator",
    "NM": "VOR/DME",
    "NN": "TACAN",
    "NO": "OMEGA",
    "NT": "VORTAC",
    "NV": "VOR",
    "OA": "Aeronautical information service",
    "OB": "Obstacle",
    "OE": "Aircraft entry requirements",
    "OL": "Obstacle lights",
    "OR": "Rescue coordination centre",
    "PA": "Standard instrument arrival",
    "PB": "Standard VFR arrival",
    "PC": "Contingency procedures",
    "PD": "Standard instrument departure",
    "PE": "Standard VFR departure",
    "PF": "Flow control procedure",
    "PH": "Holding procedure",
    "PI": "Instrument approach procedure",
    "PK": "VFR approach procedure",
    "PL": "Flight plan processing",
    "PM": "Aerodrome operating minima",
    "PN": "Noise operating restriction",
    "PO": "Obstacle clearance altitude and height",
    "PR": "Radio failure procedure",
    "PT": "Transition altitude or transition level",
    "PU": "Missed approach procedure",
    "PX": "Minimum holding altitude",
    "PZ": "ADIZ procedure",
    "RA": "Airspace reservation",
    "RD": "Danger area",
    "RM": "Military operating area",
    "RO": "Overflying",
    "RP": "Prohibited area",
    "RR": "Restricted area",
    "RT": "Temporary restricted area",
    "SA": "Automatic terminal information service",
    "SB": "ATS reporting office",
    "SC": "Area control centre",
    "SE": "Flight information service",
    "SF": "Aerodrome flight information service",
    "SL": "Flow control centre",
    "SO": "Oceanic area control centre",
    "SP": "Approach control service",
    "SS": "Flight service station",
    "ST": "Aerodrome control tower",
    "SU": "Upper area control centre",
    "SV": "VOLMET broadcast",
    "SY": "Upper advisory service",
    "WA": "Air display",
    "WB": "Aerobatics",
    "WC": "Captive balloon or kite",
    "WD": "Demolition of explosives",
    "WE": "Exercises",
    "WF": "Air refueling",
    "WG": "Glider flying",
    "WH": "Blasting",
    "WJ": "Banner/target towing",
    "WL": "Ascent of free balloon",
    "WM": "Missile, gun or rocket firing",
    "WP": "Parachute jumping exercise, paragliding, or hang gliding",
    "WR": "Radioactive materials or toxic chemicals",
    "WS": "Burning or blowing gas",
    "WT": "Mass movement of aircraft",
    "WU": "Unmanned aircraft",
    "WV": "Formation flight",
    "WW": "Significant volcanic activity",
    "WY": "Aerial survey",
    "WZ": "Model flying",
}

CONDITION = {
    "AC": "Withdrawn for maintenance",
    "AD": "Available for daylight operation",
    "AF": "Flight checked and found reliable",
    "AG": "Operating but ground checked only, awaiting flight check",
    "AH": "Hours of service changed",
    "AK": "Resumed normal operations",
    "AL": "Operative",
    "AM": "Military operations only",
    "AN": "Available for night operation",
    "AO": "Operational",
    "AP": "Available, prior permission required",
    "AR": "Available on request",
    "AS": "Unserviceable",
    "AU": "Not available",
    "AW": "Completely withdrawn",
    "AX": "Previously promulgated shutdown has been canceled",
    "CA": "Activated",
    "CC": "Completed",
    "CD": "Deactivated",
    "CE": "Erected",
    "CF": "Operating frequency",
    "CG": "Downgraded to",
    "CH": "Changed",
    "CI": "Identification or radio call sign changed to",
    "CL": "Realigned",
    "CM": "Displaced",
    "CN": "Canceled",
    "CO": "Operating",
    "CP": "Operating on reduced power",
    "CR": "Temporarily replaced by",
    "CS": "Installed",
    "CT": "On test, do not use",
    "HA": "Braking action",
    "HB": "Friction coefficient",
    "HC": "Covered by compacted snow to depth of",
    "HD": "Covered by dry snow to a depth of",
    "HE": "Covered by water to a depth of",
    "HF": "Totally free of snow and ice",
    "HG": "Grass cutting in progress",
    "HH": "Hazard due to",
    "HI": "Covered by ice",
    "HJ": "Launch planned",
    "HK": "Bird migration in progress",
    "HL": "Snow clearance completed",
    "HM": "Marked by",
    "HN": "Covered by wet snow or slush to a depth of",
    "HO": "Obscured by snow",
    "HP": "Snow clearance in progress",
    "HQ": "Operation canceled",
    "HR": "Standing water",
    "HS": "Sanding in progress",
    "HT": "Approach according to signal area only",
    "HU": "Launch in progress",
    "HV": "Work completed",
    "HW": "Work in progress",
    "HX": "Concentration of birds",
    "HY": "Snow banks exist",
    "HZ": "Covered by frozen ruts and ridges",
    "LA": "Operating on auxiliary power supply",
    "LB": "Reserved for aircraft based therein",
    "LC": "Closed",
    "LD": "Unsafe",
    "LE": "Operating without auxiliary power supply",
    "LF": "Interference from",
    "LG": "Operating without identification",
    "LH": "Unserviceable for aircraft heavier than",
    "LI": "Closed to IFR operations",
    "LK": "Operating as a fixed light",
    "LL": "Usable for length and width",
    "LN": "Closed to all night operations",
    "LP": "Prohibited to",
    "LR": "Aircraft restricted to runways and taxiways",
    "LS": "Subject to interruption",
    "LT": "Limited to",
    "LV": "Closed to VFR operations",
    "LW": "Will take place",
    "LX": "Operating but caution advised due to",
    "XX": "Plain text following",
}

# Other codes sourced from Nav Canada transition docs
# https://www.navcanada.ca/en/briefing-on-the-transition-to-icao-notam-format.pdf

REPORT_TYPE = {
    "NOTAMN": "New",
    "NOTAMR": "Replace",
    "NOTAMC": "Cancel",
}

TRAFFIC_TYPE = {
    "I": "IFR",
    "V": "VFR",
    "IV": "IFR and VFR",
}

PURPOSE = {
    "N": "Immediate",
    "B": "Briefing",
    "O": "Flight Operations",
    "M": "Miscellaneous",
    "K": "Checklist",
}

SCOPE = {
    "A": "Aerodrome",
    "E": "En Route",
    "W": "Warning",
    "K": "Checklist",
}
