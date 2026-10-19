"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_name
    import capo_cloudtrail.types.refresh_schedule
    import capo_cloudtrail.types.request_widget_list
    import capo_cloudtrail.types.tags_list
    import capo_cloudtrail.types.termination_protection_enabled


class CreateDashboardRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.dashboard_name.DashboardName"
    """<p> The name of the dashboard. The name must be unique to your account. </p> <p>To create the Highlights dashboard, the name must be <code>AWSCloudTrail-Highlights</code>.</p>"""
    refresh_schedule: NotRequired[
        "capo_cloudtrail.types.refresh_schedule.RefreshSchedule"
    ]
    """<p> The refresh schedule configuration for the dashboard. </p> <p>To create the Highlights dashboard, you must set a refresh schedule and set the <code>Status</code> to <code>ENABLED</code>. The <code>Unit</code> for the refresh schedule must be <code>HOURS</code> and the <code>Value</code> must be <code>6</code>.</p>"""
    tags_list: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p> Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled. </p>"""
    widgets: NotRequired["capo_cloudtrail.types.request_widget_list.RequestWidgetList"]
    """<p> An array of widgets for a custom dashboard. A custom dashboard can have a maximum of ten widgets. </p> <p>You do not need to specify widgets for the Highlights dashboard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDashboardRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "refresh_schedule" in value:
        import capo_cloudtrail.types.refresh_schedule

        out["RefreshSchedule"] = (
            capo_cloudtrail.types.refresh_schedule.serialize_aws_json_1_1(
                value["refresh_schedule"]
            )
        )
    if "tags_list" in value:
        import capo_cloudtrail.types.tags_list

        out["TagsList"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    if "widgets" in value:
        import capo_cloudtrail.types.request_widget_list

        out["Widgets"] = (
            capo_cloudtrail.types.request_widget_list.serialize_aws_json_1_1(
                value["widgets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDashboardRequest:
    out: CreateDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RefreshSchedule") is not None:
        import capo_cloudtrail.types.refresh_schedule

        out["refresh_schedule"] = (
            capo_cloudtrail.types.refresh_schedule.deserialize_aws_json_1_1(
                data["RefreshSchedule"]
            )
        )
    if data.get("TagsList") is not None:
        import capo_cloudtrail.types.tags_list

        out["tags_list"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    if data.get("TerminationProtectionEnabled") is not None:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    if data.get("Widgets") is not None:
        import capo_cloudtrail.types.request_widget_list

        out["widgets"] = (
            capo_cloudtrail.types.request_widget_list.deserialize_aws_json_1_1(
                data["Widgets"]
            )
        )
    return out
