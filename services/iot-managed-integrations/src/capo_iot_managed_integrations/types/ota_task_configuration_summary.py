"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskConfigurationSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.created_at
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_configuration_name


class OtaTaskConfigurationSummary(TypedDict, closed=True):
    task_configuration_id: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
    ]
    """<p>The id of the over-the-air (OTA) task configuration</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
    ]
    """<p>The name of the over-the-air (OTA) task configuration.</p>"""
    created_at: NotRequired["capo_iot_managed_integrations.types.created_at.CreatedAt"]
    """<p>The timestamp value of when the over-the-air (OTA) task configuration was created at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskConfigurationSummary) -> dict:
    out: dict = {}
    if "task_configuration_id" in value:
        out["TaskConfigurationId"] = value["task_configuration_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> OtaTaskConfigurationSummary:
    out: OtaTaskConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("TaskConfigurationId") is not None:
        out["task_configuration_id"] = data["TaskConfigurationId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out


def redact_sensitive(value: OtaTaskConfigurationSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
