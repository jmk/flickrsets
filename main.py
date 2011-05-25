#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template, util

import os
import flickr

flickr.API_KEY = "b4321172a6dfef2135a2ac62aef80849"

class MainHandler(webapp.RequestHandler):
    def get(self):
        # Retrieve flickr user.
        # Note: The name must be the *screenname* of the flickr user.
        name = self.request.get("name")
        assert name
        user = flickr.people_findByUsername(name)
        assert user

        # Collect photosets.
        # XXX: Hardcoded limit is 3.
        sets = user.getPhotosets()[:3]

        # Render output via template.
        path = os.path.join(os.path.dirname(__file__), "template.html")
        values = {
            "sets": sets,
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
    webapp.template.register_template_library('filters')

    application = webapp.WSGIApplication([("/", MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == "__main__":
    main()
