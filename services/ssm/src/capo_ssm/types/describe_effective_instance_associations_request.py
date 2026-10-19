"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeEffectiveInstanceAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.effective_instance_association_max_results
    import capo_ssm.types.instance_id
    import capo_ssm.types.next_token


class DescribeEffectiveInstanceAssociationsRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.instance_id.InstanceId"
    """<p>The managed node ID for which you want to view all associations.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.effective_instance_association_max_results.EffectiveInstanceAssociationMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEffectiveInstanceAssociationsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEffectiveInstanceAssociationsRequest:
    out: DescribeEffectiveInstanceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
