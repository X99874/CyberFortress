from setuptools import setup, find_packages

setup(
    name="CyberFortress",  
    version="0.1.0",         
    description="A cool Python project",  
    author="X99874",      
    author_email="youremail@example.com",  
    packages=find_packages(Docker),  
    install_requires=[       
        "requests",
        "numpy",
    ],
    extras_require={         
        "dev": [
            "pytest",
        ],
    },
    classifiers=[            
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: APACHE LICENSE",
    ],
)
