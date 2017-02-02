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
    <form method="post" action="/welcome">
        <h1>Signup</h1>
        <label> Username
            <input type="text" name="username">
        </label>
        <br>
        <label> Password
            <input type="password" name="password">
        </label>
        <br>
        <label> Verify Password
            <input type="password" name="verify">
        </label>
        <br>
        <label> Email (optional)
            <input type="email" name="email">
        </label>
        <br>
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
        return month_abbvs.get(username)

def valid_password(password, verify):
    if password and verify:
        if password == verify:
            return password

def valid_email(email):
    if email:
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
        email = valid_password(input_password)

        if not (username and password and email):
            self.write.form("Incorrect input")
        else:
            self.redirect("/welcome")

class WelcomeHandler(webapp2.RequestHandler):
    def post(self):
        content = 'Welcome, ' + self.request.get("username") + '!'
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
