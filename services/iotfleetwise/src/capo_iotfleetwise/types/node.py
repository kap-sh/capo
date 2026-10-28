"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Node``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.actuator
    import capo_iotfleetwise.types.attribute
    import capo_iotfleetwise.types.branch
    import capo_iotfleetwise.types.custom_property
    import capo_iotfleetwise.types.custom_struct
    import capo_iotfleetwise.types.sensor


class NodeBranchMember(TypedDict, closed=True):
    branch: "capo_iotfleetwise.types.branch.Branch"


class NodeSensorMember(TypedDict, closed=True):
    sensor: "capo_iotfleetwise.types.sensor.Sensor"


class NodeActuatorMember(TypedDict, closed=True):
    actuator: "capo_iotfleetwise.types.actuator.Actuator"


class NodeAttributeMember(TypedDict, closed=True):
    attribute: "capo_iotfleetwise.types.attribute.Attribute"


class NodeStructMember(TypedDict, closed=True):
    struct: "capo_iotfleetwise.types.custom_struct.CustomStruct"


class NodePropertyMember(TypedDict, closed=True):
    property: "capo_iotfleetwise.types.custom_property.CustomProperty"


Node: TypeAlias = (
    NodeBranchMember
    | NodeSensorMember
    | NodeActuatorMember
    | NodeAttributeMember
    | NodeStructMember
    | NodePropertyMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Node) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Node: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "branch" in value:
        import capo_iotfleetwise.types.branch

        return {
            "branch": capo_iotfleetwise.types.branch.serialize_aws_json_1_0(
                value["branch"]
            )
        }
    elif "sensor" in value:
        import capo_iotfleetwise.types.sensor

        return {
            "sensor": capo_iotfleetwise.types.sensor.serialize_aws_json_1_0(
                value["sensor"]
            )
        }
    elif "actuator" in value:
        import capo_iotfleetwise.types.actuator

        return {
            "actuator": capo_iotfleetwise.types.actuator.serialize_aws_json_1_0(
                value["actuator"]
            )
        }
    elif "attribute" in value:
        import capo_iotfleetwise.types.attribute

        return {
            "attribute": capo_iotfleetwise.types.attribute.serialize_aws_json_1_0(
                value["attribute"]
            )
        }
    elif "struct" in value:
        import capo_iotfleetwise.types.custom_struct

        return {
            "struct": capo_iotfleetwise.types.custom_struct.serialize_aws_json_1_0(
                value["struct"]
            )
        }
    elif "property" in value:
        import capo_iotfleetwise.types.custom_property

        return {
            "property": capo_iotfleetwise.types.custom_property.serialize_aws_json_1_0(
                value["property"]
            )
        }
    else:
        raise SerializationError("Node: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Node:
    if data.get("branch") is not None:
        import capo_iotfleetwise.types.branch

        return {
            "branch": capo_iotfleetwise.types.branch.deserialize_aws_json_1_0(
                data["branch"]
            )
        }
    elif data.get("sensor") is not None:
        import capo_iotfleetwise.types.sensor

        return {
            "sensor": capo_iotfleetwise.types.sensor.deserialize_aws_json_1_0(
                data["sensor"]
            )
        }
    elif data.get("actuator") is not None:
        import capo_iotfleetwise.types.actuator

        return {
            "actuator": capo_iotfleetwise.types.actuator.deserialize_aws_json_1_0(
                data["actuator"]
            )
        }
    elif data.get("attribute") is not None:
        import capo_iotfleetwise.types.attribute

        return {
            "attribute": capo_iotfleetwise.types.attribute.deserialize_aws_json_1_0(
                data["attribute"]
            )
        }
    elif data.get("struct") is not None:
        import capo_iotfleetwise.types.custom_struct

        return {
            "struct": capo_iotfleetwise.types.custom_struct.deserialize_aws_json_1_0(
                data["struct"]
            )
        }
    elif data.get("property") is not None:
        import capo_iotfleetwise.types.custom_property

        return {
            "property": capo_iotfleetwise.types.custom_property.deserialize_aws_json_1_0(
                data["property"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Node: no recognized variant key")
