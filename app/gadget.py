#!/usr/bin/python2.5
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from utils import *

class Gadget(Handler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/xml'
    self.render('templates/gadget.xml', domain=self.domain,
                params=self.params, vars=self.vars)

if __name__ == '__main__':
  run([('/gadget', Gadget)], debug=False)
