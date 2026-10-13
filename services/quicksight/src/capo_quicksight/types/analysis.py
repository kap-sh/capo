"""Generated from Smithy shape ``com.amazonaws.quicksight#Analysis``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_error_list
    import capo_quicksight.types.analysis_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_set_arns_list
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.sheet_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.topic_arns_list


class Analysis(TypedDict, closed=True):
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the analysis.</p>"""
    name: NotRequired["capo_quicksight.types.analysis_name.AnalysisName"]
    """<p>The descriptive name of the analysis.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>Status associated with the analysis.</p>"""
    errors: NotRequired["capo_quicksight.types.analysis_error_list.AnalysisErrorList"]
    """<p>Errors associated with the analysis.</p>"""
    data_set_arns: NotRequired[
        "capo_quicksight.types.data_set_arns_list.DataSetArnsList"
    ]
    """<p>The ARNs of the datasets of the analysis.</p>"""
    topic_arns: NotRequired["capo_quicksight.types.topic_arns_list.TopicArnsList"]
    """<p>The ARNs of the topics associated with the analysis.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme of the analysis.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the analysis was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the analysis was last updated.</p>"""
    sheets: NotRequired["capo_quicksight.types.sheet_list.SheetList"]
    """<p>A list of the associated sheets with the unique identifier and name of each sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Analysis) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "errors" in value:
        import capo_quicksight.types.analysis_error_list

        out["Errors"] = capo_quicksight.types.analysis_error_list.serialize_json(
            value["errors"]
        )
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
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["Sheets"] = capo_quicksight.types.sheet_list.serialize_json(value["sheets"])
    return out


def deserialize_json(data: dict) -> Analysis:
    out: Analysis = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisId") is not None:
        out["analysis_id"] = data["AnalysisId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if data.get("Errors") is not None:
        import capo_quicksight.types.analysis_error_list

        out["errors"] = capo_quicksight.types.analysis_error_list.deserialize_json(
            data["Errors"]
        )
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
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("Sheets") is not None:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.deserialize_json(
            data["Sheets"]
        )
    return out


def redact_sensitive(value: Analysis) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.redact_sensitive(
            value["sheets"]
        )
    return out
