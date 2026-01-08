# -*- coding:utf-8 -*-
#
# Copyright (C) 2018 sthoo <sth201807@gmail.com>
#
# Support: Report an issue at https://github.com/sth2018/FastWordQuery/issues
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version; http://www.gnu.org/copyleft/gpl.html.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import importlib.util
from collections import defaultdict

_local_hooks = defaultdict(list)

_gui_hooks_spec = importlib.util.find_spec("aqt.gui_hooks")
if _gui_hooks_spec:
    from aqt import gui_hooks as _gui_hooks
else:
    _gui_hooks = None

_anki_hooks_spec = importlib.util.find_spec("anki.hooks")
if _anki_hooks_spec:
    from anki import hooks as _anki_hooks
    _anki_add_hook = _anki_hooks.addHook
    _anki_rem_hook = _anki_hooks.remHook
    _anki_run_hook = _anki_hooks.runHook
    _anki_wrap = _anki_hooks.wrap
else:
    _anki_add_hook = None
    _anki_rem_hook = None
    _anki_run_hook = None
    _anki_wrap = None

_HOOK_MAP = {
    "profileLoaded": "profile_did_open",
    "browser.setupMenus": "browser_menus_did_init",
    "EditorWebView.contextMenuEvent": "editor_will_show_context_menu",
}


def add_local_hook(name, func):
    _local_hooks[name].append(func)


def rem_local_hook(name, func):
    if func in _local_hooks.get(name, []):
        _local_hooks[name].remove(func)


def run_local_hook(name, *args, **kwargs):
    for func in list(_local_hooks.get(name, [])):
        func(*args, **kwargs)


def add_anki_hook(name, func):
    if _gui_hooks:
        hook_attr = _HOOK_MAP.get(name)
        if hook_attr and hasattr(_gui_hooks, hook_attr):
            getattr(_gui_hooks, hook_attr).append(func)
            return
    if _anki_add_hook:
        _anki_add_hook(name, func)


def rem_anki_hook(name, func):
    if _gui_hooks:
        hook_attr = _HOOK_MAP.get(name)
        if hook_attr and hasattr(_gui_hooks, hook_attr):
            hook = getattr(_gui_hooks, hook_attr)
            if func in hook:
                hook.remove(func)
            return
    if _anki_rem_hook:
        _anki_rem_hook(name, func)


def run_anki_hook(name, *args, **kwargs):
    if _anki_run_hook:
        _anki_run_hook(name, *args, **kwargs)


def wrap(old, new, pos="after"):
    if _anki_wrap:
        return _anki_wrap(old, new, pos)

    def _wrapped(*args, **kwargs):
        if pos == "before":
            new(*args, **kwargs)
            return old(*args, **kwargs)
        if pos == "after":
            result = old(*args, **kwargs)
            new(*args, **kwargs)
            return result
        return new(old, *args, **kwargs)

    return _wrapped
