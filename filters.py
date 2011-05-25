from google.appengine.ext.webapp import template

# Do not rename this variable.
register = template.create_template_register()

# Returns the URL to the given photo set.
def seturl(set):
    def getUser(set):
        return set.primary.owner

    format = "http://www.flickr.com/photos/%s/sets/%s/"
    return format % (getUser(set).username, set.id)

register.filter(seturl)
