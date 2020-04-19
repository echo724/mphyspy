from setuptools import find_packages, setup
import setuptools

# Read in the README for the long description on PyPI
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
      name='mphyspy',
      version='0.1.9',
      description='Python3 library for calculating college modern physics',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/eunchan1001/mphyspy.git',
      author='Eunchan Cho',
      author_email='eunchan1001@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3.7',
          ],
      zip_safe=False)
