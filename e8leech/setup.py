from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="e8leech",
    version="0.1.0",
    author="E8Leech Framework Team",
    author_email="team@e8leech.dev",
    description="Mathematically rigorous E8 and Leech lattice implementation with quantum-safe cryptography and AI applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/e8leech/e8leech",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Security :: Cryptography",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "hypothesis", "black", "flake8", "mypy"],
        "docs": ["sphinx", "jupyter-book"],
        "quantum": ["qiskit", "cirq"],
    },
    entry_points={
        "console_scripts": [
            "e8leech=e8leech.cli:main",
        ],
    },
)
