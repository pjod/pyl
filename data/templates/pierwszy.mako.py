# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1371725669.566638
_enable_loop = True
_template_filename = '/home/pjo/projekt1/projekt1/templates/pierwszy.mako'
_template_uri = 'pierwszy.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<h1>nag\u0142\xf3weczke</h1>\n<ul>\n    <li>')
        # SOURCE LINE 3
        __M_writer(escape(c.name))
        __M_writer(u'</li>\n</ul>')
        return ''
    finally:
        context.caller_stack._pop_frame()


