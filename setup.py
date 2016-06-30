from setuptools import setup

setup(name='pasta',
      version='0.1',
      description='The Yangcong Data Requirement ToolKit',
      url='http://github.com/guanghetv/pasta',
      author='ronfe',
      author_email='hongfei@guanghe.tv',
      license='MIT',
      packages=['pasta'],
      install_requires=[
          'pymongo'
      ],
      zip_safe=False)