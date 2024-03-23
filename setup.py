from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="exif-frame",
    version="v1.0.5",
    author="Cyan@https://github.com/cyan-io",
    author_email="cyan-io@outlook.com",
    url="https://github.com/cyan-io/exif-frame",
    download_url="https://github.com/cyan-io/exif-frame/releases",
    license="MPL 2.0",
    include_package_data=True,
    packages=find_packages(),
    entry_points={"console_scripts": ["frame = frame.frame:main"]},
    install_requires=["PyYAML", "pillow"],
    platforms="any",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.6",
)
