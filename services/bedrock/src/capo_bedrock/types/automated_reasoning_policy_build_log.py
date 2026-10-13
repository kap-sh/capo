"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildLog``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_log_entry_list


class AutomatedReasoningPolicyBuildLog(TypedDict, closed=True):
    entries: "capo_bedrock.types.automated_reasoning_policy_build_log_entry_list.AutomatedReasoningPolicyBuildLogEntryList"
    """<p>A list of log entries documenting each step in the policy build process, including timestamps, status, and detailed messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildLog) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_log_entry_list

    out["entries"] = (
        capo_bedrock.types.automated_reasoning_policy_build_log_entry_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildLog:
    out: AutomatedReasoningPolicyBuildLog = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_log_entry_list

        out["entries"] = (
            capo_bedrock.types.automated_reasoning_policy_build_log_entry_list.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("AutomatedReasoningPolicyBuildLog.entries required")
    return out


def redact_sensitive(value: AutomatedReasoningPolicyBuildLog) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_log_entry_list

        out["entries"] = (
            capo_bedrock.types.automated_reasoning_policy_build_log_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out
