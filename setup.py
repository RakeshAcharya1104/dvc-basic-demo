from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Rakesh",
    description="DVC Demo",
    url="https://github.com/RakeshAcharya1104/dvc-basic-demo.git",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="GNU",
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)