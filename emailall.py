from EmailAll.modules.collect import Collect
from EmailAll.common.output import Output

import random
import string


class EmailAll:
    """
    EmailAll is a powerful Email Collect tool
    """

    def __init__(self, debug_only=False):
        self.domain = None
        self.output = Output()
        self.debug_only = debug_only

    def _generate_random_email(self):
        # Generate a random email address with test number in curly braces
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        return f"test_{random_string}@{self.domain}"

    def run(self, domain):
        self.domain = domain.lower().strip()
        if self.debug_only:
            # Generate a random number of test email addresses
            results = {}
            for i in range(1, random.randint(2, 5)):  # Generate between 2 and 4 test email addresses
                results[f"test{i}"] = [self._generate_random_email() for _ in range(random.randint(1, 4))]  # Generate between 1 and 3 emails per test
            return results
        collect = Collect(self.domain)
        return collect.run()


if __name__ == "__main__":
    emailAll = EmailAll()
    result = emailAll.run("test.com")
