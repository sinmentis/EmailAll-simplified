from modules.collect import Collect
from common.output import Output


class EmailAll:
    """
    EmailAll is a powerful Email Collect tool

    Example:
        python3 emailall.py --domain example.com run
    """

    def __init__(self, domain=None):
        self.domain = domain.lower().strip()  # 单条
        self.output = Output()  # 输出结果类

    def run(self):
        collect = Collect(self.domain)
        result = collect.run()
        return result


if __name__ == "__main__":
    emailAll = EmailAll("test.com")
    emailAll.run()
