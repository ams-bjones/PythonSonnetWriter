PythonSonnetWriter
==================

Automatic sonnet writer by Python.

The origional idea from @TheBritKnight [SonnetWriter](https://github.com/TheBritKnight/SonnetWriter), which is a simple [Markov_chain](http://en.wikipedia.org/wiki/Markov_chain) implementation. Based on this, I am trying to generate a real sonnet.

A [sonnet](http://en.wikipedia.org/wiki/Sonnet) is a poem, but not only a poem. There are different variations of sonnets. We will start from [English (Shakespearean) sonnet](http://en.wikipedia.org/wiki/Sonnet#English_.28Shakespearean.29_sonnet). Hopefully, we can walk into other variation as well.

Requirements
============

NLTK - Not needed for current version. For furture versions (not sure which one though) only.
----

Thanks for [Kash's Post](http://kashthealien.wordpress.com/2013/06/15/213/) to get a list of rhyming words.

To install NLTK:

pip install pyyaml nltk

To download NLTK data:

>>> import nltk
>>> nltk.download()

The data is huge. However, you only need corpus -> cmudict for this app.

Usage
=====

python SonnetWriter.py

Sample
======

flatter the times more by succession thine outward form of
perforce am mortgaged to my brain and let those dancing
describe adonis and child and me a dream doth nature
than both from heat still lives a noted yet then
doing thee hold me thus mine eyes belongs to time
revenge upon deceased i assure ye
'tis with his compeers by advis'd respects
music music music to eat up to whom frown'st thou
drink up the truth proves thievish for no ill report
hath mask'd him here live unwoo'd and such matter that
weeds among weeds among the even in so will drink
die i condemned for still will bitter think that still
darkening thy spirit is abused
points on high as truth proves thievish progress to times

License
=======

[CC-BY-NC](http://creativecommons.org/licenses/by-nc/4.0/deed.en_US)