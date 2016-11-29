from setuptools import setup, find_packages

setup(
    name="prodavnica-flask",
    version="0.1",
    packages=find_packages(),
    install_requires=['injector>=0.11',
                      'Flask-Injector>=0.8',
                      'Flask>=0.11'],
    entry_points = {
        'console_scripts':
            ['prodavnica_main=prodavnica.run_server:main'],
    },
    package_data={'prodavnica': ['static/*.css','templates/*.html']},
    zip_safe=False
)