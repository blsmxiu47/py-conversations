import setuptools

setuptools.setup(
    name="py_conversations",
    packages=setuptools.find_packages(exclude=["py_conversations_tests"]),
    install_requires=[
        "dagster==0.14.6",
        "dagit==0.14.6",
        "pytest",
    ],
)
