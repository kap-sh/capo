"""Generated from Smithy shape ``com.amazonaws.glue#SelectFromCollection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.node_name
    import capo_glue.types.non_negative_int
    import capo_glue.types.one_input


class SelectFromCollection(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    index: "capo_glue.types.non_negative_int.NonNegativeInt"
    """<p>The index for the DynamicFrame to be selected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectFromCollection) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Index"] = value.get("index", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectFromCollection:
    out: SelectFromCollection = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("Index") is not None:
        out["index"] = data["Index"]
    else:
        out["index"] = 0
    return out
