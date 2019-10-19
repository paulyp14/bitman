import IPython.display as dp


def render_html(text):
    return dp.HTML("<style>.nowrap{white-space:pre;font-family:monospace}</style><span class='nowrap' >" + text +
                   "</span>")
