"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dashboard_error_list
    import capo_quicksight.types.dashboard_name
    import capo_quicksight.types.dashboard_publish_options
    import capo_quicksight.types.dashboard_version_definition
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeDashboardDefinitionResponse(TypedDict, closed=True):
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the dashboard described.</p>"""
    errors: NotRequired["capo_quicksight.types.dashboard_error_list.DashboardErrorList"]
    """<p>Errors associated with this dashboard version.</p>"""
    name: NotRequired["capo_quicksight.types.dashboard_name.DashboardName"]
    """<p>The display name of the dashboard.</p>"""
    resource_status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>Status associated with the dashboard version.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATION_SUCCESSFUL</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> </p> </li> <li> <p> <code>UPDATE_FAILED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme of the dashboard.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.dashboard_version_definition.DashboardVersionDefinition"
    ]
    """<p>The definition of a dashboard.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    dashboard_publish_options: NotRequired[
        "capo_quicksight.types.dashboard_publish_options.DashboardPublishOptions"
    ]
    """<p>Options for publishing the dashboard:</p> <ul> <li> <p> <code>AvailabilityStatus</code> for <code>AdHocFilteringOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. When this is set to <code>DISABLED</code>, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>ExportToCSVOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. The visual option to export data to .CSV format isn't enabled when this is set to <code>DISABLED</code>. This option is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>VisibilityState</code> for <code>SheetControlsOption</code> - This visibility state can be either <code>COLLAPSED</code> or <code>EXPANDED</code>. This option is <code>COLLAPSED</code> by default. </p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>QuickSuiteActionsOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to <code>DISABLED</code>. This option is <code>DISABLED</code> by default.</p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>ExecutiveSummaryOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. The option to build an executive summary is disabled when this is set to <code>DISABLED</code>. This option is <code>ENABLED</code> by default.</p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>DataStoriesSharingOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. The option to share a data story is disabled when this is set to <code>DISABLED</code>. This option is <code>ENABLED</code> by default.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardDefinitionResponse) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "errors" in value:
        import capo_quicksight.types.dashboard_error_list

        out["Errors"] = capo_quicksight.types.dashboard_error_list.serialize_json(
            value["errors"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_status" in value:
        import capo_quicksight.types.resource_status

        out["ResourceStatus"] = capo_quicksight.types.resource_status.serialize_json(
            value["resource_status"]
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "definition" in value:
        import capo_quicksight.types.dashboard_version_definition

        out["Definition"] = (
            capo_quicksight.types.dashboard_version_definition.serialize_json(
                value["definition"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "dashboard_publish_options" in value:
        import capo_quicksight.types.dashboard_publish_options

        out["DashboardPublishOptions"] = (
            capo_quicksight.types.dashboard_publish_options.serialize_json(
                value["dashboard_publish_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDashboardDefinitionResponse:
    out: DescribeDashboardDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    if data.get("Errors") is not None:
        import capo_quicksight.types.dashboard_error_list

        out["errors"] = capo_quicksight.types.dashboard_error_list.deserialize_json(
            data["Errors"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ResourceStatus") is not None:
        import capo_quicksight.types.resource_status

        out["resource_status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["ResourceStatus"]
        )
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("Definition") is not None:
        import capo_quicksight.types.dashboard_version_definition

        out["definition"] = (
            capo_quicksight.types.dashboard_version_definition.deserialize_json(
                data["Definition"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("DashboardPublishOptions") is not None:
        import capo_quicksight.types.dashboard_publish_options

        out["dashboard_publish_options"] = (
            capo_quicksight.types.dashboard_publish_options.deserialize_json(
                data["DashboardPublishOptions"]
            )
        )
    return out


def redact_sensitive(value: DescribeDashboardDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_quicksight.types.dashboard_version_definition

        out["definition"] = (
            capo_quicksight.types.dashboard_version_definition.redact_sensitive(
                value["definition"]
            )
        )
    return out
