from setuptools import setup

setup(
    name='beets-mpdadd',
    version='0.2',
    description='beets plugin that adds query results to the current MPD playlist',
    author='Daniel Greve',
    author_email='god-complex@users.noreply.github.com',
    license='MIT',
    platforms='ALL',
    packages=['beetsplug'],
    install_requires=['beets', 'python-mpd2'],
)
