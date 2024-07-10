from setuptools import setup, find_packages

setup(
    name='algolia-etl',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas',
        'boto3',
        'sqlalchemy',
        'psycopg2-binary',
        'apache-airflow',
    ],
    entry_points='''
        [console_scripts]
        algolia-etl=algolia_etl.cli:cli
    ''',
)