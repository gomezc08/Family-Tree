from Model import Manager 
import tkinter as tk
from tkinter import filedialog, simpledialog
import shutil
import os

def main():
    print("Choose an option below.")
    print("\t1. View family member (see all their info).")
    print("\t2. Add family member (create a new family member and add relationships/establish it in the family).")
    print("\t3. Edit family member (edit some of their info).")
    print("\t4. Marriage (create a spouse relationship between two people).")
    print("\t5. Divorce (tamales).")
    print("\t6. Add an interest (for example: soccer, cooking, hiking).")
    print("\t7. Remove an interest.")
    print("\t8. Add profile pic to a user.")
    print("\t9. Initialize (only for testing purposes).")
    answer = input("Option: ")
    
    if answer == '1':
        number1()
    elif answer == '2':
        number2()
    elif answer == '3':
        number3()
    elif answer == '4':
        number4()
    elif answer == '5':
        number5()
    elif answer == '6':
        number6()
    elif answer == '7':
        number7()
    elif answer == '8':
        number8()
    elif answer == '9':
        number9()
    else:
        print("Invalid input. Please enter a number between 1 and 7.")


def number1():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birthday = input("Enter bday (YYYY-MM-DD): ")
    
    manager_instance = Manager.Manager()  # Adjust this based on the actual class name
    personID = manager_instance.get_id(first_name, last_name, birthday)
    
    
    # Call view_member_information on the manager_instance
    result1 = manager_instance.view_member_information(first_name, last_name, birthday)
    
    member_info = result1[0] 
    print("\n\n\n")
    print(f"Here is {first_name} {last_name}:")
    print(f"\tID number: {member_info[0]}")
    print(f"\tFirst Name: {member_info[1]}")
    print(f"\tLast Name: {member_info[2]}")
    print(f"\tBirthday: {member_info[3]}")
    print(f"\tAge: {member_info[5]}")
    print(f"\tGender: {member_info[6]}")
    print(f"\tPronouns: {member_info[7]}")
    print(f"\tEmail: {member_info[8]}")
    print(f"\tPhone: {member_info[9]}")
    print(f"\tCity Born: {member_info[10]}, {member_info[11]}, {member_info[12]}")
    print(f"\tCurrent City: {member_info[13]}, {member_info[14]}, {member_info[15]}")
    print(f"\tInterests: {manager_instance.view_interest(personID)}")
    
    result2 = manager_instance.get_family_info(member_info[0])
    # Create empty lists for each relationship type
    spouses = []
    children = []
    parents = []

    # Iterate over each dictionary in the result2 list
    for person in result2:
        full_name = f"{person['FirstName']} {person['LastName']}"
        if person['Relationship'] == 'Spouse':
            spouses.append(full_name)
        elif person['Relationship'] == 'Child':
            children.append(full_name)
        elif person['Relationship'] == 'Parent':
            parents.append(full_name)

    # Print the lists to check the results
    print("\tSpouses:", spouses)
    print("\tChildren:", children)
    print("\tParents:", parents)
    print("\n\n\n")
    

def number2():
    manager_instance = Manager.Manager()
    # Placeholder for adding family member functionality
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    birthday_str = input("Enter birthday (YYYY-MM-DD): ").strip()
    age = 10
    is_alive_str = input("Is the member alive? (yes/no): ").strip().lower()    
    is_alive = True if is_alive_str == 'yes' else False
    gender = input("Enter gender (Male/Female/Non-binary, optional): ").strip()
    pronouns = input("Enter pronouns (optional): ").strip()
    email = input("Enter email (optional): ").strip()
    cell = input("Enter phone number (optional): ").strip()
    city_born = input("Enter city of birth (optional): ").strip()
    state_born = input("Enter state/province of birth (optional): ").strip()
    country_born = input("Enter country of birth (optional): ").strip()
    city_current = input("Enter current city (optional): ").strip()
    state_current = input("Enter current state/province (optional): ").strip()
    country_current = input("Enter current country (optional): ").strip()
    
    # Handle empty inputs
    if not birthday_str:
        birthday_str = None
    if not gender:
        gender = None
    if not pronouns:
        pronouns = None
    if not email:
        email = None
    if not cell:
        cell = None
    if not city_born:
        city_born = None
    if not state_born:
        state_born = None
    if not country_born:
        country_born = None
    if not city_current:
        city_current = None
    if not state_current:
        state_current = None
    if not country_current:
        country_current = None
    
    manager_instance.add_member(first_name, last_name, birthday_str, is_alive, age, gender, pronouns, email, cell, city_born, state_born, country_born, city_current, state_current, country_born)
    
    personID = manager_instance.get_id(first_name, last_name, birthday_str)
    parentID1 = -100
    parentID2 = -100
    spouseID = -100
    
    # establishing place in tree.
    # step 1: establishing parents.
    hasParents = input("Wanna add ur parent(s)? (yes/no)")
    if hasParents == "yes":
        f1 = input("Parent First Name: ")
        l1 = input("Parent Last Name: ")
        b1 = input("Parent Birthday (YYYY-MM-DD): ")
        parentID1 = manager_instance.get_id(f1, l1, b1)
    
        hasParents1 = input("Wanna add parent 2? (yes/no): ")
        if hasParents1 == "yes":
            f1 = input("Parent First Name: ")
            l1 = input("Parent Last Name: ")
            b1 = input("Parent Birthday (YYYY-MM-DD): ")
            parentID2 = manager_instance.get_id(f1, l1, b1)
        
        manager_instance.create_household_relationship(parentID1, parentID2, personID)
    
    # step 2: establishing spouse.
    answer2 = input("Wanna establish spouse? (yes/no): ")
    if answer2 == "yes":
        f2 = input("Spouse First Name: ")
        l2 = input("Spouse Last Name: ")
        b2 = input("Spouse Birthday (YYYY-MM-DD): ")
        spouseID = manager_instance.get_id(f2, l2, b2)
        manager_instance.create_spouse_relationship(spouseID, personID)
    
    # step 3: establishing children.
    answer3 = input("Wanna establish children? (yes/no): ")
    if answer3 == "yes":
        while answer3 == "yes":
            f3 = input("Child First Name: ")
            l3 = input("Child Last Name: ")
            b3 = input("Child Birthday (YYYY-MM-DD): ")
            childID = manager_instance.get_id(f3, l3, b3)
            manager_instance.create_household_relationship(personID, spouseID, childID)
            answer3 = input("Wanna establish another child? (yes/no): ")
    
    print("Okay! I've added it into the database. Thank you :)")

# edit family member.
def number3():
    manager_instance = Manager.Manager()
    # Placeholder for adding family member functionality
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    birthday_str = input("Enter birthday (YYYY-MM-DD): ").strip()
    age = input("Enter age: ").strip()
    is_alive_str = input("Is the member alive? (yes/no): ").strip().lower()    
    is_alive = True if is_alive_str == 'yes' else False
    gender = input("Enter gender (Male/Female/Non-binary, optional): ").strip()
    pronouns = input("Enter pronouns (optional): ").strip()
    email = input("Enter email (optional): ").strip()
    cell = input("Enter phone number (optional): ").strip()
    city_born = input("Enter city of birth (optional): ").strip()
    state_born = input("Enter state/province of birth (optional): ").strip()
    country_born = input("Enter country of birth (optional): ").strip()
    city_current = input("Enter current city (optional): ").strip()
    state_current = input("Enter current state/province (optional): ").strip()
    country_current = input("Enter current country (optional): ").strip()
    
    # Handle empty inputs
    if not birthday_str:
        birthday_str = None
    if not gender:
        gender = None
    if not pronouns:
        pronouns = None
    if not email:
        email = None
    if not cell:
        cell = None
    if not city_born:
        city_born = None
    if not state_born:
        state_born = None
    if not country_born:
        country_born = None
    if not city_current:
        city_current = None
    if not state_current:
        state_current = None
    if not country_current:
        country_current = None
    
    manager_instance.update_member(first_name, last_name, birthday_str, is_alive, age, gender, pronouns, email, cell, city_born, state_born, country_born, city_current, state_current, country_born)
    print(f"okay I have updated {first_name} :)")
    
# marriage.
def number4():
    manager_instance = Manager.Manager()
    first_name1 = input("Enter first name of person 1: ").strip()
    last_name1 = input("Enter last name of person 1: ").strip()
    birthday_str1 = input("Enter birthday of person 1 (YYYY-MM-DD): ").strip()
    manager_instance.get_id(first_name1, last_name1, birthday_str1)
    
    first_name2 = input("Enter first name of person 2: ").strip()
    last_name2 = input("Enter last name of person 2: ").strip()
    birthday_str2 = input("Enter birthday of person 2 (YYYY-MM-DD): ").strip()
    manager_instance.get_id(first_name2, last_name2, birthday_str2)
    
    print(f"Okay! {first_name1} and {first_name2} are married.")

def number5():
    manager_instance = Manager.Manager()
    first_name1 = input("Enter first name of person 1: ").strip()
    last_name1 = input("Enter last name of person 1: ").strip()
    birthday_str1 = input("Enter birthday of person 1 (YYYY-MM-DD): ").strip()
    manager_instance.get_id(first_name1, last_name1, birthday_str1)
    
    first_name2 = input("Enter first name of person 2: ").strip()
    last_name2 = input("Enter last name of person 2: ").strip()
    birthday_str2 = input("Enter birthday of person 2 (YYYY-MM-DD): ").strip()
    manager_instance.get_id(first_name2, last_name2, birthday_str2)
    
    print(f"{first_name1} and {first_name2} are now divorced :(")

def number6():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birthday = input("Enter bday (YYYY-MM-DD): ")
    
    manager_instance = Manager.Manager()  
    personID = manager_instance.get_id(first_name, last_name, birthday)
    
    interest = input(f"Enter a new interest for {first_name} {last_name}: ")
    manager_instance.add_interest(personID, interest)
    
    print("Seems like a lame interest but okay.")

def number7():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birthday = input("Enter bday (YYYY-MM-DD): ")
    
    manager_instance = Manager.Manager()  
    personID = manager_instance.get_id(first_name, last_name, birthday)
    
    print(f"Here are {first_name}'s current interests: {manager_instance.view_interest(personID)}")
    interest = input(f"Enter the interest you would like to remove (please spell correctly with correct capitialization): ")
    manager_instance.remove_interest(personID, interest)
    
    print("Memo chicken likes.")

def number8():
    # Create a Tkinter root widget (it will be hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog to select a file
    file_path = filedialog.askopenfilename(title="Select a .png file to move", filetypes=[("PNG files", "*.png")])

    # Check if a file was selected and if it has a .png extension
    if file_path and file_path.lower().endswith('.png'):
        # Ask for user input for first name, last name, and birthday
        first_name = simpledialog.askstring("Input", "Enter First Name:")
        last_name = simpledialog.askstring("Input", "Enter Last Name:")
        birthday = simpledialog.askstring("Input", "Enter birthday (YYYY-MM-DD):")
        
        manager_instance = Manager.Manager() 
        personID = manager_instance.get_id(first_name, last_name, birthday)

        # Define the destination directory
        destination_directory = "./static/pic_location"

        # Ensure the destination directory exists
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Check if a directory was selected
        if destination_directory:
            # Extract the file name from the file path
            file_name = last_name + first_name + ".png"
            # Construct the full destination path
            destination_path = os.path.join(destination_directory, file_name) 
            print(f"Destination path: {destination_path}")

            # Move the file to the destination directory
            shutil.move(file_path, destination_path)
            
            # Call the add_photo method if it exists
            manager_instance.add_photo(personID, destination_path)

            print(f"Moved '{file_path}' to '{destination_path}'")
        else:
            print("No destination directory selected.")
    else:
        print("No .png file selected.")  

def number9():
    m = Manager.Manager()
    # mama.
    m.add_member("Veronica", "Gomez", "1973-01-09", True, 51, "Female", "She/her/hers")
    m.add_interest(1, "Nursing")
    m.add_interest(1, "Cooking")
    m.add_interest(1, "Wine")
    
    # papa.
    m.add_member("Antonio", "Gomez", "1968-06-13", True, 55, "Male", "He/him/his")
    m.add_interest(2, "Soccer")
    m.add_interest(2, "Working Out")
    m.add_interest(2, "Pooping")
    
    # Angela.
    m.add_member("Angela", "Gomez", "1999-11-11", True, 24, "Female", "She/her/hers")
    m.add_interest(3, "Studying")
    m.add_interest(3, "Avacado toast")
    m.add_interest(3, "Asians")
    
    # Chris.
    m.add_member("Christian", "Gomez", "2002-07-25", True, 21, "Male", "He/him/his", "kimigomez10@gmail.com", "360-839-1100", "Vancouver", "WA", "USA")
    m.add_interest(4, "Soccer")
    m.add_interest(4, "CS")
    m.add_interest(4, "Spongebob")
    
    # Memo.
    m.add_member("Memo", "Gomez", "2016-05-05", True, 8, "Male")
    m.add_interest(5, "Walks")
    m.add_interest(5, "Chicken")
    m.add_interest(5, "Sleeping")
    m.add_interest(5, "Blankets")
    m.add_interest(5, "Papa")
    
    # getting each person's id.
    mama_id = m.get_id("Veronica", "Gomez", "1973-01-09")
    papa_id = m.get_id("Antonio", "Gomez", "1968-06-13")
    angela_id = m.get_id("Angela", "Gomez", "1999-11-11")
    chris_id = m.get_id("Christian", "Gomez", "2002-07-25")
    memo_id = m.get_id("Memo", "Gomez", "2016-05-05")
    
    # creating associations.
    m.create_spouse_relationship(papa_id, mama_id)
    mama_papa_id = m.get_spouse_id(mama_id)
    
    # children to family.
    m.create_household_relationship(mama_papa_id, angela_id)
    m.create_household_relationship(mama_papa_id, chris_id)
    m.create_household_relationship(mama_papa_id, memo_id)

if __name__ == "__main__":
    main()