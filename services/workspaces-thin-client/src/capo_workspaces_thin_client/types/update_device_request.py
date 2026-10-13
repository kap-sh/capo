"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateDeviceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.device_id
    import capo_workspaces_thin_client.types.device_name
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_update_schedule


class UpdateDeviceRequest(TypedDict, closed=True):
    id: "capo_workspaces_thin_client.types.device_id.DeviceId"
    """<p>The ID of the device to update.</p>"""
    name: NotRequired["capo_workspaces_thin_client.types.device_name.DeviceName"]
    """<p>The name of the device to update.</p>"""
    desired_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set to apply.</p>"""
    software_set_update_schedule: NotRequired[
        "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
    ]
    """<p>An option to define if software updates should be applied within a maintenance window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "desired_software_set_id" in value:
        out["desiredSoftwareSetId"] = value["desired_software_set_id"]
    if "software_set_update_schedule" in value:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["softwareSetUpdateSchedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.serialize_json(
                value["software_set_update_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDeviceRequest:
    out: UpdateDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("desiredSoftwareSetId") is not None:
        out["desired_software_set_id"] = data["desiredSoftwareSetId"]
    if data.get("softwareSetUpdateSchedule") is not None:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["software_set_update_schedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.deserialize_json(
                data["softwareSetUpdateSchedule"]
            )
        )
    return out


def redact_sensitive(value: UpdateDeviceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
