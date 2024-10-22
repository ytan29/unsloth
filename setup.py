from setuptools import setup, find_packages

setup(
    name='unsloth_ai',             # Name of your customized package
    version='0.0.1',               # Versioning of your package
    description='Unsloth AI with triton-lang backend for Intel XPU',
    author='ytan29',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[             # List required dependencies
        'packaging',               # Include any dependencies from Unsloth AI
        'tyro',
        'transformers>=4.45.1',
        'datasets>=2.16.0',
        'sentencepiece>=0.2.0',
        'tqdm',
        'psutil',
        'wheel>=0.42.0',
        'numpy',
        'accelerate>=0.26.1',
        'trl>=0.7.9,!=0.9.0,!=0.9.1,!=0.9.2,!=0.9.3',
        'peft>=0.7.1,!=0.11.0',
        'protobuf<4.0.0',
        'huggingface_hub',
        'hf_transfer',
    ]
)
