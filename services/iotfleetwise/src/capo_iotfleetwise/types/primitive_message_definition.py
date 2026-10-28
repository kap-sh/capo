"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PrimitiveMessageDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.ros2_primitive_message_definition


class PrimitiveMessageDefinitionRos2PrimitiveMessageDefinitionMember(
    TypedDict, closed=True
):
    ros2PrimitiveMessageDefinition: "capo_iotfleetwise.types.ros2_primitive_message_definition.ROS2PrimitiveMessageDefinition"


PrimitiveMessageDefinition: TypeAlias = (
    PrimitiveMessageDefinitionRos2PrimitiveMessageDefinitionMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrimitiveMessageDefinition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrimitiveMessageDefinition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ros2PrimitiveMessageDefinition" in value:
        import capo_iotfleetwise.types.ros2_primitive_message_definition

        return {
            "ros2PrimitiveMessageDefinition": capo_iotfleetwise.types.ros2_primitive_message_definition.serialize_aws_json_1_0(
                value["ros2PrimitiveMessageDefinition"]
            )
        }
    else:
        raise SerializationError("PrimitiveMessageDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PrimitiveMessageDefinition:
    if data.get("ros2PrimitiveMessageDefinition") is not None:
        import capo_iotfleetwise.types.ros2_primitive_message_definition

        return {
            "ros2PrimitiveMessageDefinition": capo_iotfleetwise.types.ros2_primitive_message_definition.deserialize_aws_json_1_0(
                data["ros2PrimitiveMessageDefinition"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PrimitiveMessageDefinition: no recognized variant key"
        )
