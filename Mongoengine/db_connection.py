from mongoengine import connect

username = "edelsas"
password = "Nightwing2204"
host = "nightwing2204cecs-323-fall-2024.am0tq.mongodb.net"  
database = "CECS-323-Fall-2024"  

mongo_url = "mongodb+srv://edelsas:Nightwing2204@cecs-323-fall-2024.am0tq.mongodb.net/?retryWrites=true&w=majority&appName=CECS-323-Fall-2024"

connect(host=mongo_url)

print(f"Connected to MongoDB database")
