#!/usr/bin/env python3

import datetime
import os
import reports
import emails

current_date = datetime.datetime.today().strftime('%Y-%m-%d')

"""
Once you define the generate_email and send_email methods
 call the methods under the main method after creating the PDF report:
 """


def generate_pdf(path):
    report_pdf_format = ""

    for filename in os.listdir(description_path):
        if filename.endswith('.txt'):
            with open(path + filename,'r') as file:
                line = file.readlines()
                name = line[0].strip()
                weight = line[1].strip()

                report_pdf_format += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return report_pdf_format


if __name__ == "__main__":
    description_path = "supplier-data/descriptions/"
    title = "Process Updated on " + current_date
    # generate the package for pdf body
    info = generate_pdf(description_path)
    reports.generate_report("/tmp/processed.pdf", title, info)

    # generate email information
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    # generate email for the online fruit store report and pdf attachment
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)

