#
# Utility functions for use with flickr.py.
#

# Returns the URL for a photo set, given its user id and set id.
def getPhotosetURL(userid, setid):
    # XXX: We must use the raw user ID here, because flickr.py doesn't give us
    #      access to a user's custom URL.
    format = "http://www.flickr.com/photos/%s/sets/%s/"
    return format % (userid, setid)

def getPhotosetThumb(set):
    return "http://farm%s.static.flickr.com/%s/%s_%s_%s.jpg" % \
            (set.farm, set.server, set.primary._getRawID(), set.secret, "s")
