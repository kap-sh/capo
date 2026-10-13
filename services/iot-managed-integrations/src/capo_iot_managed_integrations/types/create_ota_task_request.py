"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateOtaTaskRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.ota_description
    import capo_iot_managed_integrations.types.ota_mechanism
    import capo_iot_managed_integrations.types.ota_protocol
    import capo_iot_managed_integrations.types.ota_target_query_string
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_execution_retry_config
    import capo_iot_managed_integrations.types.ota_task_scheduling_config
    import capo_iot_managed_integrations.types.ota_type
    import capo_iot_managed_integrations.types.s3_url
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.target


class CreateOtaTaskRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>The description of the over-the-air (OTA) task.</p>"""
    s3_url: "capo_iot_managed_integrations.types.s3_url.S3Url"
    """<p>The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.</p>"""
    protocol: NotRequired[
        "capo_iot_managed_integrations.types.ota_protocol.OtaProtocol"
    ]
    """<p>The connection protocol the over-the-air (OTA) task uses to update the device.</p>"""
    target: NotRequired["capo_iot_managed_integrations.types.target.Target"]
    """<p>The device targeted for the over-the-air (OTA) task.</p>"""
    task_configuration_id: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The identifier for the over-the-air (OTA) task configuration.</p>"""
    ota_mechanism: NotRequired[
        "capo_iot_managed_integrations.types.ota_mechanism.OtaMechanism"
    ]
    """<p>The deployment mechanism for the over-the-air (OTA) task.</p>"""
    ota_type: "capo_iot_managed_integrations.types.ota_type.OtaType"
    """<p>The frequency type for the over-the-air (OTA) task.</p>"""
    ota_target_query_string: NotRequired[
        "capo_iot_managed_integrations.types.ota_target_query_string.OtaTargetQueryString"
    ]
    """<p>The query string to add things to the thing group.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    ota_scheduling_config: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_scheduling_config.OtaTaskSchedulingConfig"
    ]
    ota_task_execution_retry_config: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_execution_retry_config.OtaTaskExecutionRetryConfig"
    ]
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOtaTaskRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["S3Url"] = value["s3_url"]
    if "protocol" in value:
        import capo_iot_managed_integrations.types.ota_protocol

        out["Protocol"] = (
            capo_iot_managed_integrations.types.ota_protocol.serialize_json(
                value["protocol"]
            )
        )
    if "target" in value:
        import capo_iot_managed_integrations.types.target

        out["Target"] = capo_iot_managed_integrations.types.target.serialize_json(
            value["target"]
        )
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "ota_mechanism" in value:
        import capo_iot_managed_integrations.types.ota_mechanism

        out["OtaMechanism"] = (
            capo_iot_managed_integrations.types.ota_mechanism.serialize_json(
                value["ota_mechanism"]
            )
        )
    import capo_iot_managed_integrations.types.ota_type

    out["OtaType"] = capo_iot_managed_integrations.types.ota_type.serialize_json(
        value["ota_type"]
    )
    if "ota_target_query_string" in value:
        out["OtaTargetQueryString"] = value["ota_target_query_string"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateOtaTaskRequest:
    out: CreateOtaTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("S3Url") is not None:
        out["s3_url"] = data["S3Url"]
    else:
        raise DeserializationError("CreateOtaTaskRequest.s3_url required")
    if data.get("Protocol") is not None:
        import capo_iot_managed_integrations.types.ota_protocol

        out["protocol"] = (
            capo_iot_managed_integrations.types.ota_protocol.deserialize_json(
                data["Protocol"]
            )
        )
    if data.get("Target") is not None:
        import capo_iot_managed_integrations.types.target

        out["target"] = capo_iot_managed_integrations.types.target.deserialize_json(
            data["Target"]
        )
    if data.get("TaskConfigurationId") is not None:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if data.get("OtaMechanism") is not None:
        import capo_iot_managed_integrations.types.ota_mechanism

        out["ota_mechanism"] = (
            capo_iot_managed_integrations.types.ota_mechanism.deserialize_json(
                data["OtaMechanism"]
            )
        )
    if data.get("OtaType") is not None:
        import capo_iot_managed_integrations.types.ota_type

        out["ota_type"] = capo_iot_managed_integrations.types.ota_type.deserialize_json(
            data["OtaType"]
        )
    else:
        raise DeserializationError("CreateOtaTaskRequest.ota_type required")
    if data.get("OtaTargetQueryString") is not None:
        out["ota_target_query_string"] = data["OtaTargetQueryString"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
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
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateOtaTaskRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
