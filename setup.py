import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cancerify",
    version="1.0.0",
    author="Aniket Bhattacharyea",
    author_email="i_abh_esc_wq@protonmail.com",
    description="Turn an innocent text into torturous hell",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/i-abh-esc-wq/Cancerify",
    packages=setuptools.find_packages(),
    install_requires=['emoji', 'bidict'],
    scripts=['bin/cancerify'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
