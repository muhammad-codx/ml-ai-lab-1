TRAINING_DATA = [
    {"Parcel": "P1", "Traffic": "Low", "Weather": "Clear", "Courier Load": "Light", "Distance": "Short", "Target": "ON_TIME"},
    {"Parcel": "P2", "Traffic": "Medium", "Weather": "Clear", "Courier Load": "Light", "Distance": "Short", "Target": "ON_TIME"},
    {"Parcel": "P3", "Traffic": "Low", "Weather": "Clear", "Courier Load": "Light", "Distance": "Long", "Target": "ON_TIME"},
    {"Parcel": "P4", "Traffic": "Low", "Weather": "Rain", "Courier Load": "Light", "Distance": "Short", "Target": "ON_TIME"},
    {"Parcel": "P5", "Traffic": "Medium", "Weather": "Clear", "Courier Load": "Light", "Distance": "Long", "Target": "ON_TIME"},

    {"Parcel": "P6", "Traffic": "Medium", "Weather": "Rain", "Courier Load": "Light", "Distance": "Short", "Target": "DELAYED"},
    {"Parcel": "P7", "Traffic": "Medium", "Weather": "Clear", "Courier Load": "Heavy", "Distance": "Long", "Target": "DELAYED"},
    {"Parcel": "P8", "Traffic": "High", "Weather": "Clear", "Courier Load": "Light", "Distance": "Long", "Target": "DELAYED"},
    {"Parcel": "P9", "Traffic": "Low", "Weather": "Rain", "Courier Load": "Heavy", "Distance": "Long", "Target": "DELAYED"},
    {"Parcel": "P10", "Traffic": "High", "Weather": "Clear", "Courier Load": "Heavy", "Distance": "Short", "Target": "DELAYED"},

    {"Parcel": "P11", "Traffic": "High", "Weather": "Rain", "Courier Load": "Heavy", "Distance": "Long", "Target": "SEVERE_DELAY"},
    {"Parcel": "P12", "Traffic": "High", "Weather": "Rain", "Courier Load": "Heavy", "Distance": "Short", "Target": "SEVERE_DELAY"},
    {"Parcel": "P13", "Traffic": "Medium", "Weather": "Rain", "Courier Load": "Heavy", "Distance": "Long", "Target": "SEVERE_DELAY"},
    {"Parcel": "P14", "Traffic": "High", "Weather": "Rain", "Courier Load": "Light", "Distance": "Long", "Target": "SEVERE_DELAY"},
    {"Parcel": "P15", "Traffic": "High", "Weather": "Clear", "Courier Load": "Heavy", "Distance": "Long", "Target": "SEVERE_DELAY"},
]


TEST_DATA = [
    {"Parcel": "T1", "Traffic": "Low", "Weather": "Clear", "Courier Load": "Heavy", "Distance": "Short", "Actual": "ON_TIME"},
    {"Parcel": "T2", "Traffic": "High", "Weather": "Rain", "Courier Load": "Light", "Distance": "Short", "Actual": "DELAYED"},
    {"Parcel": "T3", "Traffic": "Medium", "Weather": "Rain", "Courier Load": "Heavy", "Distance": "Short", "Actual": "DELAYED"},
    {"Parcel": "T4", "Traffic": "High", "Weather": "Clear", "Courier Load": "Light", "Distance": "Short", "Actual": "DELAYED"},
    {"Parcel": "T5", "Traffic": "Medium", "Weather": "Clear", "Courier Load": "Heavy", "Distance": "Short", "Actual": "DELAYED"},
    {"Parcel": "T6", "Traffic": "High", "Weather": "Rain", "Courier Load": "Heavy", "Distance": "Long", "Actual": "SEVERE_DELAY"},
]


FEATURES = [
    "Traffic",
    "Weather",
    "Courier Load",
    "Distance"
]


CLASSES = [
    "ON_TIME",
    "DELAYED",
    "SEVERE_DELAY"
]