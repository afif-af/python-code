# from pathlib import Path
# path = Path('Python code\Beggining\pi_digits.txt')
# contents = path.read_text(encoding='utf-8')
# contents = contents.rstrip()
# lines = contents.splitlines()
# for line in lines:
#         print(line)
# print(contents)
#
# from pathlib import Path
# import json
# def get_stored_username(path):
#     """Get stored username if available."""
#     Files and Exceptions 205
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None
# def greet_user():
#
#     path = Path('username.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
#
# greet_user()