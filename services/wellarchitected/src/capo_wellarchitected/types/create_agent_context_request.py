"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentContextRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.context_content
    import capo_wellarchitected.types.context_type
    import capo_wellarchitected.types.sensitive_string


class CreateAgentContextRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile to associate the context with.</p>"""
    title: "capo_wellarchitected.types.sensitive_string.SensitiveString"
    """<p>The title of the context.</p>"""
    context_type: "capo_wellarchitected.types.context_type.ContextType"
    """<p>The type of the context.</p>"""
    content: "capo_wellarchitected.types.context_content.ContextContent"
    """<p>The typed content of the context. The structure contains application-specific fields such as account IDs, Regions, services, and resource types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentContextRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["title"] = value["title"]
    import capo_wellarchitected.types.context_type

    out["contextType"] = capo_wellarchitected.types.context_type.serialize_json(
        value["context_type"]
    )
    import capo_wellarchitected.types.context_content

    out["content"] = capo_wellarchitected.types.context_content.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> CreateAgentContextRequest:
    out: CreateAgentContextRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateAgentContextRequest.title required")
    if data.get("contextType") is not None:
        import capo_wellarchitected.types.context_type

        out["context_type"] = capo_wellarchitected.types.context_type.deserialize_json(
            data["contextType"]
        )
    else:
        raise DeserializationError("CreateAgentContextRequest.context_type required")
    if data.get("content") is not None:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("CreateAgentContextRequest.content required")
    return out


def redact_sensitive(value: CreateAgentContextRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "content" in value:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.redact_sensitive(
            value["content"]
        )
    return out
