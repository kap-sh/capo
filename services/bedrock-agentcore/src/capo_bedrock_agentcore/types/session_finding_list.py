"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionFindingList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_finding

SessionFindingList: TypeAlias = list[
    "capo_bedrock_agentcore.types.session_finding.SessionFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionFindingList) -> list:
    import capo_bedrock_agentcore.types.session_finding

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.session_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionFindingList:
    import capo_bedrock_agentcore.types.session_finding

    out: SessionFindingList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.session_finding.deserialize_json(item))
    return out


def redact_sensitive(value: SessionFindingList) -> list[Any]:
    import capo_bedrock_agentcore.types.session_finding

    return [
        capo_bedrock_agentcore.types.session_finding.redact_sensitive(item)
        for item in value
    ]
