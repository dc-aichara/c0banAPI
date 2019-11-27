import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
  name='c0banAPI',
  packages=['c0banAPI'],
  version='1.5',
  license='MIT',
  description='c0banAPI will request c0ban blockchain insight api to get blocks and transactions related data',
  author='Dayal Chand Aichara',
  author_email='dc.aichara@gmail.com',
  url='https://github.com/dc-aichara/c0banAPI',
  download_url='https://github.com/dc-aichara/c0banAPI/archive/v-1.5.tar.gz',
  keywords=['c0ban', 'blockchain', 'cryptocurrency', 'blocks', 'c0bantrade', 'c0banPrice'],
  install_requires=['requests', 'pandas'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Operating System :: OS Independent'
  ],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
