# -*- coding: utf-8 -*-

from module.plugins.internal.DeadHoster import DeadHoster, create_getInfo


class BillionuploadsCom(DeadHoster):
    __name__    = "BillionuploadsCom"
    __type__    = "hoster"
    __version__ = "0.06"

    __pattern__ = r'http://(?:www\.)?billionuploads\.com/\w{12}'

    __description__ = """Billionuploads.com hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


getInfo = create_getInfo(BillionuploadsCom)
