#from Database.Connector import Connector
from Model.Connector import Connector

class Manager:
    """
    Focuses on handling operations within the family tree system, such as creating, modifying, and deleting members.

    Attributes:
        connector (Connector): An instance of the Connector class.
        filter_type (dict): A dictionary containing different ways to filter the current family tree. 

    Methods:
        add_member: adds a new member to the family tree with specified information.
        delete_member: deletes a current member from the family tree.
        view_member_information
        update_member: updates a current member from the family tree with specified information; everything else remains the same.
        add_interest: adds interest to specified family member id.
        remove_interest: removes a specified interest id.
        add_photo: adds photo to specified family member id.
        remove_photo: removes a specified interest id.
        create_spouse_relationship: 
        delete_spouse_relationship:
        add_children: adds children to specified family id (spouse couple id).
        remove_children: removes a specified children id.
        view_member_family_tree: displays the near family tree of specified member.
    """
    def __init__(self):
        self.connector = Connector()
        self.filter_type = {"Age, Alive, Dead, Last Name, Gender"}

    def add_member(self, first_name, last_name, birthday, Nickname=None, YearDied=None, gender=None, pronouns=None, email=None, cell=None, city_born=None, state_born=None, country_born=None, city_current=None, state_current=None, country_current=None):
        self.connector.open_connection()
        
        try:
            query = """
            INSERT INTO Person (FirstName, LastName, Birthday, Nickname, YearDied, Gender, Pronouns, Email, Cell, CityBorn, StateBorn, CountryBorn, CityCurrent, StateCurrent, CountryCurrent) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (first_name, last_name, birthday, Nickname, YearDied, gender, pronouns, email, cell, city_born, state_born, country_born, city_current, state_current, country_current)
            self.connector.cursor.execute(query, values)
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()
    
    def view_member_information(self, first_name, last_name, birthday):
        self.connector.open_connection()
        
        try:
            query = "SELECT * FROM Person WHERE FirstName = %s AND LastName = %s AND Birthday = %s"
            self.connector.cursor.execute(query, (first_name, last_name, birthday,))
            results = self.connector.cursor.fetchall()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()
        
        return results
    
    def delete_member(self, person_id):
        self.connector.open_connection()
        
        try:
            query = "DELETE FROM Person WHERE ID = %s"
            self.connector.cursor.execute(query, (person_id,))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()

    def update_member(self, person_id, first_name=None, last_name=None, birthday=None, is_alive=None, age=None, gender=None, pronouns=None, email=None, cell=None, city_born=None, state_born=None, country_born=None, city_current=None, state_current=None, country_current=None):
        self.connector.open_connection()

        try:
            update_fields = []
            values = []

            # Debug: Print initial values
            print(f"Initial values: {locals()}")

            if first_name is not None:
                update_fields.append("FirstName = %s")
                values.append(first_name)
            if last_name is not None:
                update_fields.append("LastName = %s")
                values.append(last_name)
            if birthday is not None:
                update_fields.append("Birthday = %s")
                values.append(birthday)
            if is_alive is not None:
                update_fields.append("IsAlive = %s")
                values.append(is_alive)
            if age is not None:
                try:
                    age = int(age)
                except ValueError:
                    raise ValueError("Age must be an integer.")
                update_fields.append("Age = %s")
                values.append(age)
            if gender is not None:
                update_fields.append("Gender = %s")
                values.append(gender)
            if pronouns is not None:
                update_fields.append("Pronouns = %s")
                values.append(pronouns)
            if email is not None:
                update_fields.append("Email = %s")
                values.append(email)
            if cell is not None:
                update_fields.append("Cell = %s")
                values.append(cell)
            if city_born is not None:
                update_fields.append("CityBorn = %s")
                values.append(city_born)
            if state_born is not None:
                update_fields.append("StateBorn = %s")
                values.append(state_born)
            if country_born is not None:
                update_fields.append("CountryBorn = %s")
                values.append(country_born)
            if city_current is not None:
                update_fields.append("CityCurrent = %s")
                values.append(city_current)
            if state_current is not None:
                update_fields.append("StateCurrent = %s")
                values.append(state_current)
            if country_current is not None:
                update_fields.append("CountryCurrent = %s")
                values.append(country_current)

            if update_fields:
                query = f"UPDATE Person SET {', '.join(update_fields)} WHERE ID = %s"
                values.append(person_id)

                # Debug: Print query and values before execution
                print(f"Executing query: {query}")
                print(f"With values: {values}")

                self.connector.cursor.execute(query, tuple(values))
                self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()


    def add_interest(self, person_id, interest):
        self.connector.open_connection()
        
        try:
            query = "INSERT INTO Interests (Interest, PersonID) VALUES (%s, %s)"
            self.connector.cursor.execute(query, (interest, person_id))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()
    
    def remove_interest(self, person_id, interest):
        self.connector.open_connection()
        
        try:
            query = "DELETE FROM Interests WHERE PersonID = %s AND Interest = %s"
            self.connector.cursor.execute(query, (person_id, interest,))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()

    def add_photo(self, person_id, photo_path):
        self.connector.open_connection()
        
        try:
            query = "INSERT INTO Photo (PersonID, PhotoPath) VALUES (%s, %s)"
            self.connector.cursor.execute(query, (person_id, photo_path))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()
    
    def remove_photo(self, photo_id):
        self.connector.open_connection()
        
        try:
            query = "DELETE FROM Photo WHERE PhotoID = %s"
            self.connector.cursor.execute(query, (photo_id,))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()

    def create_spouse_relationship(self, parent1_ID, parent2_ID):
        self.connector.open_connection()
        
        try:
            query = "INSERT INTO Spouse (Spouse1ID, Spouse2ID) VALUES (%s, %s)"
            self.connector.cursor.execute(query, (parent1_ID, parent2_ID))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()
    
    def delete_spouse_relationship(self, relationship_id):
        self.connector.open_connection()
        
        try:
            query = "DELETE FROM Spouse WHERE ID = %s"
            self.connector.cursor.execute(query, (relationship_id,))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()

    def create_household_relationship(self, parents1_id, parents2_id, child_id):
        self.connector.open_connection()
        
        if parents2_id == -100:
            parents2_id = None
        
        try:
            query = "INSERT INTO Household (Parent1ID, Parent2ID, ChildID) VALUES (%s, %s, %s)"
            self.connector.cursor.execute(query, (parents1_id, parents2_id, child_id))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()
    
    def delete_household_relationship(self, parents_id, child_id):
        self.connector.open_connection()
        
        try:
            query = "DELETE FROM Children WHERE ParentsID = %s AND ChildID = %s"
            self.connector.cursor.execute(query, (parents_id, child_id))
            self.connector.cnx.commit()

        except Exception as e:
            print(e)
            self.connector.cnx.rollback()

        finally:
            self.connector.close_connection()

    def get_id(self, first_name, last_name, bday):
        self.connector.open_connection()
        
        try:
            query = "SELECT ID FROM Person WHERE FirstName = %s AND LastName = %s AND Birthday = %s"
            self.connector.cursor.execute(query, (first_name, last_name, bday,))
            id = [result[0] for result in self.connector.cursor.fetchall()]

        except Exception as e:
            print(e)

        finally:
            self.connector.close_connection()

        print(id)
        print(id[0])
        return id[0]
    
    def get_parents_id(self, child_id):
        self.connector.open_connection()
        
        try:
            query = "SELECT ParentsID FROM Household WHERE ChildID = %s"
            self.connector.cursor.execute(query, (child_id,))
            parents_id = [result[0] for result in self.connector.cursor.fetchall()]

        except Exception as e:
            print(e)
            parents_id = []

        finally:
            self.connector.close_connection()

        return parents_id[0]

    def get_children_id(self, parents_id):
        self.connector.open_connection()
        
        try:
            query = "SELECT ChildID FROM Household WHERE ParentsID = %s"
            self.connector.cursor.execute(query, (parents_id,))
            children_id = [result[0] for result in self.connector.cursor.fetchall()]

        except Exception as e:
            print(e)
            children_id = []

        finally:
            self.connector.close_connection()

        return children_id
    
    def get_spouse_id(self, person_id):
        self.connector.open_connection()
        
        try:
            query = "SELECT ID FROM Spouse WHERE Spouse1ID = %s OR Spouse2ID = %s"
            self.connector.cursor.execute(query, (person_id, person_id,))
            spouse_id = [result[0] for result in self.connector.cursor.fetchall()]

        except Exception as e:
            print(e)
            spouse_id = []

        finally:
            self.connector.close_connection()

        return spouse_id[0]
    
    def view_interest(self, person_id):
        self.connector.open_connection()
        
        try:
            query = "SELECT Interest FROM Interests WHERE PersonID = %s"
            self.connector.cursor.execute(query, (person_id,))
            interest = [result[0] for result in self.connector.cursor.fetchall()]

        except Exception as e:
            print(e)
            interest = []

        finally:
            self.connector.close_connection()

        return interest
    
    def get_family_info(self, person_id):
        self.connector.open_connection()
        
        try:
            # Query for parents
            query_parents = """
                SELECT DISTINCT p1.ID AS ParentID, p1.FirstName AS ParentFirstName, p1.LastName AS ParentLastName
                FROM Household h
                JOIN Person p1 ON h.ParentsID = p1.ID
                LEFT JOIN Spouse s ON s.Spouse1ID = p1.ID OR s.Spouse2ID = p1.ID
                WHERE h.ChildID = %s

                UNION

                SELECT DISTINCT p2.ID AS ParentID, p2.FirstName AS ParentFirstName, p2.LastName AS ParentLastName
                FROM Household h
                JOIN Person p1 ON h.ParentsID = p1.ID
                LEFT JOIN Spouse s ON s.Spouse1ID = p1.ID OR s.Spouse2ID = p1.ID
                JOIN Person p2 ON p2.ID = (CASE 
                                                WHEN s.Spouse1ID = p1.ID THEN s.Spouse2ID 
                                                WHEN s.Spouse2ID = p1.ID THEN s.Spouse1ID 
                                            END)
                WHERE h.ChildID = %s;

            """
            self.connector.cursor.execute(query_parents, (person_id, person_id,))
            parents = self.connector.cursor.fetchall()

            # Query for spouse (if any)
            query_spouse = """
                SELECT p.ID AS SpouseID, p.FirstName, p.LastName
                FROM Spouse s
                JOIN Person p ON (s.Spouse1ID = p.ID OR s.Spouse2ID = p.ID)
                WHERE (s.Spouse1ID = %s OR s.Spouse2ID = %s) AND p.ID != %s;
            """
            self.connector.cursor.execute(query_spouse, (person_id, person_id, person_id,))
            spouse = self.connector.cursor.fetchone()

            # Query for children (if any)
            query_children = """
                SELECT p.ID AS ChildID, p.FirstName, p.LastName
                FROM Household h
                JOIN Person p ON h.ChildID = p.ID
                WHERE h.ParentsID = %s;

            """
            self.connector.cursor.execute(query_children, (person_id,))
            children = self.connector.cursor.fetchall()

            # Store the results in a list of dictionaries for easier handling
            results = []

            for parent in parents:
                results.append({
                    "Relationship": "Parent",
                    "ID": parent[0],
                    "FirstName": parent[1],
                    "LastName": parent[2]
                })

            if spouse:
                results.append({
                    "Relationship": "Spouse",
                    "ID": spouse[0],
                    "FirstName": spouse[1],
                    "LastName": spouse[2]
                })

            for child in children:
                results.append({
                    "Relationship": "Child",
                    "ID": child[0],
                    "FirstName": child[1],
                    "LastName": child[2]
                })

            return results

        except Exception as e:
            # Log the error or raise a custom exception
            print(f"Error fetching family info: {e}")
            return None

        finally:
            self.connector.close_connection()



if __name__ == "__main__":
    m = Manager()
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