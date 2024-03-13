api_response = {"first_name": "Muthuparvathi",
                "last_name" : "Muthukrishnan",
                 "age" : 28, "email":"parukrish.social@gmail.com",
                "password" : "test@123"}
print(api_response)

for k,v in api_response.items():
    print(k, '->', v)

api = api_response.get("age")
print(api)

#sets are mutable in nature
api_response["last_name"] = "M"
print(api_response)