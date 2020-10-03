# About

How to write clean, maintainable and scalable code on Python:
- https://bigdatateam.org/python-course

# Environment Configuration

1. Download [requirements.txt](requirements.txt)
2. Create environment:
```bash
export env_name="bdt-python-course"
conda create -n $env_name python=3.7
conda activate $env_name
conda install --file requirements.txt
```

# HowTos

How to use pylint:
```bash
pylint --output-format=colorized -d C0111,C0103 -v inverted_index.py
```

How to use pytest:
```bash
pytest -v .
pytest --cov -v .
pytest --cov -vv --durations=0 .
```

# Study Datasets

1. [Wikipedia sample](https://drive.google.com/open?id=1ASO-nWW5FpvM7PfpOxxPu-0imjcMZhqN) - do not forget to unzip after download
2. [Stop words](https://drive.google.com/open?id=1NBPhZzUyFc0e-_vQwZpxtrxBqzCsB9Yg)

