"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAgentContextRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.context_content
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.uuid


class UpdateAgentContextRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile containing the context.</p>"""
    id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the context to update.</p>"""
    title: NotRequired["capo_wellarchitected.types.sensitive_string.SensitiveString"]
    """<p>The updated title of the context.</p>"""
    content: NotRequired["capo_wellarchitected.types.context_content.ContextContent"]
    """<p>The updated typed content of the context. The structure contains application-specific fields such as account IDs, Regions, services, and resource types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentContextRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "title" in value:
        out["title"] = value["title"]
    if "content" in value:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentContextRequest:
    out: UpdateAgentContextRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("content") is not None:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.deserialize_json(
            data["content"]
        )
    return out


def redact_sensitive(value: UpdateAgentContextRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "content" in value:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.redact_sensitive(
            value["content"]
        )
    return out
