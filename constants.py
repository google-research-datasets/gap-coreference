#!/usr/bin/python
#
# Copyright 2018 Google LLC
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

"""Constants.
"""

from enum import Enum


class Gender(Enum):
  UNKNOWN = 0
  MASCULINE = 1
  FEMININE = 2


# Mapping of (lowercased) pronoun form to gender value. Note that reflexives
# are not included in GAP, so do not appear here.
PRONOUNS = {
    'she': Gender.FEMININE,
    'her': Gender.FEMININE,
    'hers': Gender.FEMININE,
    'he': Gender.MASCULINE,
    'his': Gender.MASCULINE,
    'him': Gender.MASCULINE,
}

# Fieldnames used in the gold dataset .tsv file.
GOLD_FIELDNAMES = [
    'ID', 'Text', 'Pronoun', 'Pronoun-offset', 'A', 'A-offset', 'A-coref', 'B',
    'B-offset', 'B-coref', 'URL'
]

# Fieldnames expected in system output .tsv files.
SYSTEM_FIELDNAMES = ['ID', 'A-coref', 'B-coref']
