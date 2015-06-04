# MPDAdd Plugin For beets

The ```mpdadd``` plugin adds the results of a query to the current MPD playlist.

## Installation

```
pip install git+git://github.com/danielgreve/beets-mpdadd.git
```

## Usage

First, enable the ```mpdadd``` plugin by adding it to the [plugins](http://beets.readthedocs.org/en/v1.3.10/plugins/index.html) section of your beets configuration file.

Using ```mpdadd``` is similar to performing a [query](http://beets.readthedocs.org/en/v1.3.10/reference/query.html):

```
beet add moonage daydream

beet add album:ziggy stardust

beet add year:2015
```

Use the -c or --clear option to clear the playlist before adding music.

```
beet add -c space oddity
```

Use the -a or --albums option to add only matching albums.

```
beet add -a heroes
```

## Configuration

Specify non-default options for ```mpdadd``` with a ```mpd:``` section in your beets configuration file. The available options are:

* host: The MPD server hostname. Default: ```localhost```.
* port: The MPD server port. Default: ```6600```.
* password: The MPD server password. Default: ```None```.
* music_directory: If your MPD library is at a different location from the beets library, specify the path here. Default: The beets library directory.

An example configuation:

```yaml
directory: ~/Music/beets
library: ~/.config/beets/musiclibrary.blb
plugins: mpdadd
mpd:
    host: 192.168.1
    port: 8000
    password: MajorTom
```

## More Information

* [The MPD User's Manual](http://www.musicpd.org/doc/user/)
* [Documentation for beets](http://beets.readthedocs.org/en/v1.3.10/)
