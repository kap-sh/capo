"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePatchStatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_id_list
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_compliance_max_results


class DescribeInstancePatchStatesRequest(TypedDict, closed=True):
    instance_ids: "capo_ssm.types.instance_id_list.InstanceIdList"
    """<p>The ID of the managed node for which patch state information should be retrieved.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
    ]
    """<p>The maximum number of managed nodes to return (per page).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePatchStatesRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.instance_id_list

    out["InstanceIds"] = capo_ssm.types.instance_id_list.serialize_aws_json_1_1(
        value["instance_ids"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePatchStatesRequest:
    out: DescribeInstancePatchStatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceIds") is not None:
        import capo_ssm.types.instance_id_list

        out["instance_ids"] = capo_ssm.types.instance_id_list.deserialize_aws_json_1_1(
            data["InstanceIds"]
        )
    else:
        out["instance_ids"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
