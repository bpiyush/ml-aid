# ML-AID: ML and AI Development
Utilities for ML and AI Development towards research

## Utilities

### IO

For basic input/output operations w.r.t. `yml`, `pkl`, `json` and `txt` files, please refer to the following example:

```python
from mlaid.utils.io import load_yml, save_yml

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
