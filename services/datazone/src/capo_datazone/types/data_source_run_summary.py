"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_source_error_message
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_id
    import capo_datazone.types.data_source_run_lineage_summary
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.data_source_run_type
    import capo_datazone.types.date_time
    import capo_datazone.types.project_id
    import capo_datazone.types.run_statistics_for_assets


class DataSourceRunSummary(TypedDict, closed=True):
    id: "capo_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The identifier of the data source run.</p>"""
    data_source_id: "capo_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source of the data source run.</p>"""
    type: "capo_datazone.types.data_source_run_type.DataSourceRunType"
    """<p>The type of the data source run.</p>"""
    status: "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
    """<p>The status of the data source run.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The project ID of the data source run.</p>"""
    run_statistics_for_assets: NotRequired[
        "capo_datazone.types.run_statistics_for_assets.RunStatisticsForAssets"
    ]
    error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    created_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when a data source run was created.</p>"""
    updated_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when a data source run was updated.</p>"""
    started_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when a data source run was started.</p>"""
    stopped_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when a data source run was stopped.</p>"""
    lineage_summary: NotRequired[
        "capo_datazone.types.data_source_run_lineage_summary.DataSourceRunLineageSummary"
    ]
    """<p>The run lineage summary of a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["dataSourceId"] = value["data_source_id"]
    import capo_datazone.types.data_source_run_type

    out["type"] = capo_datazone.types.data_source_run_type.serialize_json(value["type"])
    import capo_datazone.types.data_source_run_status

    out["status"] = capo_datazone.types.data_source_run_status.serialize_json(
        value["status"]
    )
    out["projectId"] = value["project_id"]
    if "run_statistics_for_assets" in value:
        import capo_datazone.types.run_statistics_for_assets

        out["runStatisticsForAssets"] = (
            capo_datazone.types.run_statistics_for_assets.serialize_json(
                value["run_statistics_for_assets"]
            )
        )
    if "error_message" in value:
        import capo_datazone.types.data_source_error_message

        out["errorMessage"] = (
            capo_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
    import capo_datazone.types.date_time

    out["createdAt"] = capo_datazone.types.date_time.serialize_json(value["created_at"])
    import capo_datazone.types.date_time

    out["updatedAt"] = capo_datazone.types.date_time.serialize_json(value["updated_at"])
    if "started_at" in value:
        import capo_datazone.types.date_time

        out["startedAt"] = capo_datazone.types.date_time.serialize_json(
            value["started_at"]
        )
    if "stopped_at" in value:
        import capo_datazone.types.date_time

        out["stoppedAt"] = capo_datazone.types.date_time.serialize_json(
            value["stopped_at"]
        )
    if "lineage_summary" in value:
        import capo_datazone.types.data_source_run_lineage_summary

        out["lineageSummary"] = (
            capo_datazone.types.data_source_run_lineage_summary.serialize_json(
                value["lineage_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceRunSummary:
    out: DataSourceRunSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("type") is not None:
        import capo_datazone.types.data_source_run_type

        out["type"] = capo_datazone.types.data_source_run_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_datazone.types.data_source_run_type.DataSourceRunType", ""
        )
    if data.get("status") is not None:
        import capo_datazone.types.data_source_run_status

        out["status"] = capo_datazone.types.data_source_run_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.data_source_run_status.DataSourceRunStatus", ""
        )
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
    if data.get("runStatisticsForAssets") is not None:
        import capo_datazone.types.run_statistics_for_assets

        out["run_statistics_for_assets"] = (
            capo_datazone.types.run_statistics_for_assets.deserialize_json(
                data["runStatisticsForAssets"]
            )
        )
    if data.get("errorMessage") is not None:
        import capo_datazone.types.data_source_error_message

        out["error_message"] = (
            capo_datazone.types.data_source_error_message.deserialize_json(
                data["errorMessage"]
            )
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
    if data.get("startedAt") is not None:
        import capo_datazone.types.date_time

        out["started_at"] = capo_datazone.types.date_time.deserialize_json(
            data["startedAt"]
        )
    if data.get("stoppedAt") is not None:
        import capo_datazone.types.date_time

        out["stopped_at"] = capo_datazone.types.date_time.deserialize_json(
            data["stoppedAt"]
        )
    if data.get("lineageSummary") is not None:
        import capo_datazone.types.data_source_run_lineage_summary

        out["lineage_summary"] = (
            capo_datazone.types.data_source_run_lineage_summary.deserialize_json(
                data["lineageSummary"]
            )
        )
    return out
