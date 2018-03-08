def tag(name,cls=None,*content,**attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attrs_str = ''.join('%s="%s"' % (attr,value) for attr,value in sorted(attrs.items()))
    else:
        attrs_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name,attr_str,c,name) for c in content)
    else:
        return '<%s%s />' % (name,attr_str)
