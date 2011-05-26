#!/usr/bin/env python

# Use Django 1.2. (This must be done first.)
from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template, util

import os
import flickr

flickr.API_KEY = "b4321172a6dfef2135a2ac62aef80849"

def getUser(name):
    # Note: We only cache the user id, not the entire User object, because we
    # don't want to cache the associated photo set list. Of course, we assume
    # that the name -> id mapping is basically static.
    key = "user_" + name
    id = memcache.get(key)
    if (id is None):
        user = flickr.people_findByUsername(name)
        assert memcache.set(key, user.id)
        return user
    else:
        return flickr.User(id)

# Returns user's photo set data as dictionaries for presentation.
# XXX: Hardcoded limit is 3 for now.
def getPhotosetData(user, limit=3):
    # Collect photosets.
    sets = user.getPhotosets()[:limit]
    result = []

    for s in sets:
        import flickrutil
        result.append({
            "url": flickrutil.getPhotosetURL(user.id, s.id),
            "title": s.title,
            "img": flickrutil.getPhotosetThumb(s),
        })

    return result

class MainHandler(webapp.RequestHandler):
    def get(self):
        # Retrieve flickr user.
        # Note: The name must be the *screenname* of the flickr user.
        name = self.request.get("name")
        assert name
        user = getUser(name)
        assert user

        # Render output via template.
        path = os.path.join(os.path.dirname(__file__), "template.html")
        values = {
            "sets": getPhotosetData(user),
            "font": self.request.get("font"),
            "fontsize": self.request.get("fontsize")
        }

        self.response.out.write(template.render(path, values))

    # For debugging only!
    def log(self, out):
        import cgi
        self.response.out.write(cgi.escape(str(out)))
        self.response.out.write("\n")

def main():
    # Register template types.
    # XXX: Is there a better place for this?
    webapp.template.register_template_library('tags.filters')

    application = webapp.WSGIApplication([("/", MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == "__main__":
    main()
