from setuptools import setup, find_namespace_packages


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="spectral_data_converter_vis",
    description="Visualization plugins for the spectral-data-converter library.",
    long_description=(
            _read('DESCRIPTION.rst') + b'\n' +
            _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/waikato-datamining/spectral-data-converter-vis",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    install_requires=[
        "spectral_data_converter",
        "matplotlib",
    ],
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
    entry_points={
        "class_lister": [
            "sdc=sdc.vis.class_lister",
        ],
    },
)
