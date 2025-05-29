# AWS Diagramming Templates and Assets

This library is initialy based on the great project by Will Thames.

## Installation

Download or clone this repository
```
git clone https://github.com/willthames/aws-inkscape-symbols
```

## Generation of symbols

Download the latest Assets Package
from the [AWS Simple Icons](https://aws.amazon.com/architecture/icons/)
page

Run:

```
build.sh /path/to/downloaded.zip
```

This will create all of the AWS symbols in the `target` subdirectory

## Using the symbols with inkscape

Copy the symbol sets you require to your inkscape configuration
directory (e.g. ~/Library/Application\ Support/org.inkscape.Inkscape/config/inkscape/symbols)

The bigger the symbol sets you use, the slower Inkscape seems to
be to start up, so just add symbol sets as you need them (if you
want to add all of them in that knowledge, feel free!).


## References/Inspiration

Thanks to Xaviju for
[enough pointers to get me started](https://medium.com/@xaviju/creating-your-own-symbol-library-in-inkscape-0-91-and-make-your-front-end-developer-you-338588137aaf) generating a symbol set from the base SVG files that
AWS provide

Thanks to jbruce12000 for providing a
[getting started set](https://github.com/jbruce12000/inkscape-aws-simple-icons)
of symbols and inspiring me to generate the rest.


## Contributions

Please feel free to raise issues or pull requests for improvements.
There are some obvious quick wins (e.g. better symbol naming)
and some bugs (the SVG that AWS provide for WorkMail doesn't have
a `<g>` element and I haven't bothered addressing that one).


## License

This repository is currently offered under the MIT License
Different terms almost certainly apply to your usage of the AWS
Icon Sets. At the time of writing, AWS
[haven't explicitly stated those terms](https://forums.aws.amazon.com/thread.jspa?messageID=792596)

Once those terms become clear, I might start including the symbols
alongside the generation code (at which point the license might need
to change).
