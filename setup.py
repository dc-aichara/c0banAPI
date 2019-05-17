from distutils.core import setup
setup(
  name = 'c0banAPI',
  packages = ['c0banAPI'],
  version = '01',
  license='MIT',
  description = 'c0banAPI will request c0ban blockchain insight api to get blocks and transactions related data',
  author = 'Dayal Chand Aichara',
  author_email = 'dc.aichara@gmail.com',
  url = 'https://github.com/dc-aichara/c0banAPI',
  download_url = 'https://github.com/dc-aichara/c0banAPI/archive/v_01.tar.gz',
  keywords = ['c0ban', 'blockchain', 'cryptocurrency, blocks'],
  install_requires=[
          'requests',
          'json',
          ''
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
