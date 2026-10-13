"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetExampleList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.sensitive_json

DatasetExampleList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.sensitive_json.SensitiveJson"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetExampleList) -> list:
    return list(value)


def deserialize_json(data: list) -> DatasetExampleList:
    return [item for item in data if item is not None]


def redact_sensitive(value: DatasetExampleList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
