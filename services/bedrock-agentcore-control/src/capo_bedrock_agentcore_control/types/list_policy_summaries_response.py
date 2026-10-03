"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicySummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.policy_summary_list


class ListPolicySummariesResponse(TypedDict, closed=True):
    policies: (
        "capo_bedrock_agentcore_control.types.policy_summary_list.PolicySummaryList"
    )
    """<p>An array of policy summary objects that match the specified criteria. Each summary contains resource identifiers, status, and timestamps without customer-encrypted content.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token that can be used in subsequent <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicySummaries.html">ListPolicySummaries</a> calls to retrieve additional results. This token is only present when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicySummariesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.policy_summary_list

    out["policies"] = (
        capo_bedrock_agentcore_control.types.policy_summary_list.serialize_json(
            value["policies"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicySummariesResponse:
    out: ListPolicySummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("policies") is not None:
        import capo_bedrock_agentcore_control.types.policy_summary_list

        out["policies"] = (
            capo_bedrock_agentcore_control.types.policy_summary_list.deserialize_json(
                data["policies"]
            )
        )
    else:
        raise DeserializationError("ListPolicySummariesResponse.policies required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
