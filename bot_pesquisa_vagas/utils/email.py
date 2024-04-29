import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

def enviar_email():  
    corpo_email = """
    <p>Robô de Vagas</p>
    <p>Olá, Novas Vagas Disponíveis</p>
    <p>Dê uma olhada!</p>
    """

    msg = MIMEMultipart()
    msg['Subject'] = "Vagas RPA"
    msg['From'] = os.getenv("email_gmail")
    destinatarios = [f'{os.getenv("primeiro_destinatario")}', f'{os.getenv("segundo_destinatario")}', f'{os.getenv("terceiro_destinatario")}']
    msg['To'] = ", ".join(destinatarios)
    password = os.getenv("senha_gmail")
    
    corpo_mime = MIMEText(corpo_email, 'html')
    msg.attach(corpo_mime)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], destinatarios, msg.as_string())
    print('Email enviado')

enviar_email()
