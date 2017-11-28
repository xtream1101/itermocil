from setuptools import setup, find_packages

setup(
    name='itermocil',
    version='0.2.1.5',
    url='https://github.com/xtream1101/itermocil',
    license='MIT',
    description='Create pre-defined window/pane layouts and run commands in iTerm',
    author='Eddy Hintze',
    author_email='edy@hintze.co',
    packages=find_packages(),
    py_modules=['itermocil'],
    package_data={},
    classifiers=[],
    entry_points={
        'console_scripts': [
            'itermocil = itermocil:main',
        ]
    },
    install_requires=[
        'PyYAML',
    ]
)
