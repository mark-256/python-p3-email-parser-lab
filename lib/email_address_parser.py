import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Split by comma and/or space (one or more)
        tokens = re.split(r'[,\s]+', self.email_string)

        # Email regex pattern (basic)
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        # Filter valid emails only and get unique set
        valid_emails = {token for token in tokens if email_pattern.match(token)}

        # Natural sort key helper to sort emails by user and number parts
        import re as _re
        
        def natural_key(email):
            user, domain = email.split('@')
            # Split the user part into digit and nondigit parts for natural sorting
            split_parts = _re.split(r'(\d+)', user)
            # Convert digit parts to int, others stay as string for sorting
            return [int(part) if part.isdigit() else part.lower() for part in split_parts] + [domain.lower()]

        # Return naturally sorted list using the custom key
        return sorted(valid_emails, key=natural_key)
