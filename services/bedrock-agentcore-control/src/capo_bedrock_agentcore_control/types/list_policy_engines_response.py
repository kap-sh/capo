"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyEnginesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.policy_engines


class ListPolicyEnginesResponse(TypedDict, closed=True):
    policy_engines: "capo_bedrock_agentcore_control.types.policy_engines.PolicyEngines"
    """<p>An array of policy engine objects that exist in the account. Each policy engine object contains the engine metadata, status, and key identifiers for further operations.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token that can be used in subsequent <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngines.html">ListPolicyEngines</a> calls to retrieve additional results. This token is only present when there are more results available. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyEnginesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.policy_engines

    out["policyEngines"] = (
        capo_bedrock_agentcore_control.types.policy_engines.serialize_json(
            value["policy_engines"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyEnginesResponse:
    out: ListPolicyEnginesResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyEngines") is not None:
        import capo_bedrock_agentcore_control.types.policy_engines

        out["policy_engines"] = (
            capo_bedrock_agentcore_control.types.policy_engines.deserialize_json(
                data["policyEngines"]
            )
        )
    else:
        raise DeserializationError("ListPolicyEnginesResponse.policy_engines required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
