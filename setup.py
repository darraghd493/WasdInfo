setup(
    name="WasdInfo",
    version="1.0.0",
    description="WasdInfo displays weather you are pressing your WASD keys and/or left and right mouse buttons onto your screen through PyQt5 (Python wrapper for Qt5).",
    long_description="README.MD",
    long_description_content_type="text/markdown",
    url="https://github.com/dogesupremacy/WasdInfo",
    author="dogesupremacy",
    author_email="darragh@dowssetts.org",
    license="GNU General Public License (GPL)",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=[
        "pywin32", "PyQt5"
    ],
    include_package_data=True,
    install_requires=[
        "pywin32", "PyQt5"
    ],
    entry_points={"console_scripts": ["WasdInfo=src.__main__:main"]},
)
