import setuptools

with open("READNE.MD",'r') as f:
    long_description = f.read()

setuptools.setup(
    name="OverwatchUserDirectory",
    version="1.0",
    author="Yotam",
    author_email="yotam201410@gmail.com",
    description="An Overwatch user directory that gets everything you can take from Overwatch API using ovrstat(https://ovrstat.com) ",
    url="https://github.com/yotam201410/OverwatchUserDirectory",
    packages=setuptools.find_packages(),
    lisence="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    python_requires='>=3.5',
    install_requires=[
        'requests>=2.25.1'
    ]
)
