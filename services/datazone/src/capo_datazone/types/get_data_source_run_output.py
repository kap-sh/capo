"""Generated from Smithy shape ``com.amazonaws.datazone#GetDataSourceRunOutput``."""

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
    import capo_datazone.types.domain_id
    import capo_datazone.types.project_id
    import capo_datazone.types.run_statistics_for_assets


class GetDataSourceRunOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which this data source run was performed.</p>"""
    data_source_id: "capo_datazone.types.data_source_id.DataSourceId"
    """<p>The ID of the data source for this data source run.</p>"""
    id: "capo_datazone.types.data_source_run_id.DataSourceRunId"
    """<p>The ID of the data source run.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project in which this data source run occured.</p>"""
    status: "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
    """<p>The status of this data source run.</p>"""
    type: "capo_datazone.types.data_source_run_type.DataSourceRunType"
    """<p>The type of this data source run.</p>"""
    data_source_configuration_snapshot: NotRequired["str"]
    """<p>The configuration snapshot of the data source run.</p>"""
    run_statistics_for_assets: NotRequired[
        "capo_datazone.types.run_statistics_for_assets.RunStatisticsForAssets"
    ]
    """<p>The asset statistics from this data source run.</p>"""
    lineage_summary: NotRequired[
        "capo_datazone.types.data_source_run_lineage_summary.DataSourceRunLineageSummary"
    ]
    """<p>The summary of the data lineage.</p>"""
    error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when the data source run was created.</p>"""
    updated_at: "capo_datazone.types.date_time.DateTime"
    """<p>The timestamp of when this data source run was updated.</p>"""
    started_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when this data source run started.</p>"""
    stopped_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when this data source run stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSourceRunOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["id"] = value["id"]
    out["projectId"] = value["project_id"]
    import capo_datazone.types.data_source_run_status

    out["status"] = capo_datazone.types.data_source_run_status.serialize_json(
        value["status"]
    )
    import capo_datazone.types.data_source_run_type

    out["type"] = capo_datazone.types.data_source_run_type.serialize_json(value["type"])
    if "data_source_configuration_snapshot" in value:
        out["dataSourceConfigurationSnapshot"] = value[
            "data_source_configuration_snapshot"
        ]
    if "run_statistics_for_assets" in value:
        import capo_datazone.types.run_statistics_for_assets

        out["runStatisticsForAssets"] = (
            capo_datazone.types.run_statistics_for_assets.serialize_json(
                value["run_statistics_for_assets"]
            )
        )
    if "lineage_summary" in value:
        import capo_datazone.types.data_source_run_lineage_summary

        out["lineageSummary"] = (
            capo_datazone.types.data_source_run_lineage_summary.serialize_json(
                value["lineage_summary"]
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
    return out


def deserialize_json(data: dict) -> GetDataSourceRunOutput:
    out: GetDataSourceRunOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        out["project_id"] = ""
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
    if data.get("dataSourceConfigurationSnapshot") is not None:
        out["data_source_configuration_snapshot"] = data[
            "dataSourceConfigurationSnapshot"
        ]
    if data.get("runStatisticsForAssets") is not None:
        import capo_datazone.types.run_statistics_for_assets

        out["run_statistics_for_assets"] = (
            capo_datazone.types.run_statistics_for_assets.deserialize_json(
                data["runStatisticsForAssets"]
            )
        )
    if data.get("lineageSummary") is not None:
        import capo_datazone.types.data_source_run_lineage_summary

        out["lineage_summary"] = (
            capo_datazone.types.data_source_run_lineage_summary.deserialize_json(
                data["lineageSummary"]
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
    return out
