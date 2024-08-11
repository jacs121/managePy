from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'for manage your scripts'
LONG_DESCRIPTION = 'this tool has a lot of decorator and functions for managing or restricting other functions for unique purpose '

# Setting up
setup(
    name="managePy",
    version=VERSION,
    author="jacs121 (Florian Dedov)",
    author_email="<nitzansoriano1@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
