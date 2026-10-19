"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_source_error_message
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.data_source_status
    import capo_datazone.types.date_time
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.enable_setting
    import capo_datazone.types.name
    import capo_datazone.types.schedule_configuration


class DataSourceSummary(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data source exists.</p>"""
    environment_id: NotRequired["str"]
    """<p>The ID of the environment in which the data source exists.</p>"""
    connection_id: NotRequired["str"]
    """<p>The connection ID that's part of the data source summary.</p>"""
    data_source_id: "capo_datazone.types.data_source_id.DataSourceId"
    """<p>The ID of the data source.</p>"""
    name: "capo_datazone.types.name.Name"
    """<p>The name of the data source.</p>"""
    type: "str"
    """<p>The type of the data source.</p>"""
    status: "capo_datazone.types.data_source_status.DataSourceStatus"
    """<p>The status of the data source.</p>"""
    enable_setting: NotRequired["capo_datazone.types.enable_setting.EnableSetting"]
    """<p>Specifies whether the data source is enabled.</p>"""
    schedule: NotRequired[
        "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
    ]
    last_run_status: NotRequired[
        "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
    ]
    """<p>The status of the last data source run.</p>"""
    last_run_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source run was last performed.</p>"""
    last_run_error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    last_run_asset_count: NotRequired["int"]
    """<p>The count of the assets created during the last data source run.</p>"""
    created_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was created.</p>"""
    updated_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was updated.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The data source description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    out["dataSourceId"] = value["data_source_id"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    import capo_datazone.types.data_source_status

    out["status"] = capo_datazone.types.data_source_status.serialize_json(
        value["status"]
    )
    if "enable_setting" in value:
        import capo_datazone.types.enable_setting

        out["enableSetting"] = capo_datazone.types.enable_setting.serialize_json(
            value["enable_setting"]
        )
    if "schedule" in value:
        import capo_datazone.types.schedule_configuration

        out["schedule"] = capo_datazone.types.schedule_configuration.serialize_json(
            value["schedule"]
        )
    if "last_run_status" in value:
        import capo_datazone.types.data_source_run_status

        out["lastRunStatus"] = (
            capo_datazone.types.data_source_run_status.serialize_json(
                value["last_run_status"]
            )
        )
    if "last_run_at" in value:
        import capo_datazone.types.date_time

        out["lastRunAt"] = capo_datazone.types.date_time.serialize_json(
            value["last_run_at"]
        )
    if "last_run_error_message" in value:
        import capo_datazone.types.data_source_error_message

        out["lastRunErrorMessage"] = (
            capo_datazone.types.data_source_error_message.serialize_json(
                value["last_run_error_message"]
            )
        )
    if "last_run_asset_count" in value:
        out["lastRunAssetCount"] = value["last_run_asset_count"]
    if "created_at" in value:
        import capo_datazone.types.date_time

        out["createdAt"] = capo_datazone.types.date_time.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone.types.date_time

        out["updatedAt"] = capo_datazone.types.date_time.serialize_json(
            value["updated_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DataSourceSummary:
    out: DataSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("dataSourceId") is not None:
        out["data_source_id"] = data["dataSourceId"]
    else:
        out["data_source_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.data_source_status

        out["status"] = capo_datazone.types.data_source_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.data_source_status.DataSourceStatus", ""
        )
    if data.get("enableSetting") is not None:
        import capo_datazone.types.enable_setting

        out["enable_setting"] = capo_datazone.types.enable_setting.deserialize_json(
            data["enableSetting"]
        )
    if data.get("schedule") is not None:
        import capo_datazone.types.schedule_configuration

        out["schedule"] = capo_datazone.types.schedule_configuration.deserialize_json(
            data["schedule"]
        )
    if data.get("lastRunStatus") is not None:
        import capo_datazone.types.data_source_run_status

        out["last_run_status"] = (
            capo_datazone.types.data_source_run_status.deserialize_json(
                data["lastRunStatus"]
            )
        )
    if data.get("lastRunAt") is not None:
        import capo_datazone.types.date_time

        out["last_run_at"] = capo_datazone.types.date_time.deserialize_json(
            data["lastRunAt"]
        )
    if data.get("lastRunErrorMessage") is not None:
        import capo_datazone.types.data_source_error_message

        out["last_run_error_message"] = (
            capo_datazone.types.data_source_error_message.deserialize_json(
                data["lastRunErrorMessage"]
            )
        )
    if data.get("lastRunAssetCount") is not None:
        out["last_run_asset_count"] = data["lastRunAssetCount"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.date_time

        out["created_at"] = capo_datazone.types.date_time.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_datazone.types.date_time

        out["updated_at"] = capo_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: DataSourceSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "schedule" in value:
        out["schedule"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
