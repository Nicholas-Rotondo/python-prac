import csv
import json

def get_info():
    birthdays = {}
    name = input("Enter your name(first and last): ").lower()
    birth = input("Enter birthday like so: (MM/DD/YYYY): ").lower()
    birthdays[name] = birth
    return birthdays

def search_person():
    with open("./birthdict.json", "r") as f:
        for line in f:
            print(line)


def write_to_json():
    birth_info = get_info()
    to_json = json.dumps(birth_info)
    print("Currently adding your input")
    f = open("birthdict.json", "a")
    f.write(to_json + "\n")
    f.close()

def add_another():
    while True:
        add_person = input("Would you like to add another person(y/n): ").lower()
        if add_person == "y":
            write_to_json()
        elif add_person == "n":
            print("Take care")
            break
        else:
            print("Error wrong choice. Goodbye")

def main():
    choice = input("""If you would like to add someone, (type add).
If you would like to look up someones birthday, (type search).
If none of these option suit your needs, (type quit).
""").lower()
    if choice == "add":
        add_another()
    elif choice == "search":
        search_person()
    elif choice == "quit":
        print("Goodbye")
main()


# def write_to_txt(info):
#     wi th open("test_text.txt", "w") as f:
#         f.write(info)
#
# def append_to_txt(info):
#     with open("test_text.txt", "a") as f:
#         f.write(info + "\n")
#
# def write_to_csv(info):
#     f = csv.writer(open("birthdict.csv", "w"))
#     for key, val in birthday.items():
#         f.writerow([kev,val])
#
#
# # seperate to make function that only deals with adding to files
# # keep get_name as just a get method for retrieving info
# # def get_name():
# #     births_of_ppl = get_info()
# #     append_func = append_to_txt(str(births_of_ppl))
# #     retrieve = input("Enter the name of a person you desire: ").lower()
# #     for key,value in births_of_ppl.items():
# #         if retrieve == key:
# #             print(f"The persons birthday is {births_of_ppl.values()}")
# #             append_func
# # get_name()
