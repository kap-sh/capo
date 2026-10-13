"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupInvocationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.action_group_output_string
    import capo_bedrock_agent_runtime.types.metadata


class ActionGroupInvocationOutput(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.action_group_output_string.ActionGroupOutputString"
    ]
    """<p>The JSON-formatted string returned by the API invoked by the action group.</p>"""
    metadata: NotRequired["capo_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the action group output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupInvocationOutput) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> ActionGroupInvocationOutput:
    out: ActionGroupInvocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out


def redact_sensitive(value: ActionGroupInvocationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
