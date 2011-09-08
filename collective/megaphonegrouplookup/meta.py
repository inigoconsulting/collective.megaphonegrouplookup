from zope.interface import Interface
from zope import schema
from zope.component.zcml import adapter, utility
from collective.megaphonegrouplookup.lookup import (
    GroupLookupRecipientSource,
    GroupLookupRecipientSourceRegistration,
    IGroupSetting
)

from collective.megaphonegrouplookup.interfaces import IGroupSource

from collective.megaphone.interfaces import IMegaphone
from zope.publisher.interfaces.browser import IBrowserRequest
from collective.megaphone.interfaces import IRecipientSource

from zope.configuration.fields import Path
from zope.schema.vocabulary import SimpleVocabulary

import simplejson

class IGroupDataSourceDirective(Interface):

    name = schema.TextLine(
        title=u'Name', 
        description=u'Identifier of the group',
    )

    json_source = Path(
        title=u'Name of the json file where the source is stored',
        description=u'''
            Refers to a file containing json in this format:

                {
                    'Group Title': [
                        {
                            'honorific': 'Mr',
                            'first': 'firstname',
                            'last': 'lastname',
                            'email': 'user@server.com',
                            'description': 'description'        
                        }, ...
                    ],
                    'Group Title': [
                        {
                            'honorific': 'Mr',
                            'first': 'firstname',
                            'last': 'lastname',
                            'email': 'user@server.com',
                            'description': 'description'        
                        }, ...
                    ]
                }
        '''
    )

    site = schema.TextLine(
        title=u'Site',
        description=u'Site ID',
        required=False,
    )

    title = schema.TextLine(
        title=u'Title',
        description=u'Title of the group',
        required=False,
    )

    description = schema.TextLine(
        title=u'Description',
        description=u'Description of the group',
        required=False
    )

    select_label = schema.TextLine(
        title=u'Label',
        description=u'Label of the selection field',
        required=False
    )

    select_description = schema.TextLine(
        title=u'Selection field description',
        required=False
    )


def groupdatasource_handler(_context, name, json_source, site=None, 
                            title=u'Officials by Group',
                            description=u'Looks up officials from a group list',
                            select_label=u'Group',
                            select_description=u'Please select a group'):

    json_data = simplejson.loads(open(json_source).read())

    vocab = SimpleVocabulary.fromItems([
                (i,i) for i in sorted(json_data.keys())
            ])
    class ISetting(Interface):
        label = schema.Choice(
            title=select_label,
            description=select_description,
            vocabulary=vocab
        )

    utility(_context, name=name, factory=lambda : json_data,
            provides=IGroupSource)  
    utility_factory = type(str(name), (GroupLookupRecipientSourceRegistration,), {
        'name': name,
        'title': title,
        'description': description,
        'site': site,
        'settings_schema': ISetting
    })

    utility(_context, name=name, factory=utility_factory)

    adapter_factory = type(str(name), (GroupLookupRecipientSource,), {
        'name': name,
    })


    adapter(_context, factory=(adapter_factory,), 
            for_=(IMegaphone, IBrowserRequest),
            provides=IRecipientSource,
            name=name)
