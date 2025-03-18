from setuptools import setup, find_packages

setup(
    name='mantis-vl',
    version='0.0.5',
    description='Official Codes for of "MANTIS: Interleaved Multi-Image Instruction Tuning"',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dongfu Jiang',
    author_email='dongfu.jiang@uwaterloo.ca',
    packages=find_packages(),
    url='https://github.com/TIGER-AI-Lab/Mantis',
    install_requires=[
        "transformers",
        "sentencepiece",
        "torch",
        "Pillow",
        "torch",
        "accelerate",
        "torchvision",
        "datasets",
        "diffusers",
        "decord",
        "ring"
    ],
    extras_require={
        "train": [
            "fire",
            "tqdm",
            "numpy",
            "requests",
            "matplotlib",
            "transformers",
            "transformers_stream_generator",
            "tiktoken",
            "chardet",
            "deepspeed",
            "peft>=0.10",
            "bitsandbytes",
            "wandb",
            "ninja",
            "scipy",
            "webdataset",
            "braceexpand",
            "pandas",
            "orjson",
            "prettytable",
            "pytest",
            "opencv-python",
            "pyarrow",
            "dask",
            "einops-exts",
            "datasets",
            "open_clip_torch",
            "openai",
            "av",
            "qwen_vl_utils",
            "ring-flash-attn @ git+https://github.com/jdf-prog/ring-flash-attention.git",
        ],
        "eval": [
            "tqdm",
            "numpy",
            "prettytable",
            "fire",
            "datasets",
            "openai",
            "tiktoken",
            "av",
            "decord",
        ]
    }
)



# change it to pyproject.toml
# [build-system]
# python setup.py sdist bdist_wheel
# twine upload dist/*