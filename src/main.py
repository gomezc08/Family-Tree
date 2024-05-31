from Database import Manager  # Adjust import based on your package structure

def main():
    print("Choose an option below.")
    print("\t1. View family member.")
    print("\t2. Add family member.")
    answer = input("Option: ")
    
    if answer == '1':
        number1()
    elif answer == '2':
        number2()
    else:
        print("Invalid option. Please choose 1 or 2.")

def number1():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    
    # Instantiate Manager if it's a class
    manager_instance = Manager.Manager()  # Adjust this based on the actual class name
    
    # Call view_member_information on the manager_instance
    result1 = manager_instance.view_member_information(first_name, last_name)
    
    if result1:
        member_info = result1[0]  # Assuming there's only one result tuple
        result2 = manager_instance.get_family_info(member_info[0])
        print(f"HERE IS {first_name} {last_name}...")
        print(f"ID number: {member_info[0]}")
        print(f"First Name: {member_info[1]}")
        print(f"Last Name: {member_info[2]}")
        print(f"Birthday: {member_info[3]}")
        print(f"Age: {member_info[5]}")
        print(f"Gender: {member_info[6]}")
        print(f"Pronouns: {member_info[7]}")
        print(f"Email: {member_info[8]}")
        print(f"Phone: {member_info[9]}")
        print(f"City Born: {member_info[10]}, {member_info[11]}, {member_info[12]}")
        print(f"Current City: {member_info[13]}, {member_info[14]}, {member_info[15]}")
        print("\n\n\n")
        print(f"HERE IS {first_name} {last_name}'s RELATIONSHIPS...")
        print(result2)
        
    else:
        print(f"No member found with first name '{first_name}' and last name '{last_name}'.")

def number2():
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
    if not phone:
        phone = None
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
    # establishing place in tree.
    # step 1: establishing parents.
    answer1 = input("Wanna add parents? (yes/no): ")
    if answer1 == "yes":
        
        manager_instance.create_household_relationship(parentsID, childID)
    
    # step 2: establishing spouse.
    answer2 = input("Wanna establish spouse? (yes/no): ")
    if answer2 == "yes":
        manager_instance.create_spouse_relationship(parent1ID, parent2ID)
    
    # step 3: establishing children.
    answer3 = input("Wanna establish children? (yes/no): ")
    while answer3 == "yes":
        manager_instance.create_household_relationship(parentsID, childID)
        answer3 = input("Wanna establish another child? (yes/no): ")
        
    

if __name__ == "__main__":
    main()
