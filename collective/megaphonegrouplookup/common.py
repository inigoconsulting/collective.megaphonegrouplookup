from collective.megaphone.interfaces import (IRecipientSourceRegistration)
from zope.interface import implements

class LookupRecipientSourceRegistration(object):
    implements(IRecipientSourceRegistration)

    name = 'group_recipient_lookup'
    title = u'Officials by Group'
    description = u'Looks up officials based on group'
    settings_schema = None
    site = None

    @property
    def enabled(self):
        if self.settings_schema is None:
            return False
        if self.site is None:
            return True
        else:
            site = getSite()
            if site.id == self.site:
                return True
        return False

    def get_label(self, settings):
        return settings['settingsdata']

