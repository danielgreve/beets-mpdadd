#Beets MPDAdd Plugin

The ```mpdadd``` plugin adds the results of a query to the current MPD playlist.

##Usage

To enable the```mpdadd``` plugin add it to the plugins section of your configuration (see [*Using Plugins*](http://beets.readthedocs.org/en/v1.3.9/plugins/index.html#using-plugins)).

To use the ```mpdadd``` plugin:

```
beet add query
```

To clear the playlist before adding music:

```
beet add -c query
```

To query albums instead of tracks:
```
beet add -a query
```

##Configuration

To configure the plugin, make an mpd: section in your configuration file. The available options are:

* host: The MPD server hostname. Default: ```localhost```.
* port: The MPD server port. Default: ```6600```.
* password: The MPD server password. Default: ```None```.
* music_directory: If your MPD library is at a different location from the beets library (e.g., because one is mounted on a NFS share), specify the path here. Default: The beets library directory.


