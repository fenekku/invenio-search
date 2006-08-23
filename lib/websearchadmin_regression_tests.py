# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.  
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""WebSearch Admin Regression Test Suite."""

__revision__ = "$Id$"

import unittest

from invenio.config import weburl
from invenio.testutils import make_test_suite, warn_user_about_tests_and_run, \
                              test_web_page_content, merge_error_messages

class WebSearchAdminWebPagesAvailabilityTest(unittest.TestCase):
    """Check WebSearch Admin web pages whether they are up or not."""

    def test_websearch_admin_interface_pages_availability(self):
        """websearchadmin - availability of WebSearch Admin interface pages""" 

        baseurl = weburl + '/admin/websearch/websearchadmin.py'

        _exports = ['',
                    '?mtype=perform_showall',
                    '?mtype=perform_addcollection',
                    '?mtype=perform_addcollectiontotree',
                    '?mtype=perform_modifycollectiontree',
                    '?mtype=perform_checkwebcollstatus',
                    '?mtype=perform_checkcollectionstatus',]
        
        error_messages = []
        for url in [baseurl + page for page in _exports]:
            # first try as guest:
            error_messages.extend(test_web_page_content(url,
                                                        username='guest',
                                                        expected_text=
                                                        'Authorization failure'))
            # then try as admin:
            error_messages.extend(test_web_page_content(url,
                                                        username='admin'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_websearch_admin_guide_availability(self):
        """websearchadmin - availability of WebSearch Admin guide pages"""

        url = weburl + '/admin/websearch/guide.html'
        error_messages = test_web_page_content(url)
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

test_suite = make_test_suite(WebSearchAdminWebPagesAvailabilityTest)

if __name__ == "__main__":
    warn_user_about_tests_and_run(test_suite)