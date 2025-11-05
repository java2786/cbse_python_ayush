email = "arun_kumar@gmail.com"
email = "arun.kumar@gmail.com"
email = "arun@kumar@gmail.com"
email = "@arunkumargmail.com"
email = "arunkumar@gmail.com"
email = "arun_kumar876@gmail.com"
# email = "arun_kumar"
# email = "arun_kumar.gmail.com"
# email = "arun_kumar@gmail."
# email = "gamil.com@arun_kumar"


# email = "arun.kumar321@yahoo.co.in"

# ????


# 1. format -> should not start with special chars
# 2. format -> should not contain gap (space)
# 3. format -> should end with @gmail.com


# Basic validations

# 1. @ must present
if '@' not in email:
    print("Invalid email: '@' is missing")
# 2. . must present
elif '.' not in email:
    print("Invalid email: '.' is missing")
# 3. @ must occur only once
elif email.count('@')>1:
    print("Invalid email: More than one '@' found")
# 4. email must not start with @
elif email.startswith('@'):
    print("Invalid email: Starts with '@'")
# 5. email must not end with @
elif email.endswith('@'):
    print("Invalid email: Ends with '@'")
# 6. email must not end with .
elif email.endswith('.'):
    print("Invalid email: Ends with '.'")
# 7. email must not start with .
elif email.startswith('.'):
    print("Invalid email: Starts with '.'")
# 8. should contain domain name after @

else:
    # gmail.com@arun_kumar
    indexOfAt = email.index('@') # 9
    # while string after at, after 9
    domain = email[indexOfAt+1:]
    print(domain)
    if '.' not in domain:
        print("Invalid email: missing '.' in domain")
    elif domain.index('.')<2:
        print("Invalid email:")
    else:
        print(f"{email.upper()} is a valid email id")
    
