from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy
import os

def pyload(name):
    ns = {}
    with open(name, encoding="utf-8") as f:
        exec(compile(f.read(), name, "exec"), ns)
    return ns

def create_symlink():
    import sklearn  # Import scikit-learn here
    sklearn_path = os.path.dirname(sklearn.__file__)
    link_path = os.path.join(repo_root, 'sklearn')
    if not os.path.exists(link_path):
        os.symlink(sklearn_path, link_path)
    return link_path

def remove_symlink(link_path):
    if os.path.exists(link_path):
        os.remove(link_path)

repo_root = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(repo_root, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

ns = pyload(os.path.join(repo_root, "pdc_dp_means", "release.py"))
version = ns["__version__"]

# Call create_symlink() and store the link_path
link_path = create_symlink()

ext_modules = [
    Extension(
        "pdc_dp_means.dp_means_cython",
        sources=["pdc_dp_means/dp_means_cython.c"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name="pdc-dp-means",
    version=version,
    author="Or Dinari",
    author_email="dinari.or@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD3",
    packages=find_packages(),
    package_data={
        "pdc-dp-means": ["docs/*"],
    },
    keywords="dp-means clustering",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=[
        "scikit-learn>=1.2,<1.3",
        "numpy>=1.23.0,<2.0",
    ],
    tests_require=[
        "pytest",
        "scikit-learn",
        "numpy",
        # add any other test dependencies here
    ],
    ext_modules=cythonize(ext_modules),
    # cmdclass={"build_ext": build_ext},
    project_urls={
        "Source": "https://github.com/BGU-CS-VIL/pdc-dp-means",
        "Tracker": "https://github.com/BGU-CS-VIL/pdc-dp-means",
        "Documentation": "https://pdc-dp-means.readthedocs.io/en/latest/",
    },
)

# Remove the symlink after setup is done
remove_symlink(link_path)
