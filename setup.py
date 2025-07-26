from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ascii-animator",
    version="1.0.0",
    author="ASCII Animator Team",
    description="🎬 Create stunning ASCII animations with AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ascii-animator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "rich>=13.0.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "animate=ascii_animator.__main__:main",
        ],
    },
    keywords="ascii art animation cli ollama ai",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ascii-animator/issues",
        "Source": "https://github.com/yourusername/ascii-animator",
    },
)