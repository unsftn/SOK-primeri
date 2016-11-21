from setuptools import setup, find_packages
setup(
    name="ucitavanje-fakultet-fajl",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['rs','rs.uns','rs.uns.ftn','rs.uns.ftn.fakultet'],
    entry_points = {
        'fakultet.ucitavanje':
            ['ucitavanje_fajl=rs.uns.ftn.fakultet.ucitavanje_fajl:FakultetUcitavanjeFajl'],
    },
    data_files=[('fajlovi',['fajlovi/fakulteti.txt'])],
    zip_safe=False
)