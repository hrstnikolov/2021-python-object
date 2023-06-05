class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        pass

    def __validate_domain(self, domain):
        pass
