"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CustomProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.message
    import capo_iotfleetwise.types.node_data_encoding
    import capo_iotfleetwise.types.node_data_type
    import capo_iotfleetwise.types.node_path
    import capo_iotfleetwise.types.string


class CustomProperty(TypedDict, closed=True):
    fully_qualified_name: "capo_iotfleetwise.types.string.string"
    """<p>The fully qualified name of the custom property. For example, the fully qualified name of a custom property might be <code>ComplexDataTypes.VehicleDataTypes.SVMCamera.FPS</code>.</p>"""
    data_type: "capo_iotfleetwise.types.node_data_type.NodeDataType"
    """<p>The data type for the custom property. </p>"""
    data_encoding: NotRequired[
        "capo_iotfleetwise.types.node_data_encoding.NodeDataEncoding"
    ]
    """<p>Indicates whether the property is binary data.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the custom property.</p>"""
    deprecation_message: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>The deprecation message for the node or the branch that was moved or deleted.</p>"""
    comment: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>A comment in addition to the description.</p>"""
    struct_fully_qualified_name: NotRequired[
        "capo_iotfleetwise.types.node_path.NodePath"
    ]
    """<p>The fully qualified name of the struct node for the custom property if the data type of the custom property is <code>Struct</code> or <code>StructArray</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomProperty) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import capo_iotfleetwise.types.node_data_type

    out["dataType"] = capo_iotfleetwise.types.node_data_type.serialize_aws_json_1_0(
        value["data_type"]
    )
    if "data_encoding" in value:
        import capo_iotfleetwise.types.node_data_encoding

        out["dataEncoding"] = (
            capo_iotfleetwise.types.node_data_encoding.serialize_aws_json_1_0(
                value["data_encoding"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "deprecation_message" in value:
        out["deprecationMessage"] = value["deprecation_message"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "struct_fully_qualified_name" in value:
        out["structFullyQualifiedName"] = value["struct_fully_qualified_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomProperty:
    out: CustomProperty = {}  # type: ignore[typeddict-item]
    if data.get("fullyQualifiedName") is not None:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        out["fully_qualified_name"] = ""
    if data.get("dataType") is not None:
        import capo_iotfleetwise.types.node_data_type

        out["data_type"] = (
            capo_iotfleetwise.types.node_data_type.deserialize_aws_json_1_0(
                data["dataType"]
            )
        )
    else:
        import typing

        out["data_type"] = typing.cast(
            "capo_iotfleetwise.types.node_data_type.NodeDataType", ""
        )
    if data.get("dataEncoding") is not None:
        import capo_iotfleetwise.types.node_data_encoding

        out["data_encoding"] = (
            capo_iotfleetwise.types.node_data_encoding.deserialize_aws_json_1_0(
                data["dataEncoding"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("deprecationMessage") is not None:
        out["deprecation_message"] = data["deprecationMessage"]
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("structFullyQualifiedName") is not None:
        out["struct_fully_qualified_name"] = data["structFullyQualifiedName"]
    return out
