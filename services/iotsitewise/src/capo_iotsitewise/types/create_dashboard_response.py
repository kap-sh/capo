"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.id


class CreateDashboardResponse(TypedDict, closed=True):
    dashboard_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard.</p>"""
    dashboard_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the dashboard, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDashboardResponse) -> dict:
    out: dict = {}
    out["dashboardId"] = value["dashboard_id"]
    out["dashboardArn"] = value["dashboard_arn"]
    return out


def deserialize_json(data: dict) -> CreateDashboardResponse:
    out: CreateDashboardResponse = {}  # type: ignore[typeddict-item]
    if data.get("dashboardId") is not None:
        out["dashboard_id"] = data["dashboardId"]
    else:
        raise DeserializationError("CreateDashboardResponse.dashboard_id required")
    if data.get("dashboardArn") is not None:
        out["dashboard_arn"] = data["dashboardArn"]
    else:
        raise DeserializationError("CreateDashboardResponse.dashboard_arn required")
    return out
