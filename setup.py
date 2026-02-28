from setuptools import setup, find_packages

setup(
    name="brainflow",
    version="1.0.0",
    author="sayan", # এখানে আপনার নাম দিন
    description="A library to make AI act like a human brain with a single function.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/sayan9168/brainflow", # আপনার গিটহাব লিংক দিন
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
