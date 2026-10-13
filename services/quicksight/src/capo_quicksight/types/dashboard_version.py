"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVersion``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.dashboard_error_list
    import capo_quicksight.types.data_set_arns_list
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.sheet_list
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.topic_arns_list
    import capo_quicksight.types.version_description
    import capo_quicksight.types.version_number


class DashboardVersion(TypedDict, closed=True):
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dashboard version was created.</p>"""
    errors: NotRequired["capo_quicksight.types.dashboard_error_list.DashboardErrorList"]
    """<p>Errors associated with this dashboard version.</p>"""
    version_number: NotRequired["capo_quicksight.types.version_number.VersionNumber"]
    """<p>Version number for this version of the dashboard.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The HTTP status of the request.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    source_entity_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>Source entity ARN.</p>"""
    data_set_arns: NotRequired[
        "capo_quicksight.types.data_set_arns_list.DataSetArnsList"
    ]
    """<p>The Amazon Resource Names (ARNs) for the datasets that are associated with this version of the dashboard.</p>"""
    topic_arns: NotRequired["capo_quicksight.types.topic_arns_list.TopicArnsList"]
    """<p>The Amazon Resource Names (ARNs) for the topics that are associated with this version of the dashboard.</p>"""
    description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>Description.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme associated with a version of the dashboard.</p>"""
    sheets: NotRequired["capo_quicksight.types.sheet_list.SheetList"]
    """<p>A list of the associated sheets with the unique identifier and name of each sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVersion) -> dict:
    out: dict = {}
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "errors" in value:
        import capo_quicksight.types.dashboard_error_list

        out["Errors"] = capo_quicksight.types.dashboard_error_list.serialize_json(
            value["errors"]
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "source_entity_arn" in value:
        out["SourceEntityArn"] = value["source_entity_arn"]
    if "data_set_arns" in value:
        import capo_quicksight.types.data_set_arns_list

        out["DataSetArns"] = capo_quicksight.types.data_set_arns_list.serialize_json(
            value["data_set_arns"]
        )
    if "topic_arns" in value:
        import capo_quicksight.types.topic_arns_list

        out["TopicArns"] = capo_quicksight.types.topic_arns_list.serialize_json(
            value["topic_arns"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["Sheets"] = capo_quicksight.types.sheet_list.serialize_json(value["sheets"])
    return out


def deserialize_json(data: dict) -> DashboardVersion:
    out: DashboardVersion = {}  # type: ignore[typeddict-item]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("Errors") is not None:
        import capo_quicksight.types.dashboard_error_list

        out["errors"] = capo_quicksight.types.dashboard_error_list.deserialize_json(
            data["Errors"]
        )
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    if data.get("Status") is not None:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("SourceEntityArn") is not None:
        out["source_entity_arn"] = data["SourceEntityArn"]
    if data.get("DataSetArns") is not None:
        import capo_quicksight.types.data_set_arns_list

        out["data_set_arns"] = (
            capo_quicksight.types.data_set_arns_list.deserialize_json(
                data["DataSetArns"]
            )
        )
    if data.get("TopicArns") is not None:
        import capo_quicksight.types.topic_arns_list

        out["topic_arns"] = capo_quicksight.types.topic_arns_list.deserialize_json(
            data["TopicArns"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("Sheets") is not None:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.deserialize_json(
            data["Sheets"]
        )
    return out


def redact_sensitive(value: DashboardVersion) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.redact_sensitive(
            value["sheets"]
        )
    return out
