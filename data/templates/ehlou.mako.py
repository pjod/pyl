# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1371722102.067897
_enable_loop = True
_template_filename = '/home/pjo/projekt1/projekt1/templates/ehlou.mako'
_template_uri = '/ehlou.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        request = context.get('request', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<p>Zmienne serwera:</br>\n')
        # SOURCE LINE 2
        str(request.environ) 
        
        __M_writer(u'</p>\n\n<p>\nURL: ')
        # SOURCE LINE 5
        h.url() 
        
        __M_writer(u'\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


