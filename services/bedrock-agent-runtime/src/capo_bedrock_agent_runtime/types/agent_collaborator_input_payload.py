"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorInputPayload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_collaborator_payload_string
    import capo_bedrock_agent_runtime.types.payload_type
    import capo_bedrock_agent_runtime.types.return_control_results


class AgentCollaboratorInputPayload(TypedDict, closed=True):
    type: NotRequired["capo_bedrock_agent_runtime.types.payload_type.PayloadType"]
    """<p>The input type.</p>"""
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_collaborator_payload_string.AgentCollaboratorPayloadString"
    ]
    """<p>Input text.</p>"""
    return_control_results: NotRequired[
        "capo_bedrock_agent_runtime.types.return_control_results.ReturnControlResults"
    ]
    """<p>An action invocation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorInputPayload) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_bedrock_agent_runtime.types.payload_type

        out["type"] = capo_bedrock_agent_runtime.types.payload_type.serialize_json(
            value["type"]
        )
    if "text" in value:
        out["text"] = value["text"]
    if "return_control_results" in value:
        import capo_bedrock_agent_runtime.types.return_control_results

        out["returnControlResults"] = (
            capo_bedrock_agent_runtime.types.return_control_results.serialize_json(
                value["return_control_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorInputPayload:
    out: AgentCollaboratorInputPayload = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.payload_type

        out["type"] = capo_bedrock_agent_runtime.types.payload_type.deserialize_json(
            data["type"]
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("returnControlResults") is not None:
        import capo_bedrock_agent_runtime.types.return_control_results

        out["return_control_results"] = (
            capo_bedrock_agent_runtime.types.return_control_results.deserialize_json(
                data["returnControlResults"]
            )
        )
    return out


def redact_sensitive(value: AgentCollaboratorInputPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "return_control_results" in value:
        import capo_bedrock_agent_runtime.types.return_control_results

        out["return_control_results"] = (
            capo_bedrock_agent_runtime.types.return_control_results.redact_sensitive(
                value["return_control_results"]
            )
        )
    return out
