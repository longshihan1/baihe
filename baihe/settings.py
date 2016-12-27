# -*- coding: utf-8 -*-

# Scrapy settings for baihe project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'baihe'

SPIDER_MODULES = ['baihe.spiders']
NEWSPIDER_MODULE = 'baihe.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baihe (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/49.0.2623.87 Safari/537.36'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
  'Accept-Encoding': 'gzip, deflate, sdch',
  'Connection': 'keep-alive',
  '':'',
  'cookie':'accessID=20161221181158333740; Hm_lvt_5497f3e5cf06014777f01fb0307e58f4=1482315119; tempID=1381023784; OnceLoginWEB=142964501; LoginEmail=18119500180%40mobile.baihe.com; userID=142964501; spmUserID=142964501; _fmdata=9B7ABFF80CB73F41B2B2E923116F96E72FE3005C98DA23CEF4705FFE9F6504E8ED89BAE465DD02C18FB9E9031D04B914AFA98BEFE3673675; accessToken=BH1482812396727110301; 142964501_log=1; noticeEvent_142964501=27; lastLoginDate=2016-12-27+13%3A29%3A54; __auc=bdfc897815920e14bd3d81909ed; channel=baidu; code=313012-00003; cookie_pcc=1%7C%7Cbaidu%7C%7C313012-00003%7C%7Chttps%3A//www.baidu.com/baidu.php%3Fsc.0f0000aPftK-mFJ6dUIhrpGrJwXqTVH8HmHw5W-upPaXGc6uZUIITZWGtr6SGExvhJloTZmyWI04T3RtzfMdCsWPxJIRTZ1LTLCRdW5OcAefS48EFB7pfKeACkh8sTO2Liepa9zKAgEdhzkwK_PsYEnTY9g0MemQ59n-lDCx7md8NYj1V0.7Y_aq-qiRfgGCnYDkYcQYYApamlZQDM6C_kgmvIiXxxAlBSZfkgdSAGh2FP7BqM76lOal4QZAEWugb1vyyyTNBmLerrOI3tTMQRze-kl-9h9mL45ZBC.U1Yk0ZDq_Phl1sKY5Uju8_t0pyYqnWcd0ATqTZnz0ZNG5yF9pywdUAY0TA-b5Hc0mv-b5Hn4r0KVIjY1nHnvg1DsnHIxnW0vn-tknjD1g1Dsn1PxnH0krNt1PW0k0AVG5H00TMfqnHc10ANGujY0mhbqnW0Y0AdW5HKxnWb1nHTkPjnvg1csnNtknW04P1nzPH7xP1nYnjD1rHczg1c4n1DLnHfYPNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0KEIhsqnWmvridbX-tzPWm4yadbX-tdrjfsQH7xrjRvQHKxrjR4QHD0mycqn7ts0ANzu1Ys0ZKs5HTsPjmzPjnLnfK8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0IZN15HDvn16vPWnYP163PHf1n1fYnW6k0ZF-TgfqnHf3nW61nHc1rH0LPfK1pyfquhRdmvnYPWDsnj0kuAu9P0KWTvYqfbckfW0vfHwawj97nWPKwfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn7tsg100uZwGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00XMK_Ignqn0K9uAu_myTqnfKWThnqnH61rHf%26ck%3D2430.9.64.285.142.357.359.144%26shh%3Dwww.baidu.com%26sht%3D98395732_hao_pg%26us%3D1.0.1.0.0.0.0.0%26ie%3Dutf-8%26f%3D8%26srcqid%3D532580034255460372%26tn%3D98395732_hao_pg%26wd%3D%25E7%2599%25BE%25E5%2590%2588%26oq%3D%25E7%2599%25BE%25E5%2590%2588%26rqlang%3Dcn%26sc%3DUWY4rjn4PHT1n-qCmyqxTAThIjYkPj6zrj0zPHnYP1TYFhnqpA7EnHc1Fh7W5HcYPHfYnHRsnWb%26ssl_sample%3Dnormal%26bc%3D110101; AuthCheckStatusCookie=398B56475FD2BE43ACE69D8D3295505A14D1D3015978705726A127B203C4931405E9D878DCC812E7; Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d=1482315148,1482719471,1482812397; Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d=1482831249; nTalk_CACHE_DATA={uid:kf_9847_ISME9754_guestTEMP3CD3-A879-14}; NTKF_T2D_CLIENTID=guestTEMP3CD3-A879-1428-4731-20E0C0A56EB1'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'baihe.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'baihe.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'baihe.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.curdir))

MONGO_URI = 'mongodb://localhost:27017'

ITEM_PIPELINES = {
    'baihe.pipelines.BaihePipeline': 500,
}

BROKER_URL = 'amqp://guest:guest@localhost:5672//'