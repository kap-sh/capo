"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunActivity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_asset_activity_status
    import capo_datazone.types.data_source_error_message
    import capo_datazone.types.data_source_run_id
    import capo_datazone.types.date_time
    import capo_datazone.types.description
    import capo_datazone.types.lineage_info
    import capo_datazone.types.name
    import capo_datazone.types.project_id


class DataSourceRunActivity(TypedDict, closed=True):
    database: "capo_datazone.types.name.Name"
    """<p>The database included in the data source run activity.</p>"""
    data_source_run_id: "capo_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source for the data source run activity.</p>"""
    technical_name: "capo_datazone.types.name.Name"
    """<p>The technical name included in the data source run activity.</p>"""
    data_asset_status: (
        "capo_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
    )
    """<p>The status of the asset included in the data source run activity.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The project ID included in the data source run activity.</p>"""
    data_asset_id: NotRequired["str"]
    """<p>The identifier of the asset included in the data source run activity.</p>"""
    technical_description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The technical description included in the data source run activity.</p>"""
    error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    lineage_summary: NotRequired["capo_datazone.types.lineage_info.LineageInfo"]
    """<p>The data lineage summary.</p>"""
    created_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when data source run activity was created.</p>"""
    updated_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when data source run activity was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunActivity) -> dict:
    out: dict = {}
    out["database"] = value["database"]
    out["dataSourceRunId"] = value["data_source_run_id"]
    out["technicalName"] = value["technical_name"]
    import capo_datazone.types.data_asset_activity_status

    out["dataAssetStatus"] = (
        capo_datazone.types.data_asset_activity_status.serialize_json(
            value["data_asset_status"]
        )
    )
    out["projectId"] = value["project_id"]
    if "data_asset_id" in value:
        out["dataAssetId"] = value["data_asset_id"]
    if "technical_description" in value:
        out["technicalDescription"] = value["technical_description"]
    if "error_message" in value:
        import capo_datazone.types.data_source_error_message

        out["errorMessage"] = (
            capo_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
    if "lineage_summary" in value:
        import capo_datazone.types.lineage_info

        out["lineageSummary"] = capo_datazone.types.lineage_info.serialize_json(
            value["lineage_summary"]
        )
    import capo_datazone.types.date_time

    out["createdAt"] = capo_datazone.types.date_time.serialize_json(value["created_at"])
    import capo_datazone.types.date_time

    out["updatedAt"] = capo_datazone.types.date_time.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> DataSourceRunActivity:
    out: DataSourceRunActivity = {}  # type: ignore[typeddict-item]
    if data.get("database") is not None:
        out["database"] = data["database"]
    else:
        out["database"] = ""
    if data.get("dataSourceRunId") is not None:
        out["data_source_run_id"] = data["dataSourceRunId"]
    else:
        out["data_source_run_id"] = ""
    if data.get("technicalName") is not None:
        out["technical_name"] = data["technicalName"]
    else:
        out["technical_name"] = ""
    if data.get("dataAssetStatus") is not None:
        import capo_datazone.types.data_asset_activity_status

        out["data_asset_status"] = (
            capo_datazone.types.data_asset_activity_status.deserialize_json(
                data["dataAssetStatus"]
            )
        )
    else:
        import typing

        out["data_asset_status"] = typing.cast(
            "capo_datazone.types.data_asset_activity_status.DataAssetActivityStatus", ""
        )
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("dataAssetId") is not None:
        out["data_asset_id"] = data["dataAssetId"]
    if data.get("technicalDescription") is not None:
        out["technical_description"] = data["technicalDescription"]
    if data.get("errorMessage") is not None:
        import capo_datazone.types.data_source_error_message

        out["error_message"] = (
            capo_datazone.types.data_source_error_message.deserialize_json(
                data["errorMessage"]
            )
        )
    if data.get("lineageSummary") is not None:
        import capo_datazone.types.lineage_info

        out["lineage_summary"] = capo_datazone.types.lineage_info.deserialize_json(
            data["lineageSummary"]
        )
    if data.get("createdAt") is not None:
        import capo_datazone.types.date_time

        out["created_at"] = capo_datazone.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_datazone.types.date_time

        out["updated_at"] = capo_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: DataSourceRunActivity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "database" in value:
        out["database"] = "*** Sensitive Data Redacted ***"
    if "technical_name" in value:
        out["technical_name"] = "*** Sensitive Data Redacted ***"
    if "technical_description" in value:
        out["technical_description"] = "*** Sensitive Data Redacted ***"
    return out
