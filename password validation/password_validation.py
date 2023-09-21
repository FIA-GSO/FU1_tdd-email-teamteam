def is_valid_password(password: str):
    passwordLaenge = len(password)
    
    if(passwordLaenge >= 8 and passwordLaenge <= 12):
        return shortPasswordCheck(password)   
    
    if(passwordLaenge >= 25):
        return longPasswordCheck(password)    

    return False

def shortPasswordCheck(password: str):          
    checkTypes = checkPassword4CharTypes(password, 4)
    if(checkTypes is False):
        return False

    return True

def longPasswordCheck(password: str):
    checkTypes = checkPassword4CharTypes(password,2)
    if(checkTypes is False):
       return False
    
    return True

def checkPassword4CharTypes(password: str, requiredTypes: int):
    hasNumber = 0
    hasLowercase = 0
    hasUppercase = 0
    hasSpecialcase = 0

    for char in password:
        if(hasNumber is 0 and char.isdigit()):
            hasNumber = 1
        if(hasLowercase is 0 and char.islower()):
            hasLowercase = 1
        if(hasUppercase is 0 and char.isupper()):
            hasUppercase = 1
        if(hasSpecialcase is 0 and not char.isalnum()):
            hasSpecialcase = 1

    typesFound = hasNumber + hasLowercase + hasUppercase + hasSpecialcase
    return typesFound >= requiredTypes