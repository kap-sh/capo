"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightRootCauseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insight_root_cause

InsightRootCauseList: TypeAlias = list[
    "capo_bedrock_agentcore.types.insight_root_cause.InsightRootCause"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightRootCauseList) -> list:
    import capo_bedrock_agentcore.types.insight_root_cause

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.insight_root_cause.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightRootCauseList:
    import capo_bedrock_agentcore.types.insight_root_cause

    out: InsightRootCauseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.insight_root_cause.deserialize_json(item)
        )
    return out


def redact_sensitive(value: InsightRootCauseList) -> list[Any]:
    import capo_bedrock_agentcore.types.insight_root_cause

    return [
        capo_bedrock_agentcore.types.insight_root_cause.redact_sensitive(item)
        for item in value
    ]
