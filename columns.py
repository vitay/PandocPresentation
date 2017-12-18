import pandocfilters as pf

def html(s):
    return pf.RawBlock('html', s)

def mk_columns(k, v, f, m):
    if k == "Para":
        value = pf.stringify(v).strip()
        if value.startswith('[') and value.endswith(']'):
            content = value[1:-1]

            # Two columns
            # [leftcol]
            # ...
            # [rightcol]
            # ...
            # [endcol]
            if content.startswith("leftcol"):
                width = content.replace("leftcol", '').strip()
                if width != "":
                    width+="%"
                else:
                    width="50%"
                return html("""    <div id="col-wrapper">
      <div id="col">
        <div style="width:%(width)s; float: left;">""" % {'width': width})
            elif content.startswith("rightcol"):
                width = content.replace("rightcol", '').strip()
                if width != "":
                    width+="%"
                else:
                    width="50%"
                return html("""        </div>
        <div style="width:%(width)s; float:right;">""" % {'width': width})
            elif content.startswith("endcol"):
                return html("""        </div>
      </div>
    </div>""")

            # Center
            # [centeron]
            # ...
            # [centeroff]
            elif content.startswith("centeron"):
                return html("""
      <div style="float: center; text-align: center">""")
            elif content.startswith("centeroff"):
                return html("""
      </div">""")

            # Citation
            # [citation Source: Barack Obama]
            elif content.startswith("citation"):
                text = content[8:]
                return html("""
    <p class=citation>
        %(text)s
    </p>
    """ % {'text': text} )

if __name__ == "__main__":
    pf.toJSONFilter(mk_columns)