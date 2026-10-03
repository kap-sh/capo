"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDashboardResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.dashboard_definition
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp


class DescribeDashboardResponse(TypedDict, closed=True):
    dashboard_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard.</p>"""
    dashboard_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the dashboard, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}</code> </p>"""
    dashboard_name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the dashboard.</p>"""
    project_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the project that the dashboard is in.</p>"""
    dashboard_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The dashboard's description.</p>"""
    dashboard_definition: (
        "capo_iotsitewise.types.dashboard_definition.DashboardDefinition"
    )
    """<p>The dashboard's definition JSON literal. For detailed information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html">Creating dashboards (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    dashboard_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dashboard was created, in Unix epoch time.</p>"""
    dashboard_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dashboard was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardResponse) -> dict:
    out: dict = {}
    out["dashboardId"] = value["dashboard_id"]
    out["dashboardArn"] = value["dashboard_arn"]
    out["dashboardName"] = value["dashboard_name"]
    out["projectId"] = value["project_id"]
    if "dashboard_description" in value:
        out["dashboardDescription"] = value["dashboard_description"]
    out["dashboardDefinition"] = value["dashboard_definition"]
    import capo_iotsitewise.types.timestamp

    out["dashboardCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["dashboard_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["dashboardLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["dashboard_last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDashboardResponse:
    out: DescribeDashboardResponse = {}  # type: ignore[typeddict-item]
    if data.get("dashboardId") is not None:
        out["dashboard_id"] = data["dashboardId"]
    else:
        raise DeserializationError("DescribeDashboardResponse.dashboard_id required")
    if data.get("dashboardArn") is not None:
        out["dashboard_arn"] = data["dashboardArn"]
    else:
        raise DeserializationError("DescribeDashboardResponse.dashboard_arn required")
    if data.get("dashboardName") is not None:
        out["dashboard_name"] = data["dashboardName"]
    else:
        raise DeserializationError("DescribeDashboardResponse.dashboard_name required")
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DescribeDashboardResponse.project_id required")
    if data.get("dashboardDescription") is not None:
        out["dashboard_description"] = data["dashboardDescription"]
    if data.get("dashboardDefinition") is not None:
        out["dashboard_definition"] = data["dashboardDefinition"]
    else:
        raise DeserializationError(
            "DescribeDashboardResponse.dashboard_definition required"
        )
    if data.get("dashboardCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["dashboard_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["dashboardCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDashboardResponse.dashboard_creation_date required"
        )
    if data.get("dashboardLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["dashboard_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["dashboardLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDashboardResponse.dashboard_last_update_date required"
        )
    return out
