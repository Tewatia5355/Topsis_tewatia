
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_Tewatia",
    version="1.0.0",
    author="Yash Kumar Tewatia",
    author_email="yashbsr3@gmail.com",
    description="A package -> Calculates Topsis Score and Rank them accordingly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tewatia5355/Topsis_tewatia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
