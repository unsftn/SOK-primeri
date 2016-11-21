from setuptools import setup, find_packages
setup(
    name="studentska-sluzba-core",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs','rs.uns','rs.uns.ftn'],
    provides=['rs.uns.ftn.studentska.sluzba.services',
              ],
    entry_points = {
        'console_scripts':
            ['sluzba_main=rs.uns.ftn.studentska.sluzba.console_main:main'],
    },
    zip_safe=True
)