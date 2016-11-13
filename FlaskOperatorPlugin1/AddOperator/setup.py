from setuptools import setup, find_packages
setup(
    name="operation_addition",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['plugin', 'plugin.operator'],

    entry_points={
        'core.operator': [
            'add = plugin.operator.addition.add_operator:AddOperator'
        ],
    },
    zip_safe=True
)