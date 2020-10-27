# -*- coding: utf-8 -*-
"""Installer for the collective.js.bootstrap package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.js.bootstrap',
    version='3.3.8.dev0',
    description="Get twitter bootstrap as browser resources",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Framework :: Zope2",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone CMS',
    author='JeanMichel aka toutpt',
    author_email='toutpt@gmail.com',
    url='https://github.com/collective/collective.js.bootstrap',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/collective.js.bootstrap',
        'Source': 'https://github.com/collective/collective.js.bootstrap',
        'Tracker': 'https://github.com/collective/collective.js.bootstrap/issues',
        # 'Documentation': 'https://collective.js.bootstrap.readthedocs.io/en/latest/',
    },
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.js'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'plone.app.jquery>=1.8.3',
        'setuptools',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing>=5.0.0',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.js.bootstrap.locales.update:update_locale
    """,
)
