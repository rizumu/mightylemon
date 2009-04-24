from setuptools import setup, find_packages

setup(
    name='mightylemon',
    version='0.1.0',
    description='This is a simple FAQ application.',
    author='brosner',
    author_email='',
    url='http://github.com/rizumu/mightylemon/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
