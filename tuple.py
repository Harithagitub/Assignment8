airport_data = {}

def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airport_data[icao_code] = airport_name
    print(f"Airport '{airport_name}' with ICAO code '{icao_code}' added successfully.")

def fetch_airport_info():
    icao_code = input("Enter the ICAO code of the airport: ")
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code '{icao_code}' is '{airport_data[icao_code]}'.")
    else:
        print(f"No information found for the airport with ICAO code '{icao_code}'.")

while True:
    print("\n1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        add_airport()
    elif choice == '2':
        fetch_airport_info()
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
