import csv
import json

def get_info():
    birthdays = {}
    name = input("Enter your name(first and last): ").lower()
    birth = input("Enter birthday like so: (MM/DD/YYYY): ").lower()
    birthdays[name] = birth
    return birthdays

def validate_user_input():
    print("Validating user data!")
validate_user_input()

def write_to_json():
    birth_info = get_info()
    to_json = json.dumps(birth_info)
    print("Currently adding your input")
    f = open("birthdict.json", "a")
    f.write(to_json + "\n")
    f.close()
write_to_json()

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
add_another()


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
#
# # def get_name():
# #     births_of_ppl = get_info()
# #     retrieve = input("Enter the name of a person you desire: ").lower()
# #     for key,value in births_of_ppl.items():
# #         if retrieve == key:
# #             print(f"The persons birthday is {births_of_ppl.values()}")
# # get_name()
