from setuptools import setup


setup(
    name="heartbeat",
    version="1.0.0",
    description="Heartbeat",
    author="Saúl Hernández",
    author_email="saul@teamt.benefi365.com",
    url="",
    packages=[
        'core',
        'core.models',
        'core.migrations',
    ],
    scripts=[],
    install_requires=[
        "django>=4.0.0"
    ]
)
