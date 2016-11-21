from setuptools import setup, find_packages
setup(
    name="prikaz-fakultet-obican",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs','rs.uns','rs.uns.ftn','rs.uns.ftn.fakultet'],
    entry_points = {
        'fakultet.prikaz':
            ['prikaz_obican=rs.uns.ftn.fakultet.prikaz_obican:FakultetPrikazObican'],
    },
    zip_safe=True
)