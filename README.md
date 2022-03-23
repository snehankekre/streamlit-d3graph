# streamlit-d3graph

**A simple component to display [d3graph](https://github.com/erdogant/d3graph) network graphs in Streamlit apps.** 

This component is powered by [d3graph](https://github.com/erdogant/d3graph), a Python package that simplifies the task of creating interactive and stand-alone networks in d3 JavaScript using Python.

---

<h3 align="center">
  🕸️ <a href="https://share.streamlit.io/snehankekre/streamlit-d3graph/main/examples/example.py">Live demo</a> 🕸️
</h3>

---

## Installation

```bash
pip install streamlit-d3graph
```

## Usage

```python
import streamlit as st
from streamlit_d3graph import d3graph

# Initialize
d3 = d3graph()
# Load karate example
adjmat, df = d3.import_example('karate')

label = df['label'].values
node_size = df['degree'].values

d3.graph(adjmat)
d3.set_node_properties(color=df['label'].values)
d3.show()

d3.set_node_properties(label=label, color=label, cmap='Set1')
d3.show()
```
