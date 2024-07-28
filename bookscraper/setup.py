from setuptools import setup, find_packages

setup(
    name='bookscraper',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Scrapy==2.11.2',
        'Flask==2.1.1',
        'psycopg2-binary==2.9.3',
        'confluent_kafka==1.7.0',
    ],
    entry_points={
        'console_scripts': [
            'runserver = bookscraper.flask_app.app:main',
        ],
    },
    package_data={
        'bookscraper': [
            'flask_app/templates/*.html',
            'flask_app/static/css/*.css',
            'flask_app/static/*.jpg',
            'flask_app/static/*.webp',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
