"""Generated from Smithy shape ``com.amazonaws.glue#Mapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.mappings


class Mapping(TypedDict, closed=True):
    to_key: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>After the apply mapping, what the name of the column should be. Can be the same as <code>FromPath</code>.</p>"""
    from_path: NotRequired[
        "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    ]
    """<p>The table or column to be modified.</p>"""
    from_type: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The type of the data to be modified.</p>"""
    to_type: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The data type that the data is to be modified to.</p>"""
    dropped: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>If true, then the column is removed.</p>"""
    children: NotRequired["capo_glue.types.mappings.Mappings"]
    """<p>Only applicable to nested data structures. If you want to change the parent structure, but also one of its children, you can fill out this data strucutre. It is also <code>Mapping</code>, but its <code>FromPath</code> will be the parent's <code>FromPath</code> plus the <code>FromPath</code> from this structure.</p> <p>For the children part, suppose you have the structure:</p> <p> <code>{ "FromPath": "OuterStructure", "ToKey": "OuterStructure", "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner", "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }</code> </p> <p>You can specify a <code>Mapping</code> that looks like:</p> <p> <code>{ "FromPath": "OuterStructure", "ToKey": "OuterStructure", "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner", "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Mapping) -> dict:
    out: dict = {}
    if "to_key" in value:
        out["ToKey"] = value["to_key"]
    if "from_path" in value:
        import capo_glue.types.enclosed_in_string_properties

        out["FromPath"] = (
            capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
                value["from_path"]
            )
        )
    if "from_type" in value:
        out["FromType"] = value["from_type"]
    if "to_type" in value:
        out["ToType"] = value["to_type"]
    if "dropped" in value:
        out["Dropped"] = value["dropped"]
    if "children" in value:
        import capo_glue.types.mappings

        out["Children"] = capo_glue.types.mappings.serialize_aws_json_1_1(
            value["children"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Mapping:
    out: Mapping = {}  # type: ignore[typeddict-item]
    if data.get("ToKey") is not None:
        out["to_key"] = data["ToKey"]
    if data.get("FromPath") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["from_path"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["FromPath"]
            )
        )
    if data.get("FromType") is not None:
        out["from_type"] = data["FromType"]
    if data.get("ToType") is not None:
        out["to_type"] = data["ToType"]
    if data.get("Dropped") is not None:
        out["dropped"] = data["Dropped"]
    if data.get("Children") is not None:
        import capo_glue.types.mappings

        out["children"] = capo_glue.types.mappings.deserialize_aws_json_1_1(
            data["Children"]
        )
    return out
