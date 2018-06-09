#!/usr/bin/python3

from setuptools import setup

setup(name='raceupdate',
        version='0.3',
        description='Scrape torrents from SMcGill1969 on Demonoid for rtorrent',
        author='CPrompt',
        author_email='cprompt@triad.rr.com',
        license='GPL',
        packages=['raceupdate'],
        zip_safe=False,
        scripts=['raceupdate.py']
        )

