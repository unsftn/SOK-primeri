from setuptools import setup, find_packages
setup(
    name="ucitavanje-fakultet-kod",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs','rs.uns','rs.uns.ftn','rs.uns.ftn.fakultet'],
    entry_points = {
        'fakultet.ucitavanje':
            ['ucitavanje_kod=rs.uns.ftn.fakultet.ucitavanje_kod:FakultetUcitavanjeKod'],
    },
    zip_safe=True
)