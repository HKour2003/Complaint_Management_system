class CountryManagementApp:
    def __init__(self):
        self.country_dict = {
            'IN': ['India', 'Delhi', 1320000000],
            'US': ['America', 'Washington', 320000000],
            'AU': ['Australia', 'Canberra', 24000000],
            'CA': ['Canada', 'Ottawa', 940000]
        }

    def view_countries(self):
        print("Country Code\tCountry Name\tCapital\t\tPopulation")
        for code, details in self.country_dict.items():
            print(f"{code}\t\t{details[0]}\t\t{details[1]}\t\t{details[2]}")

    def add_country(self, code, name, capital, population):
        if code in self.country_dict:
            print(f"Country with code {code} already exists.")
        else:
            self.country_dict[code] = [name, capital, population]
            print(f"Country {name} ({code}) added successfully.")

    def delete_country(self, code):
        if code in self.country_dict:
            country_name = self.country_dict.pop(code)[0]
            print(f"Country {country_name} ({code}) deleted successfully.")
        else:
            print(f"Country with code {code} not found.")

# Sample usage of the CountryManagementApp
app = CountryManagementApp()

while True:
    print("\nCountry Management App Menu:")
    print("1. View Countries")
    print("2. Add Country")
    print("3. Delete Country")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        app.view_countries()
    elif choice == '2':
        code = input("Enter country code: ")
        name = input("Enter country name: ")
        capital = input("Enter capital city: ")
        population = int(input("Enter population: "))
        app.add_country(code, name, capital, population)
    elif choice == '3':
        code = input("Enter country code to delete: ")
        app.delete_country(code)
    elif choice == '4':
        print("Exiting the Country Management App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
