from EmailAll.modules.collect import Collect
from EmailAll.common.output import Output


class EmailAll:
    """
    EmailAll is a powerful Email Collect tool
    """

    def __init__(self, debug_only=False):
        self.domain = None
        self.output = Output()
        self.debug_only = debug_only

    def run(self, domain):
        self.domain = domain.lower().strip()
        if self.debug_only:
            return {"test": ["test@gmail.com", "test2@gmail.com"], "test2": ["test1@hotmail.com", "test2@hotmail.com"]}
        collect = Collect(self.domain)
        return collect.run()


if __name__ == "__main__":
    emailAll = EmailAll()
    result = emailAll.run("test.com")
