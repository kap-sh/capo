"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.policy_generation_summary_list


class ListPolicyGenerationSummariesResponse(TypedDict, closed=True):
    policy_generations: "capo_bedrock_agentcore_control.types.policy_generation_summary_list.PolicyGenerationSummaryList"
    """<p>An array of policy generation summary objects that match the specified criteria. Each summary contains resource identifiers, status, timestamps, and findings without customer-encrypted content.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token that can be used in subsequent <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationSummaries.html">ListPolicyGenerationSummaries</a> calls to retrieve additional results. This token is only present when there are more results available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationSummariesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.policy_generation_summary_list

    out["policyGenerations"] = (
        capo_bedrock_agentcore_control.types.policy_generation_summary_list.serialize_json(
            value["policy_generations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationSummariesResponse:
    out: ListPolicyGenerationSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyGenerations") is not None:
        import capo_bedrock_agentcore_control.types.policy_generation_summary_list

        out["policy_generations"] = (
            capo_bedrock_agentcore_control.types.policy_generation_summary_list.deserialize_json(
                data["policyGenerations"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyGenerationSummariesResponse.policy_generations required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
