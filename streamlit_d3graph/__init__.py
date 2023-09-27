import streamlit.components.v1 as components
from d3graph import d3graph as OrigD3graph
from d3graph.d3graph import *  # noqa: F403

## Below class extends
## https://github.com/erdogant/d3graph/blob/master/d3graph/d3graph.py
## to display d3graph in Streamlit apps


class d3graph(OrigD3graph):
    def show(self, figsize=(800, 800), title="d3graph", *args, **kwargs):
        """Build and show the graph.

        Parameters
        ----------
        figsize : tuple, (default: (800, 800))
            Size of the figure in the browser, [height, width].
        title : String, (default: None)
            Title of the figure.

        Examples
        --------

        >>> import streamlit as st
        >>> from streamlit_d3graph import d3graph
        >>>
        >>> d3 = d3graph()
        >>> adjmat, df = d3.import_example('karate')
        >>> label = df['label'].values
        >>> node_size = df['degree'].values
        >>> d3.graph(adjmat)
        >>> d3.set_node_properties(color=df['label'].values)
        >>> d3.show()

        """

        return components.html(
            # Create html with json file embedded
            super().show(figsize, title, *args, filepath=None, **kwargs),
            height=self.config["figsize"][1],
            width=self.config["figsize"][0],
        )
