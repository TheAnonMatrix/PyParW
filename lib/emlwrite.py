#!/usr/bin/env python
# -*- coding: UTF-8 -*

import os
import hashlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders


fp = open(path, 'rb')
msg = MIMEBase(maintype, subtype)
msg.set_payload(fp.read())
fp.close()
encoders.encode_base64(msg)

class EMLWriter(object):
    """Writing eml files"""
    def __init__(self, mail):
        self.mail = mail
        self.path = os.getcwd()

    def write(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.mail["Title"]
        msg["From"] = self.mail["From"]
        msg['To'] = self.mail["To"]
        msg['Date'] = self.mail['Date']
        msg.attach(MIMEText(self.mail["Body"]))
        if self.mail['Attachment']:
            for i in self.mail:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(i)
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename=Attachment')
                msg.attach(part)


    def mailsave(self):
        pass

    def file_name(self):
        if not self.mail['Email-ID']:
            self.mail['Email-ID'] = self.mail['Date']
        sha1_hash = hashlib.sha1("%s/%s/%s/%s" % (self.mail['From'], self.mail['To'], self.mail['Email-ID'], self.mail["Title"])).hexdigest()
        return sha1_hash