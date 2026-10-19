"""Generated from Smithy shape ``com.amazonaws.ssm#GetResourcePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.resource_arn_string
    import capo_ssm.types.resource_policy_max_results
    import capo_ssm.types.string


class GetResourcePoliciesRequest(TypedDict, closed=True):
    resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString"
    """<p>Amazon Resource Name (ARN) of the resource to which the policies are attached.</p>"""
    next_token: NotRequired["capo_ssm.types.string.String"]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.resource_policy_max_results.ResourcePolicyMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePoliciesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePoliciesRequest:
    out: GetResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
