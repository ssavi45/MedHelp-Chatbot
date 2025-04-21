from setuptools import find_packages, setup

setup(
    name='MedHelp',
    version='0.0.1',
    author='CSE299#Group-8 (Shoumik, Shefat, Anik)',
    author_email='group08@northsouth.edu',
    packages=find_packages(),
    install_requires=[
        "langchain>=0.2.0",
        "langchain-community>=0.0.10",
        "pinecone-client>=3.0.0",
        "python-dotenv",
        "sentence-transformers",
    ]
)
