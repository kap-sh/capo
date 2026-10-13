"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessages``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_message

HarnessMessages: TypeAlias = list[
    "capo_bedrock_agentcore.types.harness_message.HarnessMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessages) -> list:
    import capo_bedrock_agentcore.types.harness_message

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.harness_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> HarnessMessages:
    import capo_bedrock_agentcore.types.harness_message

    out: HarnessMessages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.harness_message.deserialize_json(item))
    return out


def redact_sensitive(value: HarnessMessages) -> list[Any]:
    import capo_bedrock_agentcore.types.harness_message

    return [
        capo_bedrock_agentcore.types.harness_message.redact_sensitive(item)
        for item in value
    ]
