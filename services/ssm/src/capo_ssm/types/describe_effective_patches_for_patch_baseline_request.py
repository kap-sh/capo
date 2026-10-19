"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeEffectivePatchesForPatchBaselineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_id
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_baseline_max_results


class DescribeEffectivePatchesForPatchBaselineRequest(TypedDict, closed=True):
    baseline_id: "capo_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline to retrieve the effective patches for.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
    ]
    """<p>The maximum number of patches to return (per page).</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeEffectivePatchesForPatchBaselineRequest,
) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEffectivePatchesForPatchBaselineRequest:
    out: DescribeEffectivePatchesForPatchBaselineRequest = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    else:
        out["baseline_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
