from urllib.parse import urlunparse

lst = ['https', 'example.com', '/employees/name/', '', 'salary>=25000', '']
new_url = urlunparse(lst)
print ("URL:", new_url)





