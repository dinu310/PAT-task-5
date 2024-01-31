import re

def validate_email(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email) is not None

def validate_bangladesh_mobile(mobile):
    regex = r'^01[15-9]\d{8}$'
    return re.search(regex, mobile) is not None

def validate_usa_telephone(telephone):
    regex = r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    return re.search(regex, telephone) is not None

def validate_password(password):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%*?&])[A-Za-z\d@$!%*#?&]{16}$'
    return re.search(regex, password) is not None


print(validate_email("example@example.com"))  # True
print(validate_email("example@example"))  # False
print(validate_bangladesh_mobile("01512345678"))  # True
print(validate_bangladesh_mobile("0112345678"))  # False
print(validate_usa_telephone("123-45-7890"))  # False
print(validate_usa_telephone("+1 123 456 7890"))  # True
print(validate_password("Password12345!@#")) #True
print(validate_password("password12345!@#")) #False

