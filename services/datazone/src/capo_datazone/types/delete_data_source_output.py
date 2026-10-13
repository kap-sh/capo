"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDataSourceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.data_source_configuration_output
    import capo_datazone.types.data_source_error_message
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.data_source_status
    import capo_datazone.types.data_source_type
    import capo_datazone.types.date_time
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.enable_setting
    import capo_datazone.types.environment_id
    import capo_datazone.types.form_output_list
    import capo_datazone.types.name
    import capo_datazone.types.project_id
    import capo_datazone.types.schedule_configuration
    import capo_datazone.types.self_grant_status_output


class DeleteDataSourceOutput(TypedDict, closed=True):
    id: "capo_datazone.types.data_source_id.DataSourceId"
    """<p>The ID of the data source that is deleted.</p>"""
    status: NotRequired["capo_datazone.types.data_source_status.DataSourceStatus"]
    """<p>The status of this data source.</p>"""
    type: NotRequired["capo_datazone.types.data_source_type.DataSourceType"]
    """<p>The type of this data source.</p>"""
    name: "capo_datazone.types.name.Name"
    """<p>The name of the data source that is deleted.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the data source that is deleted.</p>"""
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the data source is deleted.</p>"""
    project_id: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the project in which this data source exists and from which it's deleted.</p>"""
    environment_id: NotRequired["capo_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environemnt associated with this data source.</p>"""
    connection_id: NotRequired["str"]
    """<p>The ID of the connection that is deleted.</p>"""
    configuration: NotRequired[
        "capo_datazone.types.data_source_configuration_output.DataSourceConfigurationOutput"
    ]
    """<p>The configuration of the data source that is deleted.</p>"""
    enable_setting: NotRequired["capo_datazone.types.enable_setting.EnableSetting"]
    """<p>The enable setting of the data source that specifies whether the data source is enabled or disabled.</p>"""
    publish_on_import: NotRequired["bool"]
    """<p>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</p>"""
    asset_forms_output: NotRequired[
        "capo_datazone.types.form_output_list.FormOutputList"
    ]
    """<p>The asset data forms associated with this data source.</p>"""
    schedule: NotRequired[
        "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule of runs for this data source.</p>"""
    last_run_status: NotRequired[
        "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
    ]
    """<p>The status of the last run of this data source.</p>"""
    last_run_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when the data source was last run.</p>"""
    last_run_error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    error_message: NotRequired[
        "capo_datazone.types.data_source_error_message.DataSourceErrorMessage"
    ]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when this data source was created.</p>"""
    updated_at: NotRequired["capo_datazone.types.date_time.DateTime"]
    """<p>The timestamp of when this data source was updated.</p>"""
    self_grant_status: NotRequired[
        "capo_datazone.types.self_grant_status_output.SelfGrantStatusOutput"
    ]
    """<p>Specifies the status of the self-granting functionality.</p>"""
    retain_permissions_on_revoke_failure: NotRequired["bool"]
    """<p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "status" in value:
        import capo_datazone.types.data_source_status

        out["status"] = capo_datazone.types.data_source_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        out["type"] = value["type"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["domainId"] = value["domain_id"]
    out["projectId"] = value["project_id"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "configuration" in value:
        import capo_datazone.types.data_source_configuration_output

        out["configuration"] = (
            capo_datazone.types.data_source_configuration_output.serialize_json(
                value["configuration"]
            )
        )
    if "enable_setting" in value:
        import capo_datazone.types.enable_setting

        out["enableSetting"] = capo_datazone.types.enable_setting.serialize_json(
            value["enable_setting"]
        )
    if "publish_on_import" in value:
        out["publishOnImport"] = value["publish_on_import"]
    if "asset_forms_output" in value:
        import capo_datazone.types.form_output_list

        out["assetFormsOutput"] = capo_datazone.types.form_output_list.serialize_json(
            value["asset_forms_output"]
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
    if "error_message" in value:
        import capo_datazone.types.data_source_error_message

        out["errorMessage"] = (
            capo_datazone.types.data_source_error_message.serialize_json(
                value["error_message"]
            )
        )
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
    if "self_grant_status" in value:
        import capo_datazone.types.self_grant_status_output

        out["selfGrantStatus"] = (
            capo_datazone.types.self_grant_status_output.serialize_json(
                value["self_grant_status"]
            )
        )
    if "retain_permissions_on_revoke_failure" in value:
        out["retainPermissionsOnRevokeFailure"] = value[
            "retain_permissions_on_revoke_failure"
        ]
    return out


def deserialize_json(data: dict) -> DeleteDataSourceOutput:
    out: DeleteDataSourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteDataSourceOutput.id required")
    if data.get("status") is not None:
        import capo_datazone.types.data_source_status

        out["status"] = capo_datazone.types.data_source_status.deserialize_json(
            data["status"]
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteDataSourceOutput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("DeleteDataSourceOutput.domain_id required")
    if data.get("projectId") is not None:
        out["project_id"] = data["projectId"]
    else:
        raise DeserializationError("DeleteDataSourceOutput.project_id required")
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    if data.get("configuration") is not None:
        import capo_datazone.types.data_source_configuration_output

        out["configuration"] = (
            capo_datazone.types.data_source_configuration_output.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("enableSetting") is not None:
        import capo_datazone.types.enable_setting

        out["enable_setting"] = capo_datazone.types.enable_setting.deserialize_json(
            data["enableSetting"]
        )
    if data.get("publishOnImport") is not None:
        out["publish_on_import"] = data["publishOnImport"]
    if data.get("assetFormsOutput") is not None:
        import capo_datazone.types.form_output_list

        out["asset_forms_output"] = (
            capo_datazone.types.form_output_list.deserialize_json(
                data["assetFormsOutput"]
            )
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
    if data.get("updatedAt") is not None:
        import capo_datazone.types.date_time

        out["updated_at"] = capo_datazone.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    if data.get("selfGrantStatus") is not None:
        import capo_datazone.types.self_grant_status_output

        out["self_grant_status"] = (
            capo_datazone.types.self_grant_status_output.deserialize_json(
                data["selfGrantStatus"]
            )
        )
    if data.get("retainPermissionsOnRevokeFailure") is not None:
        out["retain_permissions_on_revoke_failure"] = data[
            "retainPermissionsOnRevokeFailure"
        ]
    return out


def redact_sensitive(value: DeleteDataSourceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "asset_forms_output" in value:
        import capo_datazone.types.form_output_list

        out["asset_forms_output"] = (
            capo_datazone.types.form_output_list.redact_sensitive(
                value["asset_forms_output"]
            )
        )
    if "schedule" in value:
        out["schedule"] = "*** Sensitive Data Redacted ***"
    return out
