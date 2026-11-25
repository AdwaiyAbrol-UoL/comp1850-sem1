
import httpx

base_url = "https://dummyjson.com/"

content = "recipes/meal-type/snack"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

data = response.json()   # JSON data

for recipe in data['recipes']:  # Each recipe returned by the API
    print(recipe['name'], recipe['difficulty'])  # Recipe name and difficulty

#Q1:
# Below is the code to show that I altered the api_call.py file to get the answer for Q1 on the Worksheet for week1.8.

# import httpx
# import random
# base_url = "https://dummyjson.com/"
# content = "posts/1"
# url = base_url + content  # API request
# response = httpx.get(url)   # API call
# print(response.status_code)   # HTTP response
# content = response.json()   # JSON data
# print(content)

# number = random.choice([k for k in range(3,21,2)])
# print(number)


#Q2:
# Below is the code to show that I altered the api_call.py file to get the answer for Q2 on the Worksheet for week1.8.

# import httpx
# base_url = "https://dummyjson.com/"
# content = "products/search?q=apple"
# url = base_url + content  # API request
# response = httpx.get(url)   # API call
# print(response.status_code)   # HTTP response
# data = response.json()   # JSON data
# print(data['total'])   # Total number of products found


#Q7:
# Below is the code to show that I altered the api_call.py file to get the answer for Q7 on the Worksheet for week1.8.

# import httpx
# base_url = "https://dummyjson.com/"
# content = "posts/5"
# url = base_url + content  # API request
# response = httpx.get(url)   # API call
# print(response.status_code)   # HTTP response
# data = response.json()   # JSON data
# print(data) # The data returned from the API call
# print(data['reactions']['likes']) # The number of likes for the post, which are inside the reactions dictionary


#Q9: 
#Below is the code to show that I altered the api_call.py file to get the answer for Q9 on the Worksheet for week1.8.

# import httpx
# base_url = "https://dummyjson.com/"
# content = "recipes/meal-type/snack"
# url = base_url + content  # API request
# response = httpx.get(url)   # API call
# print(response.status_code)   # HTTP response
# data = response.json()   # JSON data
# for recipe in data['recipes']:  # Each recipe returned by the API
    # print(recipe['name'], recipe['difficulty'])  # Recipe name and difficulty