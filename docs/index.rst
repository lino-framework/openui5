.. _openui5:

==========================
OpenUI5 front end for Lino
==========================

This is the documentation tree for :mod:`lino_openui5`.


.. py2rst::

  from lino_openui5 import SETUP_INFO
  print(SETUP_INFO['long_description'])


How to try it:

- Install some Lino application as explained in :ref:`lino.dev.install`.

- In your :xfile:`settings.py` file, set set the :attr:`default_ui
  <lino.core.site.Site.default_ui>` attribute to `"lino_openui5.openui5"`::

    class Site(Site):
        ...
        default_ui = 'lino_openui.openui5'
        ...

- Run :manage:`collectstatic`::

    $ python manage.py collectstatic


Content
========

.. toctree::
   :maxdepth: 1

   API <api/index>
   specs
   changes/index
