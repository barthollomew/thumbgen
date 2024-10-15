from setuptools import setup, find_packages

setup(
    name='thumbgen',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'python-pptx',
        'pdf2image'
    ],
    entry_points={
        'console_scripts': [
            'thumbgen=thumbgen.cli:main',
        ],
    },
)
