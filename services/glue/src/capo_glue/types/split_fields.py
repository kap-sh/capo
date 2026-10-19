"""Generated from Smithy shape ``com.amazonaws.glue#SplitFields``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class SplitFields(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    paths: "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    """<p>A JSON path to a variable in the data structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitFields) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.glue_studio_path_list

    out["Paths"] = capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["paths"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitFields:
    out: SplitFields = {}  # type: ignore[typeddict-item]
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
    if data.get("Paths") is not None:
        import capo_glue.types.glue_studio_path_list

        out["paths"] = capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
            data["Paths"]
        )
    else:
        out["paths"] = []
    return out
