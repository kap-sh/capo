"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#SatisfiedConditions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.satisfied_condition

SatisfiedConditions: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.satisfied_condition.SatisfiedCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: SatisfiedConditions) -> list:
    import capo_bedrock_agent_runtime.types.satisfied_condition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.satisfied_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SatisfiedConditions:
    import capo_bedrock_agent_runtime.types.satisfied_condition

    out: SatisfiedConditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.satisfied_condition.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SatisfiedConditions) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
