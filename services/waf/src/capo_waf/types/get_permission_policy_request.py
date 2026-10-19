"""Generated from Smithy shape ``com.amazonaws.waf#GetPermissionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf.types.resource_arn


class GetPermissionPolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_waf.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the RuleGroup for which you want to get the policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPermissionPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPermissionPolicyRequest:
    out: GetPermissionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
