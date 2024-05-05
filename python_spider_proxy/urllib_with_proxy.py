# -*- coding:utf-8 -*-
# Created on 2023/11/15

import urllib.request

proxy_support = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:7890',
                                             'https': 'http://127.0.0.1:7890'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
