"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyJustificationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_justification_text

AutomatedReasoningPolicyJustificationList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_justification_text.AutomatedReasoningPolicyJustificationText"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyJustificationList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutomatedReasoningPolicyJustificationList:
    return [item for item in data if item is not None]


def redact_sensitive(value: AutomatedReasoningPolicyJustificationList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
