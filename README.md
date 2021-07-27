# ML-AID: ML and AI Development
Utilities for ML and AI Development towards research

## Installation

The setup is done via a `conda` environment. Please follow the steps [here](setup/readme.md) for instructions.

## Utilities

### IO

For basic input/output operations w.r.t. `yml`, `pkl`, `json` and `txt` files, please refer to the following example:

```python
from mlaid.utils.io import load_yml, save_yml

# define sample dict
data = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# save the dict into `yml` file
yml_path = "assets/data.yml"
save_yml(data, yml_path)

# load the dict from `yml` file
data = read_yml(yml_path)
```

### Basic operations

* Converting a torch tensor into numpy ndarray and vice-versa:
```python
from mlaid.utils.ops import tensorize, numpify

x = torch.ones((3, 4, 5), requires_grad=True)
x = numpify(x)

x = np.ones((3, 4, 5))
x = tensorize(x)
```

* Getting and setting values in a nested dictionary
```python
from mlaid.utils.ops import get_from_dict, set_in_dict

x = {"a": {"b": {"c": 2}}, "x": 3}

# get value from nested dictionary
value = get_from_dict(x, ["a", "b", "c"])
# value = x["a"]["b"]["c"] = 2

# set value in the dictionary
set_in_dict(x, ["a", "b", "c"], value=10)
# x = {"a": {"b": {"c": 10}}, "x": 3}
```

* Convert a dictionary to class with attributes accesible via dot notation

```python
from mlaid.utils.ops import DotDict

x = {"a": {"b": {"c": 2}}, "x": 3}
y = DotDict(x)
print(y.a.b.c) # prints 2
```

* Logging helpers

```python
from mlaid.utils.log import color, print_update

# print yellow-colored message
print(color("Sample colored message", "yellow"))

# print message as an update
print_update("Sample update message")
```