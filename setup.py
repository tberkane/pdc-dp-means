from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import os

def pyload(name):
    ns = {}
    with open(name, encoding="utf-8") as f:
        exec(compile(f.read(), name, "exec"), ns)
    return ns

repo_root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(repo_root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

ns = pyload(os.path.join(repo_root, "pdc_dp_means", "release.py"))
version = ns["__version__"]

def get_extensions():
    extensions = [
        Extension(
            "pdc_dp_means.dp_means_cython",
            ["pdc_dp_means/dp_means_cython.pyx"],
            include_dirs=[numpy.get_include()],
        )
    ]
    return extensions

setup(
    name="pdc-dp-means",
    version=version,
    author="Or Dinari",
    author_email="dinari.or@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD3",
    keywords="dp-means clustering",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    tests_require=[
        "pytest",
        "scikit-learn",
        "numpy",
    ],
    include_package_data=True,
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/BGU-CS-VIL/pdc-dp-means",
        "Tracker": "https://github.com/BGU-CS-VIL/pdc-dp-means",
        "Documentation": "https://pdc-dp-means.readthedocs.io/en/latest/",
    },
    packages=find_packages(),
    package_data={
        "pdc-dp-means": ["docs/*"],
    },
    install_requires=[
        "scikit-learn>=1.2,<1.3",
        "numpy>=1.23.0,<2.0",
        "Cython>=0.29.0",
    ],
    setup_requires=[
        "Cython>=0.29.0",
        "numpy>=1.23.0,<2.0",
    ],
    ext_modules=cythonize(get_extensions()),
)
