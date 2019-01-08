# encoding: utf-8

import os
import logging
import ast
import yaml
import json
from ansible_core import Runner, ResultsCollector


logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY = os.path.join(BASE_DIR, 'ansible.host')
INVENTORY1 = os.path.join(BASE_DIR, 'ansible.1.host')


class AnsibleTask(object):
    def __init__(self):
        pass

    def run_translate_task(self):
        ansible_ssh_user = ''
        ansible_python_interpreter = '/usr/bin/python'
        ansible_ssh_private = '/home/wt/.ssh/id_rsa'
        hosts = INVENTORY
        hosts1 = INVENTORY1
        all_hosts = [hosts, hosts1]
        ip_list = ['218.241.108.38', '218.241.108.243']

        module_name = 'copy'
        module_args = "src=%s dest=%s" % ('/tmp/1.txt', '/tmp/')

        runner = Runner(resource=all_hosts, ip_list=ip_list,
                        module_name=module_name, module_args=module_args, ansible_vault_key='devops')
        runner.run()
        # 结果
        result = runner.get_result()
        # 成功
        succ = result['success']
        # 失败
        failed = result['failed']
        # 不可达
        unreachable = result['unreachable']
        print result
        return result


res = AnsibleTask()
res.run_translate_task()
