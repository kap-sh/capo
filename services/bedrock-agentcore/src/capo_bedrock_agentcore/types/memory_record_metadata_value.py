"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordMetadataValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.string_value
    import capo_bedrock_agentcore.types.string_value_list


class MemoryRecordMetadataValueStringValueMember(TypedDict, closed=True):
    stringValue: "capo_bedrock_agentcore.types.string_value.StringValue"


class MemoryRecordMetadataValueStringListValueMember(TypedDict, closed=True):
    stringListValue: "capo_bedrock_agentcore.types.string_value_list.StringValueList"


class MemoryRecordMetadataValueNumberValueMember(TypedDict, closed=True):
    numberValue: "float"


class MemoryRecordMetadataValueDateTimeValueMember(TypedDict, closed=True):
    dateTimeValue: "datetime.datetime"


MemoryRecordMetadataValue: TypeAlias = (
    MemoryRecordMetadataValueStringValueMember
    | MemoryRecordMetadataValueStringListValueMember
    | MemoryRecordMetadataValueNumberValueMember
    | MemoryRecordMetadataValueDateTimeValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordMetadataValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MemoryRecordMetadataValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "stringListValue" in value:
        import capo_bedrock_agentcore.types.string_value_list

        return {
            "stringListValue": capo_bedrock_agentcore.types.string_value_list.serialize_json(
                value["stringListValue"]
            )
        }
    elif "numberValue" in value:
        return {
            "numberValue": (
                "NaN"
                if value["numberValue"] != value["numberValue"]
                else "Infinity"
                if value["numberValue"] == float("inf")
                else "-Infinity"
                if value["numberValue"] == float("-inf")
                else value["numberValue"]
            )
        }
    elif "dateTimeValue" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        return {
            "dateTimeValue": capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["dateTimeValue"]
            )
        }
    else:
        raise SerializationError("MemoryRecordMetadataValue: no variant present")


def deserialize_json(data: dict) -> MemoryRecordMetadataValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("stringListValue") is not None:
        import capo_bedrock_agentcore.types.string_value_list

        return {
            "stringListValue": capo_bedrock_agentcore.types.string_value_list.deserialize_json(
                data["stringListValue"]
            )
        }
    elif data.get("numberValue") is not None:
        return {"numberValue": float(data["numberValue"])}
    elif data.get("dateTimeValue") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        return {
            "dateTimeValue": capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["dateTimeValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MemoryRecordMetadataValue: no recognized variant key"
        )
