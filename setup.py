from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.megaphonegrouplookup',
      version=version,
      description="Group lookup mechanism for Megaphone.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='megaphone group lookup',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='http://svn.plone.org/svn/collective/collective.megaphonegrouplookup',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
