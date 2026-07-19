from setuptools import setup, Extension
import pybind11
import os

# Bulunduğumuz dizin ve ONNX dizini
current_dir = os.path.dirname(os.path.abspath(__file__))
onnx_dir = os.path.join(current_dir, "onnxruntime")

# C++ Çekirdek dizinimizin tam yolunu (bir üst klasöre çıkarak) belirliyoruz
core_cpp_dir = os.path.abspath(os.path.join(current_dir, "..", "core_cpp", "DnaCoreEngine", "DnaCoreEngine"))

cpp_module = Extension(
    'dnacore',
    # Derleyiciye DnaCore.cpp dosyasının orijinal yerini gösteriyoruz
    sources=['wrapper.cpp', os.path.join(core_cpp_dir, 'DnaCore.cpp')],
    include_dirs=[
        pybind11.get_include(),
        os.path.join(onnx_dir, "include"),
        core_cpp_dir  # DnaCore.h dosyasının nerede olduğunu söylüyoruz
    ],
    library_dirs=[
        os.path.join(onnx_dir, "lib")
    ],
    libraries=['onnxruntime'],
    language='c++',
    extra_compile_args=['/std:c++17', '/O2']
)

setup(
    name='dnacore',
    version='1.0',
    ext_modules=[cpp_module],
)