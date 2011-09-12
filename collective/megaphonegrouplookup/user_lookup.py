import logging
from zope import schema
from zope.interface import Interface
from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.interface import implements
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from collective.megaphone.interfaces import (IRecipientSource,
                                             IRecipientSourceRegistration)
from collective.megaphone.recipients import (get_recipient_settings,
                                             recipient_label)
from Products.CMFCore.utils import getToolByName

from zope.component import getUtility

from collective.megaphonegrouplookup.interfaces import IGroupSource

class LookupRecipientSource(object):
    implements(IRecipientSource)

    name = 'group_recipient_lookup'
    form_label = 'Send to'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.settings = get_recipient_settings(context, self.name)

    def available_groups(self):
        groups = []
        for id, data in self.settings:
            for g in data['settingsdata']:
                groups.append({
                    'value': g,
                    'label': g
                })
        return groups

    def lookup(self):
        group = self.request.get('megaphone-group-select')
        json_data = getUtility(IGroupSource, self.name)
        return json_data[group]
        

    snippet = ViewPageTemplateFile('user_select_snippet.pt')

    def render_form(self):
        return self.snippet()
