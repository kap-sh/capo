"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_value


class AgenticRetrieveMemoryMetadataValueStringValueMember(TypedDict, closed=True):
    stringValue: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_value.AgenticRetrieveMemoryMetadataStringValue"


class AgenticRetrieveMemoryMetadataValueNumberValueMember(TypedDict, closed=True):
    numberValue: "float"


class AgenticRetrieveMemoryMetadataValueStringListValueMember(TypedDict, closed=True):
    stringListValue: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list.AgenticRetrieveMemoryMetadataStringList"


class AgenticRetrieveMemoryMetadataValueDateTimeValueMember(TypedDict, closed=True):
    dateTimeValue: "datetime.datetime"


AgenticRetrieveMemoryMetadataValue: TypeAlias = (
    AgenticRetrieveMemoryMetadataValueStringValueMember
    | AgenticRetrieveMemoryMetadataValueNumberValueMember
    | AgenticRetrieveMemoryMetadataValueStringListValueMember
    | AgenticRetrieveMemoryMetadataValueDateTimeValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgenticRetrieveMemoryMetadataValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
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
    elif "stringListValue" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list

        return {
            "stringListValue": capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list.serialize_json(
                value["stringListValue"]
            )
        }
    elif "dateTimeValue" in value:
        import capo_bedrock_agent_runtime.types._prelude.timestamp

        return {
            "dateTimeValue": capo_bedrock_agent_runtime.types._prelude.timestamp.serialize_json(
                value["dateTimeValue"]
            )
        }
    else:
        raise SerializationError(
            "AgenticRetrieveMemoryMetadataValue: no variant present"
        )


def deserialize_json(data: dict) -> AgenticRetrieveMemoryMetadataValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("numberValue") is not None:
        return {"numberValue": float(data["numberValue"])}
    elif data.get("stringListValue") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list

        return {
            "stringListValue": capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_string_list.deserialize_json(
                data["stringListValue"]
            )
        }
    elif data.get("dateTimeValue") is not None:
        import capo_bedrock_agent_runtime.types._prelude.timestamp

        return {
            "dateTimeValue": capo_bedrock_agent_runtime.types._prelude.timestamp.deserialize_json(
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
            "AgenticRetrieveMemoryMetadataValue: no recognized variant key"
        )
