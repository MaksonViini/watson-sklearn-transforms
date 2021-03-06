from setuptools import setup
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'

install_requires = []  # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(
    name='my_custom_sklearn_transforms',
    version='1.0',
    description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
    url='https://github.com/MaksonViini/watson-sklearn-transforms',
    author='Makson Vinicio',
    author_email='maksonvinicio7@gmail.com',
    license='BSD',
    packages=[
        'my_custom_sklearn_transforms'
    ],
    zip_safe=False,
    install_requires=install_requires
)
