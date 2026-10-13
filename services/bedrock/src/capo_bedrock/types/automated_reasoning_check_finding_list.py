"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckFindingList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_finding

AutomatedReasoningCheckFindingList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_check_finding.AutomatedReasoningCheckFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckFindingList) -> list:
    import capo_bedrock.types.automated_reasoning_check_finding

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_check_finding.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckFindingList:
    import capo_bedrock.types.automated_reasoning_check_finding

    out: AutomatedReasoningCheckFindingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_check_finding.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckFindingList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_check_finding

    return [
        capo_bedrock.types.automated_reasoning_check_finding.redact_sensitive(item)
        for item in value
    ]
