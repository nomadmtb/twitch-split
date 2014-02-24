twitch-split
============

![](https://raw.github.com/nomadmtb/twitch-split/master/README_FILES/sample_double.gif)

What is Twitch-Split?
---------------------

Twitch-Split is a basic web application that allows users to watch two different Twitch streams at once. Right now Twitch has support for either one streamer or two. I hope to expand the functionality in the future to accomodate different orientations.

How do you use it?
------------------

To use Twitch-Split users just need to add their desired streams to the URL.

* GET: http://domain.com/goldglove
> Will generate a view for a single stream.

* GET: http://domain.com/goldglove/actabunnifoofoo
> Will generate a page for users goldglove and actabunnifoofoo.

* GET: http://domain.com/goldglove/actabunnifoofoo?orientation=vertical
> Future development will allow for a specific layout with GET parameter.

* GET: http://domain.com/goldglove/blablaerror
> Streams that dont exist via the Twitch API will generate an error notification.
