from setuptools import setup, find_packages

setup(
    name='studyplan',
    version='1.0.2',
    url='https://github.com/breitburg/studyplan',
    author='Ilya Breitburg',
    author_email='ilya.breytburg@gmail.com',
    packages=find_packages(),
    python_requires='>=3.7, <4',
    install_requires=['ics>=0.7', 'maya>=0.6.1', 'progress>=1.6'],
    entry_points={'console_scripts': ['studyplan=studyplan:main']},
)
