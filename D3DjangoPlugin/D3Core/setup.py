from setuptools import setup, find_packages

setup(
    name="d3-primeri",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=1.10'],

    package_data={'d3_primeri': ['static/*.css','static/*.js','static/*.html','templates/*.html']},
    zip_safe=False
)