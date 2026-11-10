# Utilities Features

class UtilitiesSystem:
    def __init__(self):
        pass

    def urlShortener(self, long_url):
        short_code = "lnk.ly/" + str(len(long_url) * 2)
        return short_code

    def sendMessage(self, recipient, message):
        print("Sending to:", recipient)
        print("Message:", message)
        return "Message Sent Successfully"

    def generateFakeData(self):
        fake_name = "Amber Castillo"
        fake_email = "amber@email.com"
        return fake_name, fake_email


if __name__ == "__main__":
    util = UtilitiesSystem()

    print("=== 1. URL SHORTENING ===")
    my_url = "https://www.schoolportal.edu.ph/student/dashboard/grades"
    result_url = util.urlShortener(my_url)
    print("Original:", my_url)
    print("Shortened:", result_url)

    print()  # line space

    print("=== 2. SMS AND MESSAGING ===")
    phone_num = "09123456789"
    text_msg = "Hello, reminder for our project meeting tomorrow."
    util.sendMessage(phone_num, text_msg)

    print()  # line space

    print("=== 3. FAKE DATA GENERATION ===")
    name, email = util.generateFakeData()
    print("Generated Name:", name)
    print("Generated Email:", email)

    print()  # line space