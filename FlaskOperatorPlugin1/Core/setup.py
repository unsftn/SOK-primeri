from setuptools import setup, find_packages

setup(
    name="operation-core",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin','plugin.operator'],
    install_requires=['injector>=0.11',
                      'Flask-Injector>=0.8',
                      'Flask>=0.11'],
    provides=['plugin.operator.core.services',
              ],
    entry_points = {
        'console_scripts':
            ['operator_main=plugin.operator.core.flask_main:main'],
    },
    package_data={'plugin.operator.core': ['static/*.css','templates/*.html']},
    zip_safe=False
)