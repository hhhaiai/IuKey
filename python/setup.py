import setuptools

from api import version

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="IuKey",
    version=version,
    author="sanbo",
    author_email="sanbo.xyz@gmail.com",
    description="Idea key Update. support:LanZouCloud API-2.5.8.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hhhaiai/IuKey",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "requests_toolbelt"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
