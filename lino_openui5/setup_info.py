# -*- coding: UTF-8 -*-
# Copyright 2015-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

SETUP_INFO = dict(
    name='lino_openui5',
    version='20.8.2',
    install_requires=['lino'],
    tests_require=[],
    test_suite='tests',
    description="The OpenUI5 front end for Lino",
    license='BSD-2-Clause',
    include_package_data=False,
    zip_safe=False,
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="https://github.com/lino-framework/openui5",
    classifiers="""\
  Programming Language :: Python
  Programming Language :: Python :: 3
  Development Status :: 1 - Planning
  Environment :: Web Environment
  Framework :: Django
  Intended Audience :: Developers
  Intended Audience :: System Administrators
  License :: OSI Approved :: GNU Affero General Public License v3
  Natural Language :: English
  Operating System :: OS Independent
  Topic :: Database :: Front-Ends
  Topic :: Home Automation
  Topic :: Office/Business
  Topic :: Software Development :: Libraries :: Application Frameworks""".splitlines())

SETUP_INFO.update(long_description="""\

An alternative Django admin interface based on the `SAP OpenUI5
<https://openui5.org/>`__ toolkit.

This Lino front end has passed the proof of concept phase (i.e. it shows that
the idea works), but it is not ready for production. There is still much work to
do.

Rumma & Ko Ltd currently have no resources to continue on the OpenUI5 front end.
Lino is free open source software, so anybody is welcome to work on it, and we
would be glad to help with getting started.

The central project homepage is https://openui5.lino-framework.org/

""")

SETUP_INFO.update(packages=[str(n) for n in """
lino_openui5
lino_openui5.openui5
lino_openui5.projects
lino_openui5.projects.teamUi5
lino_openui5.projects.teamUi5.settings
lino_openui5.projects.teamUi5.tests
lino_openui5.projects.lydiaUi5
lino_openui5.projects.lydiaUi5.settings
lino_openui5.projects.lydiaUi5.tests
""".splitlines() if n])

SETUP_INFO.update(include_package_data=True)
