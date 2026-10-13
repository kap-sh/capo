"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildLogEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_log_entry

AutomatedReasoningPolicyBuildLogEntryList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_build_log_entry.AutomatedReasoningPolicyBuildLogEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildLogEntryList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_build_log_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_log_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildLogEntryList:
    import capo_bedrock.types.automated_reasoning_policy_build_log_entry

    out: AutomatedReasoningPolicyBuildLogEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_log_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyBuildLogEntryList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_build_log_entry

    return [
        capo_bedrock.types.automated_reasoning_policy_build_log_entry.redact_sensitive(
            item
        )
        for item in value
    ]
