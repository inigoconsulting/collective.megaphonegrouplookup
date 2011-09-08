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

class GroupLookupRecipientSource(object):
    implements(IRecipientSource)

    name = 'group_recipient_lookup'

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.settings = get_recipient_settings(context, self.name)

    def lookup(self):
        json_data = getUtility(IGroupSource, self.name)

        info = []
        for id_, entry in self.settings:
            if entry['recipient_type'] == self.name:
                info += json_data[entry['label']]
        return info

    snippet = ViewPageTemplateFile('form_snippet.pt')

    def render_form(self):
        recipients = [r for r in  self.lookup()]
        if len(recipients):
            return self.snippet(recipients=recipients)
        return ''

class IGroupSetting(Interface):
    label = schema.TextLine(
        title=u'Group',
        description=u'Please select a group',
    )

class GroupLookupRecipientSourceRegistration(object):
    implements(IRecipientSourceRegistration)

    name = 'group_recipient_lookup'
    title = u'Officials by Group'
    description = u'Looks up officials based on group'
    settings_schema = IGroupSetting
    site = None

    @property
    def enabled(self):
        if self.site is None:
            return True
        else:
            site = getSite()
            if site.id == self.site:
                return True
        return False

    def get_label(self, settings):
        return settings['label']

