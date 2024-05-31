# your code goes here!
import re


class EmailAddressParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def parse(self):
        
        parts = re.split(r'[,\s]+', self.input_string)
        

        emails = [part.strip() for part in parts if re.match(r'^[^@]+@[^@]+\.[^@]+$', part.strip())]
        

        return list(reversed(emails)) if emails else []
