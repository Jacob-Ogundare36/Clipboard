import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"  # saves information inside a json to read


def save_data(filepath, data):  # write the data into a saved file
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(
    filepath,
):  # tries and gets the information returns empty dictionary if no info
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if (
    len(sys.argv) == 2
):  # depending on the command line args save/load/provide a list of saved clipboard information
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data Saved")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")

    elif command == "list":
        print(data)

    else:
        print("Unknown Command")
