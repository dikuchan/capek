import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='capek',
    version='0.8.2',
    author='dikuchan',
    author_email='dikuchan@protonmail.com',
    description='A convenient template for developing TORCS robots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dikuchan/capek',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.7'
)
