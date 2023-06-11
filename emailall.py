from common import utils
from modules.collect import Collect
from common.output import Output

class EmailAll:
    """
    EmailAll is a powerful Email Collect tool

    Example:
        python3 emailall.py --domain example.com run
    """

    def __init__(self, domain=None):
        self.domain = domain    # 单条
        self.output = Output()  # 输出结果类

    def main(self):
        collect = Collect(self.domain)
        collect.run()
        utils.save_all(self.domain)

    def run(self):
        self.domain = self.domain.lower().strip()
        self.main()
        self.output.run(self.domain)
