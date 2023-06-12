from modules.collect import Collect
from common.output import Output


class EmailAll:
    """
    EmailAll is a powerful Email Collect tool
    """

    def __init__(self):
        self.domain = None
        self.output = Output()

    def run(self, domain):
        self.domain = domain.lower().strip()
        collect = Collect(self.domain)
        result = collect.run()
        return result


if __name__ == "__main__":
    emailAll = EmailAll()
    result = emailAll.run("test.com")
