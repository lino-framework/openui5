from atelier.invlib import setup_from_tasks
# print(20200725, globals().keys())
ns = setup_from_tasks(
    globals(), "lino_openui5",
    languages="en de fr et".split(),
    # tolerate_sphinx_warnings=True,
    blogref_url='http://luc.lino-framework.org',
    revision_control_system='git',
    # locale_dir='lino_extjs/extjs/locale',
    cleanable_files=['docs/api/lino_openui5.*'],
    demo_projects=[
        'lino_openui5.projects.teamUi5',
        'lino_openui5.projects.lydiaUi5'])
