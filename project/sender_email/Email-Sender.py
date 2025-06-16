import smtplib
try:
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()

    ##receiver email
    receiver_email = input("input the receiver email here")  

    ##mail credentials
    sender_email = "akshatjangid9@gmail.com"
    password = "ldgc hrsx esad fpbp"

    ##login
    server.login(sender_email, password)

    ##sending mail
    subject = input("enter the subject of the mail: ")
    body = input("enter the body of the mail: ")
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")

    server.quit()
except Exception as e:
    print("An error occurred: ", e)