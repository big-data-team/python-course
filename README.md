# About

The repository is used during the following courses:
1. Effective Python

- How to write clean, maintainable and scalable code on Python
- https://bigdatateam.org/ru/python-course

2. Python for Big Data

- unix CLI
- data analysis with regex, pandas and SQL
- reproducible research
- computer science fundamentals: data structures, algorithms, Big O notation (complexity)
- https://bigdatateam.org/ru/python-for-big-data-analysis

# Environment Configuration

1. Download [requirements.txt](requirements.txt)
2. Create environment:
```bash
export env_name="bdt-python-course"
conda create -n $env_name python=3.10
conda activate $env_name
# there are packages that no more supported by conda
# so, intead of this:
conda install --file requirements.txt
# call directly pip:
pip install -r requirements.txt
```

For more information about Python virtual environments see:
* https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
* https://docs.python.org/3/library/site.html
* https://docs.python.org/3/library/venv.html

See available conda environments with the help of:
```bash
conda info --envs
```

If you need to remove environment use the following command:
```bash
conda remove --name $env_name --all
```

# HowTos

How to use pylint:
```bash
pylint --output-format=colorized -v inverted_index.py
# in case you would like to ignore some warnings:
pylint --output-format=colorized -d C0111,C0103 -v inverted_index.py
pylint --output-format=colorized -d invalid-name,missing-docstring -v inverted_index.py
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
3. [DVC experimental data](https://drive.google.com/file/d/1D-YgtxAlr5Gf--8nWY1p4N8G1tFa94xc/view?usp=sharing) - do not forget to unzip after download
4. [Stackoverflow posts dump sample (XML)](https://drive.google.com/file/d/1oDUNOK1Ap0-YV930Z78WQZVuKHtqZ2WC/view)
5. [Pandas HW data](https://drive.google.com/file/d/196D3snvk5hL3_aeIYnKPJXA1HUYrxMky/view)

# Study Artefacts

1. [Flask 404 template](https://drive.google.com/open?id=1EpBf995F7zENPKkUqKq1qP3vFfq0cpgF)


# Contributors

<a href = "https://github.com/big-data-team/python-course/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=big-data-team/python-course"/>
</a>

<!-- made with [contributors-img](https://contrib.rocks) -->
