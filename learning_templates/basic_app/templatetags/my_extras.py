from django import template

register=template.Library()
@register.filter(name='cut')
def cut(value,args):
    """
    This cuts out all the values 'args' from the strings
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
