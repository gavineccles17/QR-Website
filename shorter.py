# import pyshorteners
# import os
#
# #
# API_CUTTLY_KEY = '05ef6c0d4cc22e63fbb418086f764ad9abebc'
#
# def get_short_url(url_business):
#     #print(['Shorteners.{}'.format(i) for i in dir(pyshorteners.Shorteners) if not i.startswith('__')])
#     # s = pyshorteners.Shortener(api_key=API_CUTTLY_KEY)
#     # url_short = s.cuttly.short(url_business)
#
#     s = pyshorteners.Shortener(Shorteners.TINYURL)
#     url_short = s.short('http://www.google.com')
#     # print(shorturl)
#     return url_short
#
# def expand_short_url(url_short):
#     s = pyshorteners.Shortener(api_key=API_CUTTLY_KEY)
#     url_business = s.cuttly.expand(url_short)
#     return url_businessk