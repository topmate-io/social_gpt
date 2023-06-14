import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = [line.split('==')[0] for line in fh.read().splitlines()]

setuptools.setup(
    name="social_gpt",
    version="0.0.11",
    author="dinesh1301",
    author_email="dinesh@topmate.io",
    description="Social gpt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/topmate-io/social_gpt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements
)
