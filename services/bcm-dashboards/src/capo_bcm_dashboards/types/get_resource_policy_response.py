"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn
    import capo_bcm_dashboards.types.generic_string


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard for which the resource-based policy was retrieved.</p>"""
    policy_document: "capo_bcm_dashboards.types.generic_string.GenericString"
    """<p>The JSON policy document that represents the dashboard's resource-based policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = ""
    return out
