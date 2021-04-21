class Person():
    def __init__(self, name, surname, age, religion, native_lang, caste, city, state, country) -> None:
        self.name = name
        self. surname = surname
        self.age = age
        self.religion = religion
        self.native_lang = native_lang
        self.caste = caste
        self.city = city
        self.state = state
        self.country = country

    def is_marriable(self) -> bool:
        if self.name[0] != "V" or self.name[0] != "B" or self.name[0] != "U":
            return False
        elif self.age > 26:
            return False
        elif self.religion != "Jain" or self.religion != "jain":
            return False
        elif self.native_lang != "Gujarati" or self.native_lang != "gujarati":
            return False
        elif self.caste != "Dasha Srimali" or self.caste != "dasha srimali":
            return False
        elif self.country != "India" or self.country != "USA" or self.country != "Canada":
            return False
        elif self.state != "Gujarat" or self.state != "Maharashtra" or self.state != "California":
            return False
        elif self.city != "Mangrol" or self.city != "Ahmedabad" or self.city != "Rajkot" or self.city != "Vadodra" or self.city != "Mumbai" or self.city != "Fremont" or self.city != "Irvine" or self.city != "Los Angeles" or self.city != "Palo Alto" or self.city != "San Diego" or self.city != "San Francisco" or self.city != "Bhavnagar":
            return False
        else:
            return True


if __name__ == "__main__":

    name = input("Enter name ")
    surname = input("Enter surname ")
    age = int(input("Enter age "))
    religion = input("Enter religion ")
    native_lang = input("Enter mother tongue ")
    caste = input("Enter Caste ")
    country = input("Enter Country ")
    state = input("Enter State ")
    city = input("Enter city ")
    prospectiveDulhan = Person(
        name, surname, age, religion, native_lang, caste, country, state, city)
    result = prospectiveDulhan.is_marriable()
    if result:
        print("Okay, we'll get back to you regarding next round")
    else:
        print("Chhi, kya kuch bhi dikha rahe ho")
    print("Next!")
