import secrets,string
letters=string.ascii_letters
digits=string.digits
special_chars=string.punctuation
Alphabets=letters+digits+special_chars
pwd_length=12
pwd=''
for i in range(pwd_length):
    pwd +=''.join(secrets.choice(Alphabets))
print(pwd)
