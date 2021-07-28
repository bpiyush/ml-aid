
# Installation

## MacOS with Apple Silicon chip

Install `miniforge3` to manage `conda` enviornments. That is the best way to install dependencies compatible with the new M1 chip. See [this](https://bpiyush.github.io/ml-engg-docs/mac_m1.html) for more details.

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

## Other machines

For usual Intel Mac machines and Linux machines, the above instructions should work normally with `miniconda3` or `anaconda3`.

## Running the code

In order to run the code, you need to set the `PYTHONPATH` as follows:
```bash
cd /path/to/ml-aid/
export PYTHONPATH=$PWD
```