import streamlit as st
import streamlit.components.v1 as components
from d3graph import d3graph as OrigD3graph
import time
import os
import io

from d3graph.d3graph import *

## Below class extends
## https://github.com/erdogant/d3graph/blob/master/d3graph/d3graph.py
## to display d3graph in Streamlit apps

class d3graph(OrigD3graph):
    @classmethod
    def __init__(self, collision=0.5, charge=250, slider=[None, None], verbose=20):
        library_compatibility_checks()
        # Set the logger
        set_logger(verbose=verbose)
        # Setup configurations
        self.config = {}
        self.config["network_collision"] = collision
        self.config["network_charge"] = charge * -1
        self.config["slider"] = slider
        # Set path locations
        self.config["curpath"] = os.path.dirname(os.path.abspath(__file__))
        self.config["d3_library"] = os.path.abspath(
            os.path.join(self.config["curpath"], "d3js/d3.v3.js")
        )
        self.config["d3_script"] = os.path.abspath(
            os.path.join(self.config["curpath"], "d3js/d3graphscript.js")
        )
        self.config["css"] = os.path.abspath(
            os.path.join(self.config["curpath"], "d3js/style.css")
        )

    @classmethod
    def write_html(self, json_data):
        """Write html.
        Parameters
        ----------
        json_data : json file
            json file to embed in html.

        Returns
        -------
        io.BytesIO.getvalue
            html file.
        """
        self.content = {
            "json_data": json_data,
            "title": self.config["network_title"],
            "width": self.config["figsize"][0],
            "height": self.config["figsize"][1],
            "charge": self.config["network_charge"],
            "edge_distance": self.config["edge_distance"],
            "min_slider": self.config["slider"][0],
            "max_slider": self.config["slider"][1],
            "directed": self.config["directed"],
            "collision": self.config["network_collision"],
        }
        self.jinja_env = Environment(
            loader=PackageLoader(package_name="d3graph", package_path="d3js")
        )
        self.index_template = self.jinja_env.get_template("index.html.j2")

        # Write to in-memory buffer instead of file in /tmp
        with io.BytesIO() as buffer:
            buffer.write(self.index_template.render(self.content).encode())

            return buffer.getvalue()

    def show(self, figsize=(800, 800), title="d3graph", filepath=io.BytesIO()):
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
        time.sleep(0.5)
        self.config["figsize"] = figsize
        self.config["network_title"] = title

        self.config["filepath"] = filepath

        # Create dataframe from co-occurence matrix
        self.G = make_graph(self.node_properties, self.edge_properties)
        # Make slider
        self.setup_slider()
        # Create json
        json_data = json_create(self.G)
        # Create html with json file embedded
        self.buffer = d3graph.write_html(json_data)

        return components.html(
            self.buffer,
            height=self.config["figsize"][1],
            width=self.config["figsize"][0],
        )
