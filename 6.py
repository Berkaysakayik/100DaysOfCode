print("""
****************************************
*             WELCOME!                 *
*        We are Tour Persion..         *
*     We provide world wide tours.     *
****************************************
""")

print("""
****************************************
*             Tour Paris!              *
*  Eiffel Tower icluded all city tour  *
*     Three night and four days        *
*        3000 Euro per person          *
*           Only for 13 people         *
****************************************
""")

print("""
****************************************
*             Tour Balkans!            *
*          Hungary icluded tour        *
*        Four night and five days      *
*          1200 Euro per person        *
*           Only for 21 people         *
****************************************
""")

print("""
****************************************
*          Tour Egypt - Morocco!       *
* Pyramids included two countries tour *
*        Six night and seven days      *
*          2500 Euro per person        *
*           Only for 20 people         *        
****************************************
""")


while True:

    print("""
We Provide Three Tours
1. Tour Paris           (13 People)
2. Tour Balkan          (21 People)
3. Tour Egypt - Morocco (20 People)

    """)

    Package = int(input("Please Choose Package (1,2 or 3): "))

    if Package == 1:
        Person  = int(input("How many people are you be: "))
        Student = int(input("How many students are you have: "))

        if Person >=0 and Person <= 13:
            if Student >=0 and Student <= 13:
                cutstdnt = (Student * 3000)*(20/100)
                stprice = (Student*3000) - cutstdnt
                prsnprice = (Person-Student)*3000
                totalprice = stprice+prsnprice
                print(f"Your total bill is {totalprice} Euro. {stprice} Euro for students and {prsnprice} Euro is other peoples.")
                break

        if Person >= 13 and Person <= 21:
            print("This tour is for only 13 people, if you are more than 13 you can look other tours.")

        else:
            print("Sorry our capasite is only for package's.")
            break

    if Package == 2:
        Person  = int(input("How many people are you be: "))
        Student = int(input("How many students are you have: "))

        if Person >=0 and Person <= 21:
            if Student >=0 and Student <= 21:
                cutstdnt = (Student * 1200)*(20/100)
                stprice = (Student*1200) - cutstdnt
                prsnprice = (Person-Student)*1200
                totalprice = stprice+prsnprice
                print(f"Your total bill is {totalprice} Euro. {stprice} Euro for students and {prsnprice} Euro is other peoples.")
                break
        
        else:
            print("21 with the highest capacity of the tours we offer.")
            break

    if Package == 3:
        Person  = int(input("How many people are you be: "))
        Student = int(input("How many students are you have: "))

        if Student >=0 and Student <= 20:
                cutstdnt = (Student * 2500)*(20/100)
                stprice = (Student*2500) - cutstdnt
                prsnprice = (Person-Student)*2500
                totalprice = stprice+prsnprice
                print(f"Your total bill is {totalprice} Euro. {stprice} Euro for students and {prsnprice} Euro is other peoples.")
                break
        
        else:
            print("Maybe you have to check this Tour Balkan, it is the highest capacity of the tours we offer ")