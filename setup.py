"""
avwx Package Setup
"""

from setuptools import find_namespace_packages, setup

VERSION = "1.6.22"

dependencies = [
    "geopy~=2.2",
    "httpx~=0.22",
    "python-dateutil~=2.8",
    "xmltodict~=0.12",
]

test_dependencies = ["pytest-asyncio~=0.17", "time-machine~=2.6"]

extras = {
    "fuzz": ["rapidfuzz~=1.9"],
    "scipy": ["scipy~=1.8"],
    "docs": ["mkdocs~=1.2", "mkdocs-material~=8.1", "mkdocs-minify-plugin~=0.5"],
    "tests": test_dependencies,
}
extras["all"] = extras["fuzz"] + extras["scipy"]

setup(
    name="avwx-engine",
    version=VERSION,
    description="Aviation weather report parsing library",
    url="https://github.com/avwx-rest/avwx-engine",
    author="Michael duPont",
    author_email="michael@dupont.dev",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">= 3.7",
    install_requires=dependencies,
    packages=find_namespace_packages(include=["avwx*"]),
    package_data={"avwx.data": ["aircraft.json", "stations.json"]},
    tests_require=test_dependencies,
    extras_require=extras,
)
