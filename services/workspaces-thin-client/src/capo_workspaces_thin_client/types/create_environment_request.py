"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_thin_client.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.client_token
    import capo_workspaces_thin_client.types.desktop_endpoint
    import capo_workspaces_thin_client.types.device_creation_tags_map
    import capo_workspaces_thin_client.types.environment_name
    import capo_workspaces_thin_client.types.kms_key_arn
    import capo_workspaces_thin_client.types.maintenance_window
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_update_mode
    import capo_workspaces_thin_client.types.software_set_update_schedule
    import capo_workspaces_thin_client.types.tags_map


class CreateEnvironmentRequest(TypedDict, closed=True):
    name: NotRequired[
        "capo_workspaces_thin_client.types.environment_name.EnvironmentName"
    ]
    """<p>The name for the environment.</p>"""
    desktop_arn: "capo_workspaces_thin_client.types.arn.Arn"
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
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set to apply.</p>"""
    kms_key_arn: NotRequired["capo_workspaces_thin_client.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service key to use to encrypt the environment.</p>"""
    client_token: NotRequired[
        "capo_workspaces_thin_client.types.client_token.ClientToken"
    ]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_workspaces_thin_client.types.tags_map.TagsMap"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""
    device_creation_tags: NotRequired[
        "capo_workspaces_thin_client.types.device_creation_tags_map.DeviceCreationTagsMap"
    ]
    """<p>A map of the key-value pairs of the tag or tags to assign to the newly created devices for this environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_workspaces_thin_client.types.tags_map

        out["tags"] = capo_workspaces_thin_client.types.tags_map.serialize_json(
            value["tags"]
        )
    if "device_creation_tags" in value:
        import capo_workspaces_thin_client.types.device_creation_tags_map

        out["deviceCreationTags"] = (
            capo_workspaces_thin_client.types.device_creation_tags_map.serialize_json(
                value["device_creation_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("desktopArn") is not None:
        out["desktop_arn"] = data["desktopArn"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.desktop_arn required")
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
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_workspaces_thin_client.types.tags_map

        out["tags"] = capo_workspaces_thin_client.types.tags_map.deserialize_json(
            data["tags"]
        )
    if data.get("deviceCreationTags") is not None:
        import capo_workspaces_thin_client.types.device_creation_tags_map

        out["device_creation_tags"] = (
            capo_workspaces_thin_client.types.device_creation_tags_map.deserialize_json(
                data["deviceCreationTags"]
            )
        )
    return out
