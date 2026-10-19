"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Actuator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.double
    import capo_iotfleetwise.types.list_of_strings
    import capo_iotfleetwise.types.message
    import capo_iotfleetwise.types.node_data_type
    import capo_iotfleetwise.types.node_path
    import capo_iotfleetwise.types.string


class Actuator(TypedDict, closed=True):
    fully_qualified_name: "capo_iotfleetwise.types.string.string"
    """<p>The fully qualified name of the actuator. For example, the fully qualified name of an actuator might be <code>Vehicle.Front.Left.Door.Lock</code>.</p>"""
    data_type: "capo_iotfleetwise.types.node_data_type.NodeDataType"
    """<p>The specified data type of the actuator. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the actuator.</p>"""
    unit: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>The scientific unit for the actuator.</p>"""
    allowed_values: NotRequired["capo_iotfleetwise.types.list_of_strings.listOfStrings"]
    """<p>A list of possible values an actuator can take.</p>"""
    min: NotRequired["capo_iotfleetwise.types.double.double"]
    """<p>The specified possible minimum value of an actuator.</p>"""
    max: NotRequired["capo_iotfleetwise.types.double.double"]
    """<p>The specified possible maximum value of an actuator.</p>"""
    assigned_value: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>A specified value for the actuator.</p>"""
    deprecation_message: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>The deprecation message for the node or the branch that was moved or deleted.</p>"""
    comment: NotRequired["capo_iotfleetwise.types.message.message"]
    """<p>A comment in addition to the description.</p>"""
    struct_fully_qualified_name: NotRequired[
        "capo_iotfleetwise.types.node_path.NodePath"
    ]
    """<p>The fully qualified name of the struct node for the actuator if the data type of the actuator is <code>Struct</code> or <code>StructArray</code>. For example, the struct fully qualified name of an actuator might be <code>Vehicle.Door.LockStruct</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Actuator) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import capo_iotfleetwise.types.node_data_type

    out["dataType"] = capo_iotfleetwise.types.node_data_type.serialize_aws_json_1_0(
        value["data_type"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "unit" in value:
        out["unit"] = value["unit"]
    if "allowed_values" in value:
        import capo_iotfleetwise.types.list_of_strings

        out["allowedValues"] = (
            capo_iotfleetwise.types.list_of_strings.serialize_aws_json_1_0(
                value["allowed_values"]
            )
        )
    if "min" in value:
        out["min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    if "assigned_value" in value:
        out["assignedValue"] = value["assigned_value"]
    if "deprecation_message" in value:
        out["deprecationMessage"] = value["deprecation_message"]
    if "comment" in value:
        out["comment"] = value["comment"]
    if "struct_fully_qualified_name" in value:
        out["structFullyQualifiedName"] = value["struct_fully_qualified_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Actuator:
    out: Actuator = {}  # type: ignore[typeddict-item]
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    if data.get("allowedValues") is not None:
        import capo_iotfleetwise.types.list_of_strings

        out["allowed_values"] = (
            capo_iotfleetwise.types.list_of_strings.deserialize_aws_json_1_0(
                data["allowedValues"]
            )
        )
    if data.get("min") is not None:
        out["min"] = float(data["min"])
    if data.get("max") is not None:
        out["max"] = float(data["max"])
    if data.get("assignedValue") is not None:
        out["assigned_value"] = data["assignedValue"]
    if data.get("deprecationMessage") is not None:
        out["deprecation_message"] = data["deprecationMessage"]
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("structFullyQualifiedName") is not None:
        out["struct_fully_qualified_name"] = data["structFullyQualifiedName"]
    return out
