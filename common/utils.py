#!/usr/bin/python3
# coding=utf-8
# Author: @Tao.
import re
import json

def check_response(resp):
    """
    检查响应 输出非正常响应返回json的信息

    :param resp: 响应体
    :return: 是否正常响应
    """
    if resp.status_code == 200 and resp.content:
        return True
    return False


def match_emails(domain, html):
    """
    匹配邮箱
    :param domain:要配备邮箱的域名
    :param html: 爬取的网页
    :return: 网页解析的邮箱合集
    """
    # reg_emails = re.compile(r'[a-zA-Z0-9.\-_+#~!$&\',;=:]+' + '@' + '[a-zA-Z0-9.-]*' + domain.replace('www.', ''))
    reg_emails = re.compile(r'[a-zA-Z0-9.\-_]+' + '@' + '[a-zA-Z0-9.-]*' + domain.replace('www.', ''))
    temp = reg_emails.findall(html)
    emails = list(set(temp))
    true_emails = {str(email)[1:].lower().strip().replace('mailto:', '') if len(str(email)) > 1 and str(email)[0] == '.'
                   else len(str(email)) > 1 and str(email).lower().strip() for email in emails}
    return true_emails


def save_all(domain):
    """
    汇总 所有获取域名的邮箱保存至汇总json文件
    :param domain:
    :return:
    """
    filename = domain + '_All' + '.json'
    path = filename
    emails = set()
    for datas in settings.emails:
        for data in datas:
            emails.update(data['emails'])

    results = {
        'total': len(emails),
        'emails': list(emails)}
    with open(path, 'w', errors='ignore') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    logger.log('TRACE', f'Save the ALl Email results found by '
                        f'All module as a file')
