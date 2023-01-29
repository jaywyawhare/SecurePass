import os
import hibpwned

my_app = hibpwned.Pwned("test@example.com", "My_App", "My_API_Key")
password = my_app.search_password("Arinjay1")

if password:
    print("Password is pwned")
else:
    print("Password is not pwned")
