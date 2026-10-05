print(
    '''
    ------MENU-----
    1.Biryani
    2.Chicken 65
    3.Veg Pulao
    4.Butter Chicken
    5.Paneern Tikka
    
    '''

)
option = int(input("Enter the option :"))
match option:
    case 1:
        print('''
Item          :Biryani
Price         :₹300
Description   :Aromatic basmati rice layered with tender meat and flavorful spices.
              ''')
    case 2:
        print('''
Item          :Chicken 65
Price         :₹180
Description   :Spicy, crispy fried chicken tossed with chilies, garlic, and curry leaves.
                  ''')
    case 3:
        print('''
Item          :Veg Pulao
Price         :₹150
Description   :Fragrant basmati rice cooked with fresh vegetables and aromatic spices
                  ''')
    case 4:
        print('''
Item          :Butter Chicken
Price         :₹230
Description   :Tender chicken simmered in a rich, creamy tomato-butter gravy with aromatic spices.
                  ''')
    case 5:
        print('''
Item          :Paneer tikka
Price         :₹200
Description   :Spiced paneer cubes grilled with vegetables, offering a smoky, tangy flavor.
                  ''')
    case _:
        print("Invalid option")
