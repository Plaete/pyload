# -*- coding: utf-8 -*-

from __future__ import with_statement

import MultipartPostHandler
import re
import urllib2

from module.plugins.Container import Container
from module.utils import fs_encode, save_join


class CCF(Container):
    __name__    = "CCF"
    __type__    = "container"
    __version__ = "0.23"

    __pattern__ = r'.+\.ccf$'

    __description__ = """CCF container decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("Willnix", "Willnix@pyload.org"),
                       ("Walter Purcaro", "vuolter@gmail.com")]


    def decrypt(self, pyfile):
        fs_filename = fs_encode(pyfile.url.strip())
        opener      = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)

        dlc_content = opener.open('http://service.jdownloader.net/dlcrypt/getDLC.php',
                                  {'src'     : "ccf",
                                   'filename': "test.ccf",
                                   'upload'  : open(fs_filename, "rb")}).read()

        download_folder = self.config['general']['download_folder']
        dlc_file        = save_join(download_folder, "tmp_%s.dlc" % pyfile.name)

        try:
            dlc = re.search(r'<dlc>(.+)</dlc>', dlc_content, re.S).group(1).decode('base64')

        except AttributeError:
            self.fail(_("Container is corrupted"))

        with open(dlc_file, "w") as tempdlc:
            tempdlc.write(dlc)

        self.urls = [dlc_file]
