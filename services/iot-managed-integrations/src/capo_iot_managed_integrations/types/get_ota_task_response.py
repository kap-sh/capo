"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetOtaTaskResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.created_at
    import capo_iot_managed_integrations.types.last_updated_at
    import capo_iot_managed_integrations.types.ota_description
    import capo_iot_managed_integrations.types.ota_mechanism
    import capo_iot_managed_integrations.types.ota_protocol
    import capo_iot_managed_integrations.types.ota_status
    import capo_iot_managed_integrations.types.ota_target_query_string
    import capo_iot_managed_integrations.types.ota_task_arn
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_execution_retry_config
    import capo_iot_managed_integrations.types.ota_task_id
    import capo_iot_managed_integrations.types.ota_task_scheduling_config
    import capo_iot_managed_integrations.types.ota_type
    import capo_iot_managed_integrations.types.s3_url
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.target
    import capo_iot_managed_integrations.types.task_processing_details


class GetOtaTaskResponse(TypedDict, closed=True):
    task_id: NotRequired["capo_iot_managed_integrations.types.ota_task_id.OtaTaskId"]
    """<p>The id of the over-the-air (OTA) task.</p>"""
    task_arn: NotRequired["capo_iot_managed_integrations.types.ota_task_arn.OtaTaskArn"]
    """<p>The Amazon Resource Name (ARN) of the over-the-air (OTA) task</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>The description of the over-the-air (OTA) task.</p>"""
    s3_url: NotRequired["capo_iot_managed_integrations.types.s3_url.S3Url"]
    """<p>The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.</p>"""
    protocol: NotRequired[
        "capo_iot_managed_integrations.types.ota_protocol.OtaProtocol"
    ]
    """<p>The connection protocol the over-the-air (OTA) task uses to update the device.</p>"""
    ota_type: NotRequired["capo_iot_managed_integrations.types.ota_type.OtaType"]
    """<p>The frequency type for the over-the-air (OTA) task.</p>"""
    ota_target_query_string: NotRequired[
        "capo_iot_managed_integrations.types.ota_target_query_string.OtaTargetQueryString"
    ]
    """<p>The query string to add things to the thing group.</p>"""
    ota_mechanism: NotRequired[
        "capo_iot_managed_integrations.types.ota_mechanism.OtaMechanism"
    ]
    """<p>The deployment mechanism for the over-the-air (OTA) task.</p>"""
    target: NotRequired["capo_iot_managed_integrations.types.target.Target"]
    """<p>The device targeted for the over-the-air (OTA) task.</p>"""
    created_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the over-the-air (OTA) task was created.</p>"""
    last_updated_at: NotRequired[
        "capo_iot_managed_integrations.types.last_updated_at.LastUpdatedAt"
    ]
    """<p>The timestamp value of when the over-the-air (OTA) task was last updated at.</p>"""
    task_configuration_id: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The identifier for the over-the-air (OTA) task configuration.</p>"""
    task_processing_details: NotRequired[
        "capo_iot_managed_integrations.types.task_processing_details.TaskProcessingDetails"
    ]
    """<p>The processing details of all over-the-air (OTA) tasks.</p>"""
    ota_scheduling_config: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_scheduling_config.OtaTaskSchedulingConfig"
    ]
    ota_task_execution_retry_config: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_execution_retry_config.OtaTaskExecutionRetryConfig"
    ]
    status: NotRequired["capo_iot_managed_integrations.types.ota_status.OtaStatus"]
    """<p>The status of the over-the-air (OTA) task.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOtaTaskResponse) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "s3_url" in value:
        out["S3Url"] = value["s3_url"]
    if "protocol" in value:
        import capo_iot_managed_integrations.types.ota_protocol

        out["Protocol"] = (
            capo_iot_managed_integrations.types.ota_protocol.serialize_json(
                value["protocol"]
            )
        )
    if "ota_type" in value:
        import capo_iot_managed_integrations.types.ota_type

        out["OtaType"] = capo_iot_managed_integrations.types.ota_type.serialize_json(
            value["ota_type"]
        )
    if "ota_target_query_string" in value:
        out["OtaTargetQueryString"] = value["ota_target_query_string"]
    if "ota_mechanism" in value:
        import capo_iot_managed_integrations.types.ota_mechanism

        out["OtaMechanism"] = (
            capo_iot_managed_integrations.types.ota_mechanism.serialize_json(
                value["ota_mechanism"]
            )
        )
    if "target" in value:
        import capo_iot_managed_integrations.types.target

        out["Target"] = capo_iot_managed_integrations.types.target.serialize_json(
            value["target"]
        )
    if "created_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_iot_managed_integrations.types.last_updated_at

        out["LastUpdatedAt"] = (
            capo_iot_managed_integrations.types.last_updated_at.serialize_json(
                value["last_updated_at"]
            )
        )
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "task_processing_details" in value:
        import capo_iot_managed_integrations.types.task_processing_details

        out["TaskProcessingDetails"] = (
            capo_iot_managed_integrations.types.task_processing_details.serialize_json(
                value["task_processing_details"]
            )
        )
    if "ota_scheduling_config" in value:
        import capo_iot_managed_integrations.types.ota_task_scheduling_config

        out["OtaSchedulingConfig"] = (
            capo_iot_managed_integrations.types.ota_task_scheduling_config.serialize_json(
                value["ota_scheduling_config"]
            )
        )
    if "ota_task_execution_retry_config" in value:
        import capo_iot_managed_integrations.types.ota_task_execution_retry_config

        out["OtaTaskExecutionRetryConfig"] = (
            capo_iot_managed_integrations.types.ota_task_execution_retry_config.serialize_json(
                value["ota_task_execution_retry_config"]
            )
        )
    if "status" in value:
        import capo_iot_managed_integrations.types.ota_status

        out["Status"] = capo_iot_managed_integrations.types.ota_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetOtaTaskResponse:
    out: GetOtaTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("S3Url") is not None:
        out["s3_url"] = data["S3Url"]
    if data.get("Protocol") is not None:
        import capo_iot_managed_integrations.types.ota_protocol

        out["protocol"] = (
            capo_iot_managed_integrations.types.ota_protocol.deserialize_json(
                data["Protocol"]
            )
        )
    if data.get("OtaType") is not None:
        import capo_iot_managed_integrations.types.ota_type

        out["ota_type"] = capo_iot_managed_integrations.types.ota_type.deserialize_json(
            data["OtaType"]
        )
    if data.get("OtaTargetQueryString") is not None:
        out["ota_target_query_string"] = data["OtaTargetQueryString"]
    if data.get("OtaMechanism") is not None:
        import capo_iot_managed_integrations.types.ota_mechanism

        out["ota_mechanism"] = (
            capo_iot_managed_integrations.types.ota_mechanism.deserialize_json(
                data["OtaMechanism"]
            )
        )
    if data.get("Target") is not None:
        import capo_iot_managed_integrations.types.target

        out["target"] = capo_iot_managed_integrations.types.target.deserialize_json(
            data["Target"]
        )
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_iot_managed_integrations.types.last_updated_at

        out["last_updated_at"] = (
            capo_iot_managed_integrations.types.last_updated_at.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("TaskConfigurationId") is not None:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if data.get("TaskProcessingDetails") is not None:
        import capo_iot_managed_integrations.types.task_processing_details

        out["task_processing_details"] = (
            capo_iot_managed_integrations.types.task_processing_details.deserialize_json(
                data["TaskProcessingDetails"]
            )
        )
    if data.get("OtaSchedulingConfig") is not None:
        import capo_iot_managed_integrations.types.ota_task_scheduling_config

        out["ota_scheduling_config"] = (
            capo_iot_managed_integrations.types.ota_task_scheduling_config.deserialize_json(
                data["OtaSchedulingConfig"]
            )
        )
    if data.get("OtaTaskExecutionRetryConfig") is not None:
        import capo_iot_managed_integrations.types.ota_task_execution_retry_config

        out["ota_task_execution_retry_config"] = (
            capo_iot_managed_integrations.types.ota_task_execution_retry_config.deserialize_json(
                data["OtaTaskExecutionRetryConfig"]
            )
        )
    if data.get("Status") is not None:
        import capo_iot_managed_integrations.types.ota_status

        out["status"] = capo_iot_managed_integrations.types.ota_status.deserialize_json(
            data["Status"]
        )
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetOtaTaskResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
