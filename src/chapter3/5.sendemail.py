from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
sender = "ram.damarla@gmail.com"
username = "ram.damarla@gmail.com"
password = input("Password: ")
host = "smtp.gmail.com"
port = 587

recipient = input("Student email: ")
score = int(input("Score: "))
body = "Your score on the last exam is " + str(score) + "\n"
if score <= 50:
    body += "To do better next time, why not visit the tutoring center?"
elif score >= 90:
    body += "Fantastic job! Keep it up."

msg = MIMEMultipart()
msg.add_header("From", sender)
msg.add_header("To", recipient)
msg.add_header("Subject", "Exam score")
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()
