from setuptools import setup, find_packages

setup(
    name="sparseml-exps",
    version="0.1.0",
    description="Sparseml experiments",
    author="ajkdrag",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[
        "PyYAML==6.0",
        "torch==1.9.0",
        "torchvision==0.10.0",
        "sparseml[torch]"
    ],
    setup_requires=["flake8"],
)
