from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from idwf.affiliate import MessageFactory as _


# Interface class; used to define content-type schema.

class IAffiliate(form.Schema, IImageScaleTraversable):
    """
    IDWF Affiliate
    """
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Name of Organization')

    dexteritytextindexer.searchable('description')
    description = schema.Text(title=u'Description',
                              description=u'Brief description '
                              'or summary of organization.')
    objectives = RichText(title=u'Objectives, Aims, Mission & '
                          'Vision of Organization',)
    history = RichText(title=u'History of Organization')

    #Contact Details
    street_address = schema.TextLine(title=u'Street Adress')
    phone_number = schema.TextLine(title=u'Phone Number',
                                   description=u'Office No. eg. '
                                   '+1 34 4444 4444')
    fax_number = schema.TextLine(title=u'Fax Number',
                                 description=u'Fax No. eg. +1 34 4444 4444')
    email = schema.TextLine(title=u'Email address')
    website_url = schema.TextLine(title=u'Website URL',
                                  description=u'eg. https://www.idwfed.org')
    #Number of Members
    members_male_no = schema.Int(title=u'Number of Male Members')
    members_female_no = schema.Int(title=u'Number of Female Members')
    phone_number = schema.TextLine(title=u'Phone Number',
                                   description=u'Office No. eg. +1 '
                                   '34 4444 4444')

    #Membership Details
    member_fees = schema.Bool(title=u'Check if members pay fees')
    maintains_register_fees = schema.Bool(
        title=u'Maintains register of fees paid')
    year_established = schema.Date(title=u'Year Established')

    organization_type = schema.Choice(
           title=_(u'Organization Type'),
           values=[_(u'Trade Union'),
                   _(u'Worker Association'),
                   _(u'Coop'),
                   _(u'Other')]
    )   

alsoProvides(IAffiliate, IFormFieldProvider)
