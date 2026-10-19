"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StructuredMessage``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.primitive_message_definition
    import capo_iotfleetwise.types.structured_message_definition
    import capo_iotfleetwise.types.structured_message_list_definition


class _StructuredMessage_primitiveMessageDefinition(TypedDict, closed=True):
    primitiveMessageDefinition: "capo_iotfleetwise.types.primitive_message_definition.PrimitiveMessageDefinition"


class _StructuredMessage_structuredMessageListDefinition(TypedDict, closed=True):
    structuredMessageListDefinition: "capo_iotfleetwise.types.structured_message_list_definition.StructuredMessageListDefinition"


class _StructuredMessage_structuredMessageDefinition(TypedDict, closed=True):
    structuredMessageDefinition: "capo_iotfleetwise.types.structured_message_definition.StructuredMessageDefinition"


StructuredMessage: TypeAlias = (
    _StructuredMessage_primitiveMessageDefinition
    | _StructuredMessage_structuredMessageListDefinition
    | _StructuredMessage_structuredMessageDefinition
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StructuredMessage) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"StructuredMessage: cannot serialize unknown variant {value.name!r}"
        )
    elif "primitiveMessageDefinition" in value:
        import capo_iotfleetwise.types.primitive_message_definition

        return {
            "primitiveMessageDefinition": capo_iotfleetwise.types.primitive_message_definition.serialize_aws_json_1_0(
                value["primitiveMessageDefinition"]
            )
        }
    elif "structuredMessageListDefinition" in value:
        import capo_iotfleetwise.types.structured_message_list_definition

        return {
            "structuredMessageListDefinition": capo_iotfleetwise.types.structured_message_list_definition.serialize_aws_json_1_0(
                value["structuredMessageListDefinition"]
            )
        }
    elif "structuredMessageDefinition" in value:
        import capo_iotfleetwise.types.structured_message_definition

        return {
            "structuredMessageDefinition": capo_iotfleetwise.types.structured_message_definition.serialize_aws_json_1_0(
                value["structuredMessageDefinition"]
            )
        }
    else:
        raise SerializationError("StructuredMessage: no variant present")


def deserialize_aws_json_1_0(data: dict) -> StructuredMessage:
    if data.get("primitiveMessageDefinition") is not None:
        import capo_iotfleetwise.types.primitive_message_definition

        return {
            "primitiveMessageDefinition": capo_iotfleetwise.types.primitive_message_definition.deserialize_aws_json_1_0(
                data["primitiveMessageDefinition"]
            )
        }
    elif data.get("structuredMessageListDefinition") is not None:
        import capo_iotfleetwise.types.structured_message_list_definition

        return {
            "structuredMessageListDefinition": capo_iotfleetwise.types.structured_message_list_definition.deserialize_aws_json_1_0(
                data["structuredMessageListDefinition"]
            )
        }
    elif data.get("structuredMessageDefinition") is not None:
        import capo_iotfleetwise.types.structured_message_definition

        return {
            "structuredMessageDefinition": capo_iotfleetwise.types.structured_message_definition.deserialize_aws_json_1_0(
                data["structuredMessageDefinition"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("StructuredMessage: no recognized variant key")
