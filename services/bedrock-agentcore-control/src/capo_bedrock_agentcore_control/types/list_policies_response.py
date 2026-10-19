"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPoliciesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.policies


class ListPoliciesResponse(TypedDict, closed=True):
    policies: "capo_bedrock_agentcore_control.types.policies.Policies"
    """<p>An array of policy objects that match the specified criteria. Each policy object contains the policy metadata, status, and key identifiers for further operations.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token that can be used in subsequent ListPolicies calls to retrieve additional results. This token is only present when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.policies

    out["policies"] = capo_bedrock_agentcore_control.types.policies.serialize_json(
        value["policies"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPoliciesResponse:
    out: ListPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("policies") is not None:
        import capo_bedrock_agentcore_control.types.policies

        out["policies"] = (
            capo_bedrock_agentcore_control.types.policies.deserialize_json(
                data["policies"]
            )
        )
    else:
        out["policies"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListPoliciesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policies" in value:
        import capo_bedrock_agentcore_control.types.policies

        out["policies"] = (
            capo_bedrock_agentcore_control.types.policies.redact_sensitive(
                value["policies"]
            )
        )
    return out
