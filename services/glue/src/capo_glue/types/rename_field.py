"""Generated from Smithy shape ``com.amazonaws.glue#RenameField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class RenameField(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    source_path: (
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    )
    """<p>A JSON path to a variable in the data structure for the source data.</p>"""
    target_path: (
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    )
    """<p>A JSON path to a variable in the data structure for the target data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameField) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.enclosed_in_string_properties

    out["SourcePath"] = (
        capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["source_path"]
        )
    )
    import capo_glue.types.enclosed_in_string_properties

    out["TargetPath"] = (
        capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["target_path"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenameField:
    out: RenameField = {}  # type: ignore[typeddict-item]
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
    if data.get("SourcePath") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["source_path"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["SourcePath"]
            )
        )
    else:
        out["source_path"] = []
    if data.get("TargetPath") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["target_path"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["TargetPath"]
            )
        )
    else:
        out["target_path"] = []
    return out
