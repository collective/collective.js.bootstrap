from setuptools import setup, find_packages
import os

version = '2.3.2.dev0'

setup(name='collective.js.bootstrap',
      version=version,
      description="Get twitter bootstrap as browser resources",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone',
      author='JeanMichel aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
