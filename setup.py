from distutils.core import setup
setup(
  name = 'gli_py',         
  packages = ['gli_py'],   
  version = '0.0.3',      
  license='	gpl-3.0',       
  description = 'A python 3 API wrapper for GL-inet routers for consumption by Home Assistant',   
  author = 'HarvsG',
  author_email = 'doctor@codingdoctor.co.uk',
  url = 'https://github.com/HarvsG/gli_py',
  download_url = 'https://github.com/HarvsG/gli_py/archive/refs/tags/0.0.3.tar.gz',
  keywords = ['API', 'Router', 'Home Assistant'],
  install_requires=[
          'uplink',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.8',
  ],
)