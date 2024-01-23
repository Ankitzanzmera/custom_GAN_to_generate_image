from setuptools import setup,find_packages


setup(
    name = "custom_GAN",
    version = "0.0.0",
    author = "Ankit M Zanzmera",
    author_email = "22msrds052@jainuniversity.ac.in",
    url = 'https://github.com/Ankitzanzmera/custom_GAN_to_generate_image',
    packages = find_packages(where="src"),
    package_dir = {"":"src"}
)