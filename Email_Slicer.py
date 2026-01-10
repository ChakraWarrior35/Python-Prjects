def email_slicer(email):
    try:
        username, domain = email.split('@')
        domain_name, domain_extension = domain.split('.')
        return {
            'username': username,
            'domain_name': domain_name,
            'domain_extension': domain_extension
        }
    except ValueError:
        return "Invalid email format. Please provide a valid email address."
if __name__ == "__main__":
    email = input("Enter your email address: ")
    result = email_slicer(email)
    if isinstance(result, dict):
        print("Username:", result['username'])
        print("Domain Name:", result['domain_name'])
        print("Domain Extension:", result['domain_extension'])
    else:
        print(result)