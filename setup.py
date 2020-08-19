from setuptools import setup

setup(name='investecli',
    version='0.1',
    description='Investec CLI tool for checking your bank account',
    author='Ross Purdon',
    author_email='admin@rosspurdon.com',
    license='MIT',
    packages=['cli'],
    install_requires=[
        'requests',
        'tabulate',
        'fire'
    ],
    entry_points = {
        'console_scripts': ['investecli=cli:main'],
    },
    include_package_data=True,
    zip_safe=False)
