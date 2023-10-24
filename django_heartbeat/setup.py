from setuptools import setup


setup(
    name="heartbeat",
    version="1.0.0",
    description="Heartbeat",
    author="Saúl Hernández",
    author_email="saul@teamt.benefi365.com",
    url="",
    packages=[
        'django_heartbeat.core',
        'django_heartbeat.core.models',
        'django_heartbeat.core.migrations',
    ],
    scripts=[],
    install_requires=[
        "django>=4.0.0"
    ]
)
