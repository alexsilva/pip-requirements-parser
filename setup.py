from setuptools import setup

setup(
    name='pip-requirements-parser',
    version='2.0.0',
    url='https://github.com/alexsilva/pip-requirements-parser',
    license='MIT',
    author='alex',
    author_email='alex@fabricadigital.com.br',
    description='Gets the list of requirements in requirements.txt',
    include_package_data=True,
    py_modules=["requirements_parser"]
)
