#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

USER_REGEX = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_REGEX = re.compile(r"^.{3,20}$")
EMAIL_REGEX = re.compile(r"^[\S]+@[\S]+.[\S]+$")

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
    .error {
        color: red;
    }
    </style>
</head>
<body>
"""

main_content = """
    <h1>Signup</h1>
    <form method="post">
        <table>
            <tbody>
                <tr>
                    <td>
                        <label>Username</label>
                    </td>
                    <td>
                        <input type="text" name="username" value required>
                        <span class="error"</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label> Password</label>
                    </td>
                    <td>
                        <input type="password" name="password" value required>
                        <span class="error"</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label> Verify Password</label>
                    </td>
                    <td>
                        <input type="password" name="verify" value required>
                        <span class="error"</span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label> Email (optional)</label>
                    </td>
                    <td>
                        <input type="email" name="email">
                        <span class="error"</span>
                    </td>
                </tr>
            </tbody>
        </table>
        <input type="submit">
    </form>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def valid_username(username):
    if username:
        if USER_REGEX.match(username):
            return username

def valid_password(password, verify):
    if password and verify:
        if password == verify:
            if PASSWORD_REGEX.match(password):
                return password

def valid_email(email):
    if email:
        if EMAIL_REGEX.match(email):
            return email


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = page_header + main_content + page_footer
        self.response.write(content)

    def post(self):
        input_username = self.request.get('username')
        input_password = self.request.get('password')
        input_verify_password = self.request.get('verify')
        input_email = self.request.get('email')

        username = valid_username(input_username)
        password = valid_password(input_password, input_verify_password)
        email = valid_email(input_email)

        if not (username and password and email):
            content = page_header + main_content + "Incorrect input" + page_footer
            self.response.write(content)
            #self.write.form("Incorrect input")
        else:
            welcome_url = '/welcome?u={u}'.format(u=username)
            self.redirect(welcome_url)
#            self.redirect("/welcome")

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        content = 'Welcome, ' + self.request.get("u") + '!'
        self.response.write(content)

        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
