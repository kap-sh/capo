"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightSampleSessionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sample_session

InsightSampleSessionList: TypeAlias = list[
    "capo_bedrock_agentcore.types.sample_session.SampleSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightSampleSessionList) -> list:
    import capo_bedrock_agentcore.types.sample_session

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.sample_session.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightSampleSessionList:
    import capo_bedrock_agentcore.types.sample_session

    out: InsightSampleSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.sample_session.deserialize_json(item))
    return out


def redact_sensitive(value: InsightSampleSessionList) -> list[Any]:
    import capo_bedrock_agentcore.types.sample_session

    return [
        capo_bedrock_agentcore.types.sample_session.redact_sensitive(item)
        for item in value
    ]
