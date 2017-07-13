# atl-toc.py

Generate a table-of-contents in markdown from your note, suitable for use with gitlab & github.
Matt LeBlanc <matt.leblanc@cern.ch>

### Get the file

Clone the repository (anywhere ... maybe *not* inside of your note?) --
```
git clone ssh://git@gitlab.cern.ch:7999/mleblanc/atl-toc.git
```

### Generate your README.md

Just point the script at your note:

```
python atl-toc.py --input /PATH/TO/YOUR/NOTE/
```

This will generate a file named something like `README-ATL-CONF-999.md` in the directory where you're calling the script from. Copy this into your note's repository and name it `README.md` to have it update your gitlab page.

Support for including the figures (as .png's) is planned, but not supported yet.

:beers:

