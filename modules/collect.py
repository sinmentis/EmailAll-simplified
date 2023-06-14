#!/usr/bin/python3
# coding=utf-8
# Author: @Tao.

import threading
import importlib

from EmailAll.config.log import logger
import EmailAll.config.setting as settings


class Collect:

    def __init__(self, domain):
        self.domain = domain
        self.modules = []
        self.collect_funcs = []
        self.results = {}

    def get_mod(self):
        """
        Get modules
        """
        modules = ['certificates', 'check', 'datasets',
                   'dnsquery', 'intelligence', 'search']
        for module in modules:
            module_path = settings.modules_storage_dir.joinpath(module)
            for path in module_path.rglob('*.py'):
                import_module = f'EmailAll.modules.{module}.{path.stem}'
                self.modules.append(import_module)

    def import_func(self):
        """
        Import do function
        """
        for module in self.modules:
            name = module.split('.')[-1]
            import_object = importlib.import_module(module)
            func = getattr(import_object, 'run')
            self.collect_funcs.append([func, name])

    def run_func(self, func, func_name):
        result = func(self.domain)
        self.results[func_name] = result

    def run(self):
        """
            Class entrance
        """
        self.get_mod()
        self.import_func()

        threads = []

        for func_obj, func_name in self.collect_funcs:
            thread = threading.Thread(target=self.run_func, name=func_name, args=(func_obj, func_name,))
            threads.append(thread)

        for t in threads:
            t.start()

        for t in threads:
            t.join(6*60)

        for t in threads:
            if t.is_alive():
                logger.log('ALERT', f'{t.name} module thread timed out')

        return self.results
