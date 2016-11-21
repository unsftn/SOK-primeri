from setuptools import setup, find_packages
setup(
    name="prikaz-fakultet-slozen",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs','rs.uns','rs.uns.ftn','rs.uns.ftn.fakultet'],
    entry_points = {
        'fakultet.prikaz':
            ['prikaz_slozen=rs.uns.ftn.fakultet.prikaz_slozen:FakultetPrikazSlozen'],    },
    zip_safe=True
)