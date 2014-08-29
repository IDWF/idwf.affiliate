from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from idwf.affiliate.content.affiliate import IAffiliate
from idwf.affiliate import MessageFactory as _

class IAffiliates(form.Schema):
    """
       Marker/Form interface for Affiliates
    """

    # -*- Your Zope schema definitions here ... -*-

    form.fieldset(
            'categorization',
            label=_(u'Categorization'),
            fields=('affiliates',),
            )

    #form.widget(affiliates=AutocompleteFieldWidget)
    affiliates = RelationChoice(
            title=_(u'Affliates'),
            source=ObjPathSourceBinder(
                object_provides=IAffiliate.__identifier__),
            required=False,
            )

alsoProvides(IAffiliates,IFormFieldProvider)
