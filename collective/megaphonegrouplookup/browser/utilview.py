from Products.Five import BrowserView

class MegaphoneLookupUtil(BrowserView):
    def enable_orderedlist_js(self):
        # hack to check whether currently its megaphone view
        url = self.request.get('URL')
        if url.endswith('addMegaphoneAction'):
            return True
        if url.endswith('editMegaphoneAction'):
            return True
        return False
