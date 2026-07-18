"""
=============================================================================
DNA Storage AI - pybind11 Setup Configuration
=============================================================================
Bu kurulum dosyası, C++ çekirdek motorunu (DnaCore.cpp) Visual Studio
derleyicisi aracılığıyla derleyerek Python sanal ortamına entegre eder.

Kullanım: pip install . --no-build-isolation
=============================================================================
"""

from setuptools import setup, Extension
import pybind11

# Derlenecek C++ modülünün kaynak ve başlık (header) yolları
ext_modules = [
    Extension(
        'dnacore',
        sources=[
            'wrapper.cpp',
            '../core_cpp/DnaCoreEngine/DnaCoreEngine/DnaCore.cpp' 
        ],
        include_dirs=[
            pybind11.get_include(),
            '../core_cpp/DnaCoreEngine/DnaCoreEngine' 
        ],
        language='c++'
    ),
]

# Modülün paketlenme ayarları
setup(
    name='dnacore',
    version='1.0',
    description='DNA Storage C++ Core Engine for Python',
    ext_modules=ext_modules,
)