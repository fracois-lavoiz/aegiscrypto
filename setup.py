"""Setup configuration for aegiscrypto."""
from setuptools import setup, find_packages

setup(
    name="aegiscrypto",
    version="1.0.0",
    author="Sovereign Shield Systems Ltd",
    author_email="dev@sovereignshield.co.uk",
    description="Post-quantum cryptographic operations, certificate validation, and secure hashing at scale",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fracois-lavoiz/aegiscrypto",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["cryptography>=42.0.0"],
    extras_require={"dev": ["pytest>=8.0.0"]},
    classifiers=["Development Status :: 5 - Production/Stable", "Topic :: Security"],
)
