#!/usr/bin/env python
from os.path import exists

from setuptools import Distribution, find_packages, setup

try:
    from wheel.bdist_wheel import bdist_wheel
except ImportError:
    bdist_wheel = object

with open("README.rst") as f:
    long_description = f.read()

data_files = []
bin_files = []


class ExtensionDistribution(Distribution):
    def has_ext_modules(*args, **kwargs):
        return True


class PlatformWheel(bdist_wheel):
    def get_tag(self, *args, **kwargs):
        python, abi, plat = super().get_tag(*args, **kwargs)
        return ('py3', 'none', plat)


for license_path in ('docs/License.html', 'docs/LICENSE'):
    if bdist_wheel and exists(license_path):
        data_files.append(('docs', [license_path]))
        bin_files.extend(['MediaInfo.dll', 'libmediainfo.*', 'libzen.*'])
        break

cmdclass = {'bdist_wheel': PlatformWheel} if bin_files else {}
distclass = ExtensionDistribution if bin_files else Distribution


setup(
    name='pymediainfo-lambda',
    author='Louis Sautier',
    author_email='sautier.louis@gmail.com',
    url='https://github.com/hurlenko/pymediainfo-lambda',
    project_urls={
        "Documentation": "https://pymediainfo.readthedocs.io/",
        "Bugs": "https://github.com/sbraz/pymediainfo/issues",
    },
    description="""A Python wrapper for the mediainfo library.""",
    long_description=long_description,
    packages=find_packages(),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    data_files=data_files,
    use_scm_version=True,
    python_requires=">=3.7",
    setup_requires=["setuptools_scm"],
    install_requires=["importlib_metadata; python_version < '3.8'"],
    package_data={'pymediainfo': bin_files},
    distclass=distclass,
    cmdclass=cmdclass,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]
)