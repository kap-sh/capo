"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DashboardReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn
    import capo_bcm_dashboards.types.dashboard_name
    import capo_bcm_dashboards.types.dashboard_type
    import capo_bcm_dashboards.types.description
    import capo_bcm_dashboards.types.generic_time_stamp


class DashboardReference(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the referenced dashboard.</p>"""
    name: "capo_bcm_dashboards.types.dashboard_name.DashboardName"
    """<p>The name of the referenced dashboard.</p>"""
    description: NotRequired["capo_bcm_dashboards.types.description.Description"]
    """<p>The description of the referenced dashboard.</p>"""
    type: "capo_bcm_dashboards.types.dashboard_type.DashboardType"
    """<p>The dashboard type.</p>"""
    created_at: "capo_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    """<p>The timestamp when the dashboard was created.</p>"""
    updated_at: "capo_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    """<p>The timestamp when the dashboard was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardReference) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bcm_dashboards.types.dashboard_type

    out["type"] = capo_bcm_dashboards.types.dashboard_type.serialize_aws_json_1_0(
        value["type"]
    )
    import capo_bcm_dashboards.types.generic_time_stamp

    out["createdAt"] = (
        capo_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import capo_bcm_dashboards.types.generic_time_stamp

    out["updatedAt"] = (
        capo_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardReference:
    out: DashboardReference = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_bcm_dashboards.types.dashboard_type

        out["type"] = capo_bcm_dashboards.types.dashboard_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bcm_dashboards.types.dashboard_type.DashboardType", ""
        )
    if data.get("createdAt") is not None:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["created_at"] = (
            capo_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["updated_at"] = (
            capo_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
