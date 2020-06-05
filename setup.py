import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OverwatchUserDirectory", # Replace with your own username
    version="1.0",
    author="Yotam",
    author_email="yotam201410@gmail.com",
    description="An Overwatch user directory that gets everything you can take from overwatch API using ovrstat(https://ovrstat.com) ",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)