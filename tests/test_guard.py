# -*- coding: utf-8 -*-
#
# Copyright (c) 2016, Leigh McKenzie
# All rights reserved.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import pytest
from statechart import Guard, KwEvent


class GreaterThanZero(Guard):
    def check(self, event):
        if 'value' in event.kwargs and event.kwargs['value'] > 0:
            return True
        else:
            return False

class TestGuard:
    def test_abstract_instantiation_throws(self):
        with pytest.raises(TypeError):
            Guard()

    @pytest.mark.parametrize("event, expected", [(KwEvent(name='a', value=0), False), (KwEvent(name='a', value=1), True)])
    def test_guard_check(self, event, expected):
        guard = GreaterThanZero()
        assert guard.check(event) == expected
