from setuptools import setup, Extension

setup(name = 'cuda_gridsample',
      packages = setuptools.find_packages(),
      url = 'https://github.com/christinachen94/cuda-gridsample-grad2',
      ext_modules = [Extension(name='cuda_gridsample.extension', 
                               sources=['backend/cuda_gridsample.cpp', 
                                        'backend/cuda_gridsample.cu']
                              )
                    ]
)
