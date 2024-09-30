from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from source.services.abstract import AbstractService

import aiosmtplib


class SmtpService(AbstractService):
    def __init__(self, email: str, password: str, host: str = "smtp.yandex.ru"):
        super().__init__()
        self.email = email
        self.password = password
        self.host = host

        self._debug_level = 1

    async def send_mail(self, email_to: str, subject: str, text: str):
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = email_to
        msg["Subject"] = subject

        msg.attach(MIMEText(text, "htmp"))
        self.logger.debug("Send mail message", msg=msg, host=self.host)

        await aiosmtplib.send(
            msg,
            hostname=self.host,
            username=self.email,
            password=self.password,
        )
