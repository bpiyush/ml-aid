
# Installation

* Create a `conda` environment and activate it
  ```bash
  conda create -n ml-aid
  conda activate ml-aid
  ```
* Install `python3.9`
  ```bash
  conda install python=3.9
  ```
* Install requirements
  ```bash
  conda install pandas numpy PyYAML ipdb termcolor matplotlib seaborn
  pip install torch torchvision torchaudio torchtext
  ```


In order to run the code, you need to set the `PYTHONPATH` as follows:
```bash
cd /path/to/ml-aid/
export PYTHONPATH=$PWD
```