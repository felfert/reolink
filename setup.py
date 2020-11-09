from distutils.core import setup
setup(
  name = 'reolink',
  packages = ['reolink'],
  version = '0.1.0',
  license='MIT',
  description = 'Reolink camera package',
  author = 'fwestenberg',
  author_email = '',
  url = 'https://github.com/fwestenberg/reolink',
  download_url = 'https://github.com/fwestenberg/reolink/archive/v_010.tar.gz',
  keywords = ['Reolink', 'Home-Assistant'],
  install_requires=[
          'ffmpeg',
          'requests',
          'aiohttp',
          'hashlib',
          'base64',
          're',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)
