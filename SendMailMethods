import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def MailBot(cm, cpass, t, sub, att, p):
    # opens Email file then reads
    with open(p, 'r') as f:
        # Reads every line in file.
        for line in f:
            # Reads every word that's separated  by (|) and strips that information and Stores it in array.
            # Features.
            try:
                x = [line.split('|')]
                y = x[0]
                user_emails = y[0]  # user email is equal to the index 0 of the aray.
                name = y[1]  # name is equal to the 1st index of the array and.

                # transformation's.
                company_email = str(cm)  # company's email. is equal through the parameter cm passed from main.
                company_pass = str(cpass)  # company's pass word is equal through the parameter cpass passed from main.
                text = t  # text is equal through the parameter cpass passed from main.
                Path = str(att) # sets path equal to att

                # list's.
                list1 = list(text.split(" "))  # creates a list from text separating every word by spaces
                list_b = [word if word != '(name)' else f'{name}' for word in list1]  # looks for (name) in the text and replaces it with users name and updates list_b.
                list_to_str = ' '.join(map(str, list_b))  # this changes the list and combines updated list to look like text or paragraph(back to Text normal form).
                text = list_to_str  # sets text equal to the updated list

                # attachments.
                msg = MIMEMultipart()
                is_bot = str("(Do not reply)")  # is a do not reply msg
                msg['Subject'] = f'{sub}' # the subject of the email
                email_body = '{}\n\n\n{}'.format(text, is_bot)  # formats the body paragraph
                file = Path  # file is equal to a file path on pc.

                attachment = open(file, 'rb')  # opens file and reads it.

                extension = MIMEBase('application', 'octet-stream')

                extension.set_payload(attachment.read())  # sets file to be read
                encoders.encode_base64(extension)  # encodes it.
                extension.add_header('Content-Disposition', "attachment; filename= " + file)  # adds extension header.

                # email sender.
                msg.attach(MIMEText(email_body, 'plain'))  # attaches  email-body and sets write style to plain.
                msg.attach(extension)  # attaches extension witch is your file.
                final_msg = msg.as_string()  # converts all your attachments as a string
                MAILBOT = smtplib.SMTP('smtp.gmail.com', 587)  # gmails smtp server using port 587
                MAILBOT.starttls()  # starts server
                MAILBOT.login(company_email, company_pass)  # logs into account given correct account info
                MAILBOT.sendmail(company_email, user_emails, final_msg)  # sends the email from companys email to the users email and sends Final_msg.
            except IndexError as IE: #email error handeler
                print(IE)

