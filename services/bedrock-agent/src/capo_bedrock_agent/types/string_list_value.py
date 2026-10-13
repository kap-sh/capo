"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StringListValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.string_value

StringListValue: TypeAlias = list["capo_bedrock_agent.types.string_value.StringValue"]


# --- restJson1 ser/de ---
def serialize_json(value: StringListValue) -> list:
    return list(value)


def deserialize_json(data: list) -> StringListValue:
    return [item for item in data if item is not None]


def redact_sensitive(value: StringListValue) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
