"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeviceSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.device_id
    import capo_workspaces_thin_client.types.device_name
    import capo_workspaces_thin_client.types.device_status
    import capo_workspaces_thin_client.types.environment_id
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_update_schedule
    import capo_workspaces_thin_client.types.timestamp
    import capo_workspaces_thin_client.types.user_id


class DeviceSummary(TypedDict, closed=True):
    id: NotRequired["capo_workspaces_thin_client.types.device_id.DeviceId"]
    """<p>The ID of the device.</p>"""
    serial_number: NotRequired["str"]
    """<p>The hardware serial number of the device.</p>"""
    name: NotRequired["capo_workspaces_thin_client.types.device_name.DeviceName"]
    """<p>The name of the device.</p>"""
    model: NotRequired["str"]
    """<p>The model number of the device.</p>"""
    environment_id: NotRequired[
        "capo_workspaces_thin_client.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of the environment the device is associated with.</p>"""
    status: NotRequired["capo_workspaces_thin_client.types.device_status.DeviceStatus"]
    """<p>The status of the device.</p>"""
    current_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set currently installed on the device.</p>"""
    desired_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set which the device has been set to.</p>"""
    pending_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set that is pending to be installed on the device.</p>"""
    software_set_update_schedule: NotRequired[
        "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
    ]
    """<p>An option to define if software updates should be applied within a maintenance window.</p>"""
    last_connected_at: NotRequired[
        "capo_workspaces_thin_client.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the most recent session on the device.</p>"""
    last_posture_at: NotRequired[
        "capo_workspaces_thin_client.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the most recent check-in of the device.</p>"""
    created_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device was created.</p>"""
    updated_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device was updated.</p>"""
    arn: NotRequired["capo_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    last_user_id: NotRequired["capo_workspaces_thin_client.types.user_id.UserId"]
    """<p>The user ID of the most recent session on the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "name" in value:
        out["name"] = value["name"]
    if "model" in value:
        out["model"] = value["model"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "status" in value:
        import capo_workspaces_thin_client.types.device_status

        out["status"] = capo_workspaces_thin_client.types.device_status.serialize_json(
            value["status"]
        )
    if "current_software_set_id" in value:
        out["currentSoftwareSetId"] = value["current_software_set_id"]
    if "desired_software_set_id" in value:
        out["desiredSoftwareSetId"] = value["desired_software_set_id"]
    if "pending_software_set_id" in value:
        out["pendingSoftwareSetId"] = value["pending_software_set_id"]
    if "software_set_update_schedule" in value:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["softwareSetUpdateSchedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.serialize_json(
                value["software_set_update_schedule"]
            )
        )
    if "last_connected_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["lastConnectedAt"] = (
            capo_workspaces_thin_client.types.timestamp.serialize_json(
                value["last_connected_at"]
            )
        )
    if "last_posture_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["lastPostureAt"] = (
            capo_workspaces_thin_client.types.timestamp.serialize_json(
                value["last_posture_at"]
            )
        )
    if "created_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["createdAt"] = capo_workspaces_thin_client.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_workspaces_thin_client.types.timestamp

        out["updatedAt"] = capo_workspaces_thin_client.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "last_user_id" in value:
        out["lastUserId"] = value["last_user_id"]
    return out


def deserialize_json(data: dict) -> DeviceSummary:
    out: DeviceSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("serialNumber") is not None:
        out["serial_number"] = data["serialNumber"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("model") is not None:
        out["model"] = data["model"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("status") is not None:
        import capo_workspaces_thin_client.types.device_status

        out["status"] = (
            capo_workspaces_thin_client.types.device_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("currentSoftwareSetId") is not None:
        out["current_software_set_id"] = data["currentSoftwareSetId"]
    if data.get("desiredSoftwareSetId") is not None:
        out["desired_software_set_id"] = data["desiredSoftwareSetId"]
    if data.get("pendingSoftwareSetId") is not None:
        out["pending_software_set_id"] = data["pendingSoftwareSetId"]
    if data.get("softwareSetUpdateSchedule") is not None:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["software_set_update_schedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.deserialize_json(
                data["softwareSetUpdateSchedule"]
            )
        )
    if data.get("lastConnectedAt") is not None:
        import capo_workspaces_thin_client.types.timestamp

        out["last_connected_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["lastConnectedAt"]
            )
        )
    if data.get("lastPostureAt") is not None:
        import capo_workspaces_thin_client.types.timestamp

        out["last_posture_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["lastPostureAt"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_workspaces_thin_client.types.timestamp

        out["created_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_workspaces_thin_client.types.timestamp

        out["updated_at"] = (
            capo_workspaces_thin_client.types.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("lastUserId") is not None:
        out["last_user_id"] = data["lastUserId"]
    return out


def redact_sensitive(value: DeviceSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "last_user_id" in value:
        out["last_user_id"] = "*** Sensitive Data Redacted ***"
    return out
