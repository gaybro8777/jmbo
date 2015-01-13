from setuptools import setup, find_packages

setup(
    name='jmbo',
    version='1.1.5',
    description='The Jmbo base product introduces a content type and various tools required to build Jmbo products.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://www.jmbo.org',
    packages = find_packages(),
    dependency_links = [
        'http://github.com/praekelt/django-photologue/tarball/2.10.praekelt#egg=django-photologue-2.10.praekelt',
    ],
    install_requires = [
        'Pillow',
        'pytz',
        'django>=1.4,<1.7',
        'django-atlas',
        'django-category>=0.0.5',
        'django-likes>=0.0.8',
        'django-photologue>=2.10.praekelt',
        'django-preferences',
        'django-publisher',
        'django-sites-groups',
        'south',
        'django-tastypie>=0.10,<0.12',  # 0.12 requires Django 1.7
        'django-celery',
        'django-generate',
    ],
    include_package_data=True,
    tests_require=[
        'pysqlite>=2.5',
        'django-setuptest>=0.1.2',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
