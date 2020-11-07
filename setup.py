import setuptools

setuptools.setup(
    name='optpanda',
    version='0.1.0',
    author='Yuya Takashina',
    author_email='',
    description='Mathematical programming with pandas interface.',
    url='',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['numpy', 'pandas'],
    test_requires=['flake8', 'pytest'],
)
