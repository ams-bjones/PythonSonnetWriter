PythonSonnetWriter
==================

Automatic sonnet writer by Python.

The origional idea from @TheBritKnight [SonnetWriter](https://github.com/TheBritKnight/SonnetWriter), which is a simple [Markov_chain](http://en.wikipedia.org/wiki/Markov_chain) implementation. Based on this, I am trying to generate a real sonnet.

A [sonnet](http://en.wikipedia.org/wiki/Sonnet) is a poem, but not only a poem. There are different variations of sonnets. We will start from [English (Shakespearean) sonnet](http://en.wikipedia.org/wiki/Sonnet#English_.28Shakespearean.29_sonnet). Hopefully, we can walk into other variation as well.

Requirements
============

NLTK
----

Thanks for [Kash's Post](http://kashthealien.wordpress.com/2013/06/15/213/) to get a list of rhyming words.

To install NLTK:

```
pip install pyyaml nltk
```

To download NLTK data:

```
>>>import nltk
>>>nltk.download()
```

The data is huge. However, you only need corpus -> cmudict for this app.

Usage
=====


```
python WriteSonnet.py
```

In Program:

```
from SonnetWriter import SonnetWriter

writer = SonnetWriter()
writer.Initialize("Sonnets.txt")
writer.AnalyzeText()
writer.WriteSonnet()
writer.Print()

```

Sample
======

```
Eyes corrupt by this wide world doth deceive
Still to his living record of birds sang
Mortal moon and lusty days should achieve
Me blind soul which by my flame should do hang
No precious time at grievances foregone
Of miles when first i fortune once asleep
See others write for thee doth it live drawn
Myself i'll forfeit so dumb thoughts sold cheap
Come hindmost holds her wish would i whilst thou spend
The hours have frequent been with my chest
I journey in hideous winter and
Leave to kiss the waves make thy side against
Wilt for blunting the clock that ink my stain
Art all their verdict is from home again
```

Tasks
=====

- [ ] Write verses in iambic pentameter.
- [ ] Use second level dictionary.
- [ ] Enhance process to choose words from dictionary.
- [ ] Support more Sonnet styles.
- [ ] Performence improvement.

License
=======

[CC-BY-NC](http://creativecommons.org/licenses/by-nc/4.0/deed.en_US)