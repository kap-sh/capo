"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn


class GetResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard whose resource-based policy you want to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyRequest:
    out: GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
