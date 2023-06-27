print("GENERATOR \n1.Password Generator \n2.QR code Generator \n3.Text-to-Voice
Generator \n4.Exit" )
while True:
n = int(input("Enter your choice (1 / 2 / 3 / 4):"))
while (n==1):
import random
pass_len = int(input("Enter the length of the password: "))
pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
password = "".join(random.sample(pass_data, pass_len))
print(password)
break;
if (n == 2):
import qrcode
link = input("Enter link :")
img = qrcode.make(link)
img.save("test.png")
elif(n==3):
from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = 'en'
Text = input("Enter text which you want to convert into audio file: ")
sp = gTTS(text=Text, lang=language, slow=False)
sp.save(audio)
playsound(audio)
elif (n==4):
print("Thank you for using the generator.")
print("MADE BY :")
print("Madhi Vathani and Naafiah Fathima")
break;
