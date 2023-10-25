from setuptools import setup


setup(
    name="heartbeat",
    version="0.1.0",
    description="Heartbeat",
    author="Saúl Hernández",
    author_email="saul@teamt.benefi365.com",
    url="",
    packages=[
        'heartbeat',
        'heartbeat.models',
        'heartbeat.migrations',
        'heartbeat.services'
    ],
    scripts=[],
    install_requires=[
        "django>=4.0.0"
    ]
)
