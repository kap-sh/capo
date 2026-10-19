"""Generated from Smithy shape ``com.amazonaws.glue#Union``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.node_name
    import capo_glue.types.two_inputs
    import capo_glue.types.union_type


class Union(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.two_inputs.TwoInputs"
    """<p>The node ID inputs to the transform.</p>"""
    union_type: "capo_glue.types.union_type.UnionType"
    """<p>Indicates the type of Union transform. </p> <p>Specify <code>ALL</code> to join all rows from data sources to the resulting DynamicFrame. The resulting union does not remove duplicate rows.</p> <p>Specify <code>DISTINCT</code> to remove duplicate rows in the resulting DynamicFrame.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Union) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.two_inputs

    out["Inputs"] = capo_glue.types.two_inputs.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.union_type

    out["UnionType"] = capo_glue.types.union_type.serialize_aws_json_1_1(
        value["union_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Union:
    out: Union = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.two_inputs

        out["inputs"] = capo_glue.types.two_inputs.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("UnionType") is not None:
        import capo_glue.types.union_type

        out["union_type"] = capo_glue.types.union_type.deserialize_aws_json_1_1(
            data["UnionType"]
        )
    else:
        import typing

        out["union_type"] = typing.cast("capo_glue.types.union_type.UnionType", "")
    return out
