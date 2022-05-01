from setuptools import setup

setup(
    name="hubitat-events-dhan",
    version="0.0.1",
    author="D Han",
    author_email="emaildhan@gmail.com",
    description="Package for fetching hubitat events",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=["requests"],
    package_dir={"hubitat_events": "hubitat_events"},
    url="https://github.com/programmerdays/Hubitat-Events",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=["flake8"]
    # [flake8]
    # max-line-length = 88
    # extend-ignore = E203
)