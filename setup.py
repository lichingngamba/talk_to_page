from setuptools import setup, find_packages

setup(
    name="talk_to_page",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4==4.12.3', 'PyPDF2==3.0.1',
        'python-dotenv==1.0.1', 'haystack-ai==2.9.0',
        'streamlit==1.41.1', 
    ],

    entry_points={
        'console_scripts': [
            'start=streamlit.web.cli:main run chatbot.py',
        ],
    },
    
    author="Liching",
    author_email="lichingngamba@gmail.com",
    description="The project is a side project that crawls and scrap the content of a webpage, to response to a simple natural query",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/talk_to_page",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='==3.10',
)