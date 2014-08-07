from collective.grok import gs
from idwf.affiliate import MessageFactory as _

@gs.importstep(
    name=u'idwf.affiliate', 
    title=_('idwf.affiliate import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('idwf.affiliate.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
