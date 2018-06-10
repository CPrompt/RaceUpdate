#!/usr/bin/python3

from setuptools import setup

setup(name='raceupdate',
        version='0.3',
        description='Scrape torrents from SMcGill1969 on Demonoid for rtorrent',
        author='CPrompt',
        author_email='cprompt@triad.rr.com',
        license='GPL',
        packages=['raceupdate','raceupdate.loginfo','raceupdate.static'],
        package_data={'raceupdate.static':['*']},
        zip_safe=False,
        entry_points={
            'console_scripts':[
                'raceupdate = raceupdate.raceupdate:main',
                ]
            }
        )

