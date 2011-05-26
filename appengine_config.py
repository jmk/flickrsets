# Use Django 1.2. (This must be done first.)
from google.appengine.dist import use_library
use_library('django', '1.2')

appstats_MAX_STACK = 15
appstats_MAX_LOCALS = 15
appstats_MAX_REPR = 100
appstats_MAX_DEPTH = 15

def webapp_add_wsgi_middleware(app):
   from google.appengine.ext.appstats import recording
   app = recording.appstats_wsgi_middleware(app)
   return app
