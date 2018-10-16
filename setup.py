from setuptools import setup


setup(
    name='hostport',
    version='1.0',
    description='Simple host:port parser',
    long_description=open('README.rst', 'r').read(),
    author='Zelenyak "ZZZ" Alexander',
    author_email='zzz.sochi@gmail.com',
    url='https://github.com/zzzsochi/hostport',
    license='BSD',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['hostport'],
    tests_require=['pytest']
)
