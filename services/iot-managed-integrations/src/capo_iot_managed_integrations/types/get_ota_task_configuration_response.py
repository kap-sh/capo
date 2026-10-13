"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetOtaTaskConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.created_at
    import capo_iot_managed_integrations.types.ota_description
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_configuration_name
    import capo_iot_managed_integrations.types.push_config


class GetOtaTaskConfigurationResponse(TypedDict, closed=True):
    task_configuration_id: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The over-the-air (OTA) task configuration id.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
    ]
    """<p>The name of the over-the-air (OTA) task configuration.</p>"""
    push_config: NotRequired[
        "capo_iot_managed_integrations.types.push_config.PushConfig"
    ]
    """<p>Describes the type of configuration used for the over-the-air (OTA) task.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.ota_description.OtaDescription"
    ]
    """<p>A description of the over-the-air (OTA) task configuration.</p>"""
    created_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the over-the-air (OTA) task configuration was created at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOtaTaskConfigurationResponse) -> dict:
    out: dict = {}
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "push_config" in value:
        import capo_iot_managed_integrations.types.push_config

        out["PushConfig"] = (
            capo_iot_managed_integrations.types.push_config.serialize_json(
                value["push_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetOtaTaskConfigurationResponse:
    out: GetOtaTaskConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskConfigurationId") is not None:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("PushConfig") is not None:
        import capo_iot_managed_integrations.types.push_config

        out["push_config"] = (
            capo_iot_managed_integrations.types.push_config.deserialize_json(
                data["PushConfig"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out


def redact_sensitive(value: GetOtaTaskConfigurationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
