"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAgentGoalRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.uuid


class UpdateAgentGoalRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile containing the goal to update.</p>"""
    id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the goal to update.</p>"""
    pillars: NotRequired["capo_wellarchitected.types.pillars.Pillars"]
    """<p>The updated pillars for the goal. Pillars define the optimization focus areas such as cost, performance, resilience, and operational excellence.</p>"""
    title: NotRequired["capo_wellarchitected.types.sensitive_string.SensitiveString"]
    """<p>The updated title for the goal. Maximum length of 1000 characters.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A description of the goal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentGoalRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "pillars" in value:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.serialize_json(
            value["pillars"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAgentGoalRequest:
    out: UpdateAgentGoalRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("pillars") is not None:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.deserialize_json(
            data["pillars"]
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: UpdateAgentGoalRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
