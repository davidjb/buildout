from setuptools import setup, find_packages

setup(
    name = "zc.recipe.egg",
    version = "1.0.dev",
    author = "Jim Fulton",
    author_email = "jim@zope.com",
    description = "Recipe for installing Python package distributions as eggs",
    license = "ZPL 2.1",
    keywords = "development build",
    url='http://svn.zope.org/zc.buildout',
    download_url='http://download.zope.org/distribution',

    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    namespace_packages = ['zc', 'zc.recipe'],
    install_requires = ['zc.buildout', 'setuptools'],
    tests_require = ['zope.testing'],
    test_suite = 'zc.recipe.eggs.tests.test_suite',
    entry_points = {'zc.buildout': ['default = zc.recipe.egg:Egg']},    
    )