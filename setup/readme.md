
# Installation

## MacOS with Apple Silicon chip

Install `miniforge3` to manage `conda` enviornments. That is the best way to install dependencies compatible with the new M1 chip. See [this](https://bpiyush.github.io/ml-engg-docs/mac_m1.html) for more details.

### Short-cut instructions

Use `setup/env.yml` file to create a `conda` environment.

```bash
cd setup/
conda env create --file env.yml
```

This will create a `conda` env called `ml-aid`. Activate it and start using!
```bash
conda activate ml-aid
```

### Detailed instructions

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

For usual Intel Mac machines and Linux machines, the above instructions should work normally with `miniconda3` or `anaconda3`. But these have only been tested on Mac M1 chip machine.

## Running the code

In order to run the code, you need to set the `PYTHONPATH` as follows:
```bash
cd /path/to/ml-aid/
export PYTHONPATH=$PWD
```