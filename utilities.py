# SIA 2 Mini Project - Utilities Features

class UtilitiesSystem:
    def __init__(self):
        pass

    # 1. URL Shortening Feature
    def urlShortener(self, long_url):
        short_code = "lnk.ly/" + str(len(long_url) * 2)
        return short_code

    # 2. SMS and Messaging Feature
    def sendMessage(self, recipient, message):
        print("Sending to:", recipient)
        print("Message:", message)
        return "Message Sent Successfully"

    # 3. Fake Data Generation Feature
    def generateFakeData(self):
        fake_name = "Juan Dela Cruz"
        fake_email = "juan.delacruz@email.com"
        return fake_name, fake_email


# Paggawa ng object para sa Utilities
util = UtilitiesSystem()

print("=== 1. URL SHORTENING ===")
my_url = "https://www.schoolportal.edu.ph/student/dashboard/grades"
result_url = util.urlShortener(my_url)
print("Original:", my_url)
print("Shortened:", result_url)

print() # line space

print("=== 2. SMS AND MESSAGING ===")
phone_num = "09123456789"
text_msg = "Hello, reminder for our project meeting tomorrow."
util.sendMessage(phone_num, text_msg)

print() # line space

print("=== 3. FAKE DATA GENERATION ===")
name, email = util.generateFakeData()
print("Generated Name:", name)
print("Generated Email:", email)

print() # line space

