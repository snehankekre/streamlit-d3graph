import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-d3graph",
    version="1.0.2",
    author="Snehan Kekre",
    author_email="contact@snehankekre.com",
    description="A simple component to display d3graph network graphs in Streamlit apps.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snehankekre/streamlit-d3graph",
    install_requires=["d3graph>=2.0.1", "streamlit", "seaborn"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
