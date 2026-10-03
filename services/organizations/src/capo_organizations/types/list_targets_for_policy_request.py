"""Generated from Smithy shape ``com.amazonaws.organizations#ListTargetsForPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.max_results
    import capo_organizations.types.next_token
    import capo_organizations.types.policy_id


class ListTargetsForPolicyRequest(TypedDict, closed=True):
    policy_id: "capo_organizations.types.policy_id.PolicyId"
    """<p>ID for the policy whose attachments you want to know.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for a policy ID string requires "p-" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""
    next_token: NotRequired["capo_organizations.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""
    max_results: NotRequired["capo_organizations.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetsForPolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetsForPolicyRequest:
    out: ListTargetsForPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("ListTargetsForPolicyRequest.policy_id required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
