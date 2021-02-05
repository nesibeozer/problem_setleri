
class mail:
    pass
mail1 = mail( )
mail1.user_name= "Gaziuniversitesi"
mail1.domain_name= "@gazi.edu"
mail1.country_code= ".tr"
print(mail1.user_name+mail1.domain_name+mail1.country_code)
pass
def All_letters(username):
    All_letters= ["a","b","c","d","e","f","g","h","i","ı","j","k","l","m","n","o","p","r",
                 "s","t","u","v","y","z","A","B","C","D","E","F","G","H","I","K","L","M",
                 "N","O","P","R","S","T","U","V","Y","Z"]
    for letters in username:
        for control_letters in list:
            if letters == control_letters:
                return True
    return False

def characters_numbers (username):
    characters_numbers= ["1","2","3","4","5","6","7","8","9","-","_"]
    for characters in username:
        for control_charectars in list:
            if characters == control_charectars:
                return True
    return False

def Xch (website): # Xch = letters, numbers
     Xch = ["a","b","c","d","e","f","g","h","i","ı","j","k","l","m","n","o","p","r",
                 "s","t","u","v","y","z","A","B","C","D","E","F","G","H","I","K","L","M",
                 "N","O","P","R","S","T","U","V","Y","Z","1","2","3","4","5","6","7","8","9"]
     for X in website:
         for control_X in list:
             if X == control_X:
                 return True
     return False

def lg(website):
    LW= Xch(website)
    if len (website)<= 3:
        length = True
    else:
        length = False
