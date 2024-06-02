import os
import sqlite3

# Example of hardcoded credentials
username = "admin"
password = "supersecretpassword123"

# Example of a potentially unsafe function (eval)
def run_code(code):
    eval(code)

# Example of SQL Injection vulnerability
def get_user_info(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

# Example of storing sensitive data insecurely
def save_credentials_to_file(username, password):
    with open("credentials.txt", "w") as file:
        file.write(f"Username: {username}\nPassword: {password}")

if __name__ == "__main__":
    # Run the unsafe eval function
    user_input = "print('This is unsafe!')"
    run_code(user_input)

    # Retrieve user information with potential SQL injection
    user_info = get_user_info(1)
    print(user_info)

    # Save credentials to a file insecurely
    save_credentials_to_file(username, password)
