from setuptools import setup, find_packages

setup(
    name='recursion_and_sorting',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python package with different sorting and recursion functions',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<ExploreDon>/<recursion_and_sorting>',
    author='<Thapelo Nkosi>',
    author_email='<alutabnkosi@gmail.com>'
)
