"""Generated from Smithy shape ``com.amazonaws.glue#DropDuplicates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.limited_path_list
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class DropDuplicates(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    columns: NotRequired["capo_glue.types.limited_path_list.LimitedPathList"]
    """<p>The name of the columns to be merged or removed if repeating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DropDuplicates) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "columns" in value:
        import capo_glue.types.limited_path_list

        out["Columns"] = capo_glue.types.limited_path_list.serialize_aws_json_1_1(
            value["columns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DropDuplicates:
    out: DropDuplicates = {}  # type: ignore[typeddict-item]
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
    if data.get("Columns") is not None:
        import capo_glue.types.limited_path_list

        out["columns"] = capo_glue.types.limited_path_list.deserialize_aws_json_1_1(
            data["Columns"]
        )
    return out
