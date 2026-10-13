"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.linked_account

LinkedAccountList: TypeAlias = list[
    "capo_bedrock_agentcore.types.linked_account.LinkedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountList) -> list:
    import capo_bedrock_agentcore.types.linked_account

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.linked_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkedAccountList:
    import capo_bedrock_agentcore.types.linked_account

    out: LinkedAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.linked_account.deserialize_json(item))
    return out


def redact_sensitive(value: LinkedAccountList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
