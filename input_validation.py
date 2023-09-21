#import re   #regular Expressions
from email_validator import validate_email, EmailNotValidError

def is_valid_email(email:str) -> bool:
    try:
        validate_email(email, check_deliverability=False, allow_quoted_local=True, allow_domain_literal=True)
        return True
    except EmailNotValidError as e:
        return False