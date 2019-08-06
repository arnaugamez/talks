# Brief introduction to reverse engineering using radare2

Here you are all the resources used in the talk _Brief introduction to reverse engineering usign radare2_ during the first edition of the NcNLabs, 6 April 2018 @ Barcelona

From here you can access both the slides and the crackmes used for the demos.

Find video (ES audio) here: https://vimeo.com/267633324

### Kali VM troubleshooting
If you try to execute the bin-linux crackmes using the 64-bit Kali VM that was given to you before and during the NcNLab, you will need to install some packages to support 32-bit executables. You can achieve this by running the following commands:

```
dpkg --add-architecture i386
apt-get update
apt-get install libc6:i386 libstdc++6:i386
```

### Crackme solutions
In case you are interested, you can find some solutions to the IOLI-crackmes using radare2 by Julien Voisin in here:
https://dustri.org/b/defeating-ioli-with-radare2.html
https://dustri.org/b/defeating-ioli-with-radare2-in-2017.html (Revisited solutions)

Needless to say, try to solve them by yourself before reading anyone's solution!

Moreover, try to not only get the right password, but also manage to get any password accepted.

### Handy resources
- Inline help appending a question mark ‘?’ to any command (yes, again)
- radare2 book (updated by Maijin from r1book): https://www.gitbook.com/book/radare/radare2book/details
- radare2 explorations: https://www.gitbook.com/book/monosource/radare2-explorations/details
- r2con17 talks: https://www.youtube.com/playlist?list=PLjIhlLNy_Y9Oe-nfcPEpaki0_En5dhQ5S


### Credit
- Sergi Àlvarez (aka @pancake): Many of the content covered in the slides was based on previous presentations done by him. For example the slides from past OverdriveConference or from 33c3 were really helpful. The first one as an introduction and the second one more as a demystification of the tool. You can find those slides (an many more content) in here: http://rada.re/r/talks.html

- Chris James: The _Basics_ section was partially based on the great introduction to RE with r2 made by him. Super recommended that you check it out it, specially because of computer internals' explanation, that we had only time to cover the very surface, and great stack frames' animations: https://www.youtube.com/watch?v=LAkYW5ixvhg

- Pau Oliva (aka @pof): He is the author of the IOLI-crackmes used. Still a great learning resource after so many years.

### Support and help
- IRC: #radare at irc.freenode.net
- Telegram: https://t.me/radare
