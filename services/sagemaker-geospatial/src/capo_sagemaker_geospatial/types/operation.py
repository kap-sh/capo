"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Operation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.output_type


class Operation(TypedDict, closed=True):
    name: "str"
    """<p>The name of the operation.</p>"""
    equation: "str"
    """<p>Textual representation of the math operation; Equation used to compute the spectral index.</p>"""
    output_type: NotRequired["capo_sagemaker_geospatial.types.output_type.OutputType"]
    """<p>The type of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Operation) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Equation"] = value["equation"]
    if "output_type" in value:
        out["OutputType"] = value["output_type"]
    return out


def deserialize_json(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Equation") is not None:
        out["equation"] = data["Equation"]
    else:
        out["equation"] = ""
    if data.get("OutputType") is not None:
        out["output_type"] = data["OutputType"]
    return out
