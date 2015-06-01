from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets import ui
from beets import config
from os.path import relpath
from mpd import MPDClient

def mpd_add(lib, opts, args):
    """Converts results from a query to relative uris and sends them to MPD.
    """

    # Read user configuration.
    host = config['mpd']['host'].get()
    port = config['mpd']['port'].get()
    password = config['mpd']['password'].get()
    music_directory = config['mpd']['music_directory'].get()

    # Print how many items are being added
    def aye(item_list, item_type):
        num = len(item_list)
        if num > 1:
            item_type += 's'
        elif num == 0:
            ui.print_(ui.colorize('red', 'No items match your query.'))
            return
        elif num > 100:
            ui.print_(ui.colorize('red', 'Add %s %s to playlist?' % (num, item_type)))
            if ui.input_options(('Yes', 'No')) == 'n':
                sys.exit(0)
        ui.print_(ui.colorize('brown', 'Adding %s %s to playlist...' % (num, item_type)))

    # Perform query and retrieve the absolute path to the results.
    if opts.album:
        paths = [albums.path for albums in lib.albums(ui.decargs(args))]
        aye(paths, 'album')
    else:
        paths = [items.path for items in lib.items(ui.decargs(args))]
        aye(paths, 'track')

    # Generate relative paths of the results from user specified directory.
    playlist = [relpath(item, music_directory) for item in paths]

    # Initialize client object.
    client = MPDClient()
    
    # Authenticate with password if one is provided.
    if password:
        client.password(password)

    # Connect to MPD.
    client.connect(host,port)

    # Optionally clear current playlist before adding music.
    if opts.clear:
        client.clear()

    # Iterate through URIs and send them to MPD.
    for uri in playlist:
        client.add(uri)

    # Send the play command to MPD and close the connection.
    client.play()
    client.close()
    client.disconnect()


class MPDAddPlugin(BeetsPlugin):

    def __init__(self):
        super(MPDAddPlugin, self).__init__()

        config['mpd'].add({
            'host': u'localhost',
            'port': 6600,
            'password': u'',
            'music_directory': config['directory'].as_filename(),
        })

    def commands(self):
        mpd_add_command = Subcommand(
            'add',
            help='add music to your playlist'
        )
        mpd_add_command.parser.add_option(
            '-a', '--album',
            action='store_true', default=False,
            help='add albums instead of tracks'
        )
        mpd_add_command.parser.add_option(
            '-c', '--clear',
            action='store_true', default=False,
            help='clears current playlist before adding music'
        )
        mpd_add_command.func = mpd_add
        return [mpd_add_command]
