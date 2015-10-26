# -*- encoding: utf-8 -*-
"""Test class for Login UI"""

from robottelo.helpers import gen_string
from robottelo.test import UITestCase


def invalid_credentials():
    "Returns a list of invalid credentials"
    return [
        {u'login': 'admin', u'pass': ''},
        {u'login': '', u'pass': 'mypassword'},
        {u'login': '', u'pass': ''},
        {u'login': gen_string('alpha', 300), u'pass': ''},
        {u'login': gen_string('alpha', 300),
         u'pass': gen_string('alpha', 300)},
    ]


class Login(UITestCase):
    """Implements the login tests rom UI"""

    def test_successful_login(self):
        """@Test: Login as an admin user

        @Feature: Login - Positive

        @Assert: Successfully logged in as an admin user

        """
        self.login.login(self.katello_user, self.katello_passwd)
        self.assertTrue(self.login.is_logged())

    def test_failed_login(self):
        """@Test: Login into application using invalid credentials

        @Feature: Login - Negative

        @Assert: Fails to login

        """
        for test_data in invalid_credentials():
            with self.subTest(test_data):
                self.login.login(test_data['login'], test_data['pass'])
                self.assertFalse(self.login.is_logged())
