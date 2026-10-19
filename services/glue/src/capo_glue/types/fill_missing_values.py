"""Generated from Smithy shape ``com.amazonaws.glue#FillMissingValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class FillMissingValues(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    imputed_path: "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>A JSON path to a variable in the data structure for the dataset that is imputed.</p>"""
    filled_path: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>A JSON path to a variable in the data structure for the dataset that is filled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FillMissingValues) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["ImputedPath"] = value["imputed_path"]
    if "filled_path" in value:
        out["FilledPath"] = value["filled_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FillMissingValues:
    out: FillMissingValues = {}  # type: ignore[typeddict-item]
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
    if data.get("ImputedPath") is not None:
        out["imputed_path"] = data["ImputedPath"]
    else:
        out["imputed_path"] = ""
    if data.get("FilledPath") is not None:
        out["filled_path"] = data["FilledPath"]
    return out
