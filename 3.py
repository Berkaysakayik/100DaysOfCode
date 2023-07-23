email = input("Enter your mail: ").strip()

username = email [:email.index("@")]
domain = email [email.index("@") + 1:]

print (f"Your username {username} and domain {domain}")




temp = float(input("Enter your Fahrenheit temperature: "))

c = (temp - 32)*(5/9)

print(f"Your Fahrenheit to Celsius covering temperature is : {c}")