"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_arn


class DeleteDashboardRequest(TypedDict, closed=True):
    dashboard_id: "capo_cloudtrail.types.dashboard_arn.DashboardArn"
    """<p> The name or ARN for the dashboard. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDashboardRequest) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDashboardRequest:
    out: DeleteDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    else:
        out["dashboard_id"] = ""
    return out
