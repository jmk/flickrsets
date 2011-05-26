### About Flickrsets ###

Flickrsets is a simple Google App Engine application that displays a user's most recent flickr photosets.

For example:

    http://flickrsets.appspot.com/?name=%3Cjmk%3E

(Note that the app is hardcoded to display the three most recent photo sets.)

Clients may optionally specify a custom font and/or font size:

    http://flickrsets.appspot.com/?name=%3Cjmk%3E&font=monospace&fontsize=18px

__Note: This is just a simple hack.__ Errors are not handled gracefully, performance and scalability never entered the picture, not a flying toy, and so on.
