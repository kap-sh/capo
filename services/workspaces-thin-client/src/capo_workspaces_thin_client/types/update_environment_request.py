"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#UpdateEnvironmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.desktop_endpoint
    import capo_workspaces_thin_client.types.device_creation_tags_map
    import capo_workspaces_thin_client.types.environment_id
    import capo_workspaces_thin_client.types.environment_name
    import capo_workspaces_thin_client.types.maintenance_window
    import capo_workspaces_thin_client.types.software_set_id_or_empty_string
    import capo_workspaces_thin_client.types.software_set_update_mode
    import capo_workspaces_thin_client.types.software_set_update_schedule


class UpdateEnvironmentRequest(TypedDict, closed=True):
    id: "capo_workspaces_thin_client.types.environment_id.EnvironmentId"
    """<p>The ID of the environment to update.</p>"""
    name: NotRequired[
        "capo_workspaces_thin_client.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment to update.</p>"""
    desktop_arn: NotRequired["capo_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or AppStream 2.0.</p>"""
    desktop_endpoint: NotRequired[
        "capo_workspaces_thin_client.types.desktop_endpoint.DesktopEndpoint"
    ]
    """<p>The URL for the identity provider login (only for environments that use AppStream 2.0).</p>"""
    software_set_update_schedule: NotRequired[
        "capo_workspaces_thin_client.types.software_set_update_schedule.SoftwareSetUpdateSchedule"
    ]
    """<p>An option to define if software updates should be applied within a maintenance window.</p>"""
    maintenance_window: NotRequired[
        "capo_workspaces_thin_client.types.maintenance_window.MaintenanceWindow"
    ]
    """<p>A specification for a time window to apply software updates.</p>"""
    software_set_update_mode: NotRequired[
        "capo_workspaces_thin_client.types.software_set_update_mode.SoftwareSetUpdateMode"
    ]
    """<p>An option to define which software updates to apply.</p>"""
    desired_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id_or_empty_string.SoftwareSetIdOrEmptyString"
    ]
    """<p>The ID of the software set to apply.</p>"""
    device_creation_tags: NotRequired[
        "capo_workspaces_thin_client.types.device_creation_tags_map.DeviceCreationTagsMap"
    ]
    """<p>A map of the key-value pairs of the tag or tags to assign to the newly created devices for this environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "desktop_arn" in value:
        out["desktopArn"] = value["desktop_arn"]
    if "desktop_endpoint" in value:
        out["desktopEndpoint"] = value["desktop_endpoint"]
    if "software_set_update_schedule" in value:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["softwareSetUpdateSchedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.serialize_json(
                value["software_set_update_schedule"]
            )
        )
    if "maintenance_window" in value:
        import capo_workspaces_thin_client.types.maintenance_window

        out["maintenanceWindow"] = (
            capo_workspaces_thin_client.types.maintenance_window.serialize_json(
                value["maintenance_window"]
            )
        )
    if "software_set_update_mode" in value:
        import capo_workspaces_thin_client.types.software_set_update_mode

        out["softwareSetUpdateMode"] = (
            capo_workspaces_thin_client.types.software_set_update_mode.serialize_json(
                value["software_set_update_mode"]
            )
        )
    if "desired_software_set_id" in value:
        out["desiredSoftwareSetId"] = value["desired_software_set_id"]
    if "device_creation_tags" in value:
        import capo_workspaces_thin_client.types.device_creation_tags_map

        out["deviceCreationTags"] = (
            capo_workspaces_thin_client.types.device_creation_tags_map.serialize_json(
                value["device_creation_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentRequest:
    out: UpdateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("desktopArn") is not None:
        out["desktop_arn"] = data["desktopArn"]
    if data.get("desktopEndpoint") is not None:
        out["desktop_endpoint"] = data["desktopEndpoint"]
    if data.get("softwareSetUpdateSchedule") is not None:
        import capo_workspaces_thin_client.types.software_set_update_schedule

        out["software_set_update_schedule"] = (
            capo_workspaces_thin_client.types.software_set_update_schedule.deserialize_json(
                data["softwareSetUpdateSchedule"]
            )
        )
    if data.get("maintenanceWindow") is not None:
        import capo_workspaces_thin_client.types.maintenance_window

        out["maintenance_window"] = (
            capo_workspaces_thin_client.types.maintenance_window.deserialize_json(
                data["maintenanceWindow"]
            )
        )
    if data.get("softwareSetUpdateMode") is not None:
        import capo_workspaces_thin_client.types.software_set_update_mode

        out["software_set_update_mode"] = (
            capo_workspaces_thin_client.types.software_set_update_mode.deserialize_json(
                data["softwareSetUpdateMode"]
            )
        )
    if data.get("desiredSoftwareSetId") is not None:
        out["desired_software_set_id"] = data["desiredSoftwareSetId"]
    if data.get("deviceCreationTags") is not None:
        import capo_workspaces_thin_client.types.device_creation_tags_map

        out["device_creation_tags"] = (
            capo_workspaces_thin_client.types.device_creation_tags_map.deserialize_json(
                data["deviceCreationTags"]
            )
        )
    return out


def redact_sensitive(value: UpdateEnvironmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "desktop_endpoint" in value:
        out["desktop_endpoint"] = "*** Sensitive Data Redacted ***"
    if "device_creation_tags" in value:
        out["device_creation_tags"] = "*** Sensitive Data Redacted ***"
    return out
