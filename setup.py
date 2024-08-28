from setuptools import setup, find_packages

setup(
    name='typing_master',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Typing Master application using LLMs to help improve typing skills.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/typing_master',  # Replace with your GitHub URL or other project link
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'llama_index',
        # Add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'typing_master=typing_master.app:main',  # You can add a main() function in app.py if needed
        ],
    },
)
