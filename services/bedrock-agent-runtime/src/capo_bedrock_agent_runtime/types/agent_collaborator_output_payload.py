"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboratorOutputPayload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_collaborator_payload_string
    import capo_bedrock_agent_runtime.types.payload_type
    import capo_bedrock_agent_runtime.types.return_control_payload


class AgentCollaboratorOutputPayload(TypedDict, closed=True):
    type: NotRequired["capo_bedrock_agent_runtime.types.payload_type.PayloadType"]
    """<p>The type of output.</p>"""
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_collaborator_payload_string.AgentCollaboratorPayloadString"
    ]
    """<p>Text output.</p>"""
    return_control_payload: NotRequired[
        "capo_bedrock_agent_runtime.types.return_control_payload.ReturnControlPayload"
    ]
    """<p>An action invocation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorOutputPayload) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_bedrock_agent_runtime.types.payload_type

        out["type"] = capo_bedrock_agent_runtime.types.payload_type.serialize_json(
            value["type"]
        )
    if "text" in value:
        out["text"] = value["text"]
    if "return_control_payload" in value:
        import capo_bedrock_agent_runtime.types.return_control_payload

        out["returnControlPayload"] = (
            capo_bedrock_agent_runtime.types.return_control_payload.serialize_json(
                value["return_control_payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorOutputPayload:
    out: AgentCollaboratorOutputPayload = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.payload_type

        out["type"] = capo_bedrock_agent_runtime.types.payload_type.deserialize_json(
            data["type"]
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("returnControlPayload") is not None:
        import capo_bedrock_agent_runtime.types.return_control_payload

        out["return_control_payload"] = (
            capo_bedrock_agent_runtime.types.return_control_payload.deserialize_json(
                data["returnControlPayload"]
            )
        )
    return out


def redact_sensitive(value: AgentCollaboratorOutputPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "return_control_payload" in value:
        out["return_control_payload"] = "*** Sensitive Data Redacted ***"
    return out
