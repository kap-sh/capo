"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insight_result

InsightResultList: TypeAlias = list[
    "capo_bedrock_agentcore.types.insight_result.InsightResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightResultList) -> list:
    import capo_bedrock_agentcore.types.insight_result

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.insight_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightResultList:
    import capo_bedrock_agentcore.types.insight_result

    out: InsightResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.insight_result.deserialize_json(item))
    return out


def redact_sensitive(value: InsightResultList) -> list[Any]:
    import capo_bedrock_agentcore.types.insight_result

    return [
        capo_bedrock_agentcore.types.insight_result.redact_sensitive(item)
        for item in value
    ]
