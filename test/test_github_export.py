# Copyright (C) 2013 Steve Milner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import httplib2
import json
import mock

from . import TestCase, export_from_github


# Setup mocking
httplib2.Http.request = mock.MagicMock(httplib2.Http.request)
httplib2.Http.request.return_value = (None, json.dumps([{
    "url": "https://api.github.com/repos/USERNAME/REPONAME/issues/1",
    "html_url": "https://github.com/USERNAME/REPONAME/issues/1",
    "id": 23819707,
    "number": 1,
    "title": "Test issue",
    "user": {
        "login": "notarealperson",
    },
    "labels": [],
    "state": "open",
    "assignee": None,
    "milestone": None,
    "comments": 2,
    "created_at": "2013-12-05T21:37:16Z",
    "updated_at": "2013-12-06T01:16:28Z",
    "closed_at": None,
    "pull_request": {
        "html_url": None,
        "diff_url": None,
        "patch_url": None,
    },
    "body": "Test issue body",
}]))


class TestGithubExport(TestCase):
    """
    Tests for the github issues export.
    """

    def setUp(self):
        """
        Reset the mock every time a test runs.
        """
        httplib2.Http.request.reset_mock()

    def test_export_with_expected_input(self):
        """
        Verify that requests for github data export execute as expected.
        """
        result = export_from_github('USERNAME', 'REPONAME', 360)
        assert type(result) is list
        assert len(result) == 1
        assert httplib2.Http.request.call_count == 1
        print httplib2.Http.request.call_args
        daysago = (datetime.datetime.now() - datetime.timedelta(
            360)).strftime('%Y-%m-%d')
        expected_url = ('https://api.github.com/repos/USERNAME/REPONAME/'
                        'issues?state=open&since=' + daysago)
        httplib2.Http.request.assert_called_with(expected_url)

    def test_export_with_bad_input(self):
        self.assertRaises(TypeError, export_from_github)
        self.assertRaises(TypeError, export_from_github, 'USERNAME')
        self.assertRaises(
            TypeError, export_from_github, 'USERNAME', 'REPONAME')
        self.assertRaises(TypeError, export_from_github, repo='REPONAME')
