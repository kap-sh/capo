"""Generated from Smithy shape ``com.amazonaws.panorama#NodeInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.input_port_list
    import capo_panorama.types.output_port_list


class NodeInterface(TypedDict, closed=True):
    inputs: "capo_panorama.types.input_port_list.InputPortList"
    """<p>The node interface's inputs.</p>"""
    outputs: "capo_panorama.types.output_port_list.OutputPortList"
    """<p>The node interface's outputs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInterface) -> dict:
    out: dict = {}
    import capo_panorama.types.input_port_list

    out["Inputs"] = capo_panorama.types.input_port_list.serialize_json(value["inputs"])
    import capo_panorama.types.output_port_list

    out["Outputs"] = capo_panorama.types.output_port_list.serialize_json(
        value["outputs"]
    )
    return out


def deserialize_json(data: dict) -> NodeInterface:
    out: NodeInterface = {}  # type: ignore[typeddict-item]
    if data.get("Inputs") is not None:
        import capo_panorama.types.input_port_list

        out["inputs"] = capo_panorama.types.input_port_list.deserialize_json(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("Outputs") is not None:
        import capo_panorama.types.output_port_list

        out["outputs"] = capo_panorama.types.output_port_list.deserialize_json(
            data["Outputs"]
        )
    else:
        out["outputs"] = []
    return out
