import json
import os
import datetime
from app.modules import utility_email


class ErrorPolicy:
    def __init__(self, file_path):
        self.errors_structure = dict()
        self.file_path = file_path
        self.time_format = "%c"
        if os.path.isfile(file_path):
            json_file = open(file_path, "r")
            self.errors_structure = json.load(json_file)
            json_file.close()

    def save_changes(self):
        with open(self.file_path, 'w') as outfile:
            json.dump(self.errors_structure, outfile, indent=4, sort_keys=True)

    def should_send_email(self, error_id):
        should_send_email = False
        if self.errors_structure is None or error_id not in self.errors_structure:
            should_send_email = True
        else:
            previous_time = datetime.datetime.strptime(self.errors_structure[error_id], self.time_format)
            if (datetime.datetime.now() - previous_time).days >= 1:
                should_send_email = True

        return should_send_email

    def process_error(self, recipient, subject, error_message):
        if self.should_send_email(subject):
            self.errors_structure[subject] = datetime.datetime.now().strftime(self.time_format)
            self.save_changes()
            utility_email.send_email(recipient, subject, error_message)
