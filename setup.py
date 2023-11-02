from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Precarious codes'
 
# Setting up
setup(
    name="Precarious",
    version=VERSION,
    author="Pinkman Jessie",
    author_email="<jessie.pinkman1123@hotmail.com>",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['qiskit','numpy', 'matplotlib', 'scikit-learn', 'tensorflow','plotly','category_encoders','gym'],
    keywords=['python', 'codes'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)