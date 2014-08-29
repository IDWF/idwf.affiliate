from five import grok
from plone.directives import dexterity, form
from idwf.affiliate.content.affiliate import IAffiliate

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IAffiliate)
    grok.require('zope2.View')
    grok.template('affiliate_view')
    grok.name('view')

