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
from model import *


class Handler(BaseHandler):
    repo_required = False

    def get(self):
        redirect_url = self.maybe_redirect_jp_tier2_mobile()
        if redirect_url:
            return self.redirect(redirect_url)

        if not self.repo:
            return self.redirect('/personfinder/global/howitworks')

        # TODO(kpy): Cache more aggressively, before calling get_count.
        # To do this we need to put the Counter.get_count stuff in a callback;
        # see the corresponding TODO for resources.get_rendered().

        # Round off the count so people don't expect it to change every time
        # they add a record.
        person_count = Counter.get_count(self.repo, 'person.all')
        if person_count < 100:
            num_people = 0  # No approximate count will be displayed.
        else:
            # 100, 200, 300, etc.
            num_people = int(round(person_count, -2))

        self.render('start.html',
                    cache_seconds=1.0,
                    num_people=num_people,
                    seek_url=self.get_url('/query', role='seek'),
                    provide_url=self.get_url('/query', role='provide'))
