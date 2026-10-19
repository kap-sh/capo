"""Generated from Smithy shape ``com.amazonaws.glue#DropNullFields``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.node_name
    import capo_glue.types.null_check_box_list
    import capo_glue.types.null_value_fields
    import capo_glue.types.one_input


class DropNullFields(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    null_check_box_list: NotRequired[
        "capo_glue.types.null_check_box_list.NullCheckBoxList"
    ]
    """<p>A structure that represents whether certain values are recognized as null values for removal.</p>"""
    null_text_list: NotRequired["capo_glue.types.null_value_fields.NullValueFields"]
    """<p>A structure that specifies a list of NullValueField structures that represent a custom null value such as zero or other value being used as a null placeholder unique to the dataset.</p> <p>The <code>DropNullFields</code> transform removes custom null values only if both the value of the null placeholder and the datatype match the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DropNullFields) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "null_check_box_list" in value:
        import capo_glue.types.null_check_box_list

        out["NullCheckBoxList"] = (
            capo_glue.types.null_check_box_list.serialize_aws_json_1_1(
                value["null_check_box_list"]
            )
        )
    if "null_text_list" in value:
        import capo_glue.types.null_value_fields

        out["NullTextList"] = capo_glue.types.null_value_fields.serialize_aws_json_1_1(
            value["null_text_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DropNullFields:
    out: DropNullFields = {}  # type: ignore[typeddict-item]
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
    if data.get("NullCheckBoxList") is not None:
        import capo_glue.types.null_check_box_list

        out["null_check_box_list"] = (
            capo_glue.types.null_check_box_list.deserialize_aws_json_1_1(
                data["NullCheckBoxList"]
            )
        )
    if data.get("NullTextList") is not None:
        import capo_glue.types.null_value_fields

        out["null_text_list"] = (
            capo_glue.types.null_value_fields.deserialize_aws_json_1_1(
                data["NullTextList"]
            )
        )
    return out
