from email_address_parser import EmailAddressParser

class TestEmailAddressParserAdditional:
    def test_empty_string(self):
        parser = EmailAddressParser("")
        assert parser.parse() == []

    def test_duplicates(self):
        parser = EmailAddressParser("a@a.com,a@a.com a@a.com")
        assert parser.parse() == ["a@a.com"]

    def test_multiple_separators(self):
        parser = EmailAddressParser("a@a.com,,  , b@b.com   c@c.com")
        assert parser.parse() == ["a@a.com", "b@b.com", "c@c.com"]

    def test_invalid_emails_mixed(self):
        parser = EmailAddressParser("a@a.com, invalid, example.com, b@b.com")
        assert parser.parse() == ["a@a.com", "b@b.com"]

    def test_case_sensitivity(self):
        parser = EmailAddressParser("A@a.com a@a.com")
        # Current implementation treats different cases as unique, so sorted list includes both
        assert parser.parse() == ["A@a.com", "a@a.com"]

    def test_large_input(self):
        emails = ", ".join([f"user{i}@test.com" for i in range(1000)])
        parser = EmailAddressParser(emails)
        parsed = parser.parse()
        expected = [f"user{i}@test.com" for i in range(1000)]
        assert parsed == expected
