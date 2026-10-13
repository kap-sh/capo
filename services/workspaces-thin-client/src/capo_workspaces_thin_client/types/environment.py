"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#Environment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.activation_code
    import capo_workspaces_thin_client.types.arn
    import capo_workspaces_thin_client.types.desktop_endpoint
    import capo_workspaces_thin_client.types.desktop_type
    import capo_workspaces_thin_client.types.device_creation_tags_map
    import capo_workspaces_thin_client.types.environment_id
    import capo_workspaces_thin_client.types.environment_name
    import capo_workspaces_thin_client.types.environment_software_set_compliance_status
    import capo_workspaces_thin_client.types.kms_key_arn
    import capo_workspaces_thin_client.types.maintenance_window
    import capo_workspaces_thin_client.types.software_set_id
    import capo_workspaces_thin_client.types.software_set_update_mode
    import capo_workspaces_thin_client.types.software_set_update_schedule
    import capo_workspaces_thin_client.types.timestamp


class Environment(TypedDict, closed=True):
    id: NotRequired["capo_workspaces_thin_client.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    name: NotRequired[
        "capo_workspaces_thin_client.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment.</p>"""
    desktop_arn: NotRequired["capo_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or AppStream 2.0.</p>"""
    desktop_endpoint: NotRequired[
        "capo_workspaces_thin_client.types.desktop_endpoint.DesktopEndpoint"
    ]
    """<p>The URL for the identity provider login (only for environments that use AppStream 2.0).</p>"""
    desktop_type: NotRequired[
        "capo_workspaces_thin_client.types.desktop_type.DesktopType"
    ]
    """<p>The type of streaming desktop for the environment.</p>"""
    activation_code: NotRequired[
        "capo_workspaces_thin_client.types.activation_code.ActivationCode"
    ]
    """<p>The activation code to register a device to the environment.</p>"""
    registered_devices_count: NotRequired["int"]
    """<p>The number of devices registered to the environment.</p>"""
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
    pending_software_set_id: NotRequired[
        "capo_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    ]
    """<p>The ID of the software set that is pending to be installed.</p>"""
    pending_software_set_version: NotRequired["str"]
    """<p>The version of the software set that is pending to be installed.</p>"""
    software_set_compliance_status: NotRequired[
        "capo_workspaces_thin_client.types.environment_software_set_compliance_status.EnvironmentSoftwareSetComplianceStatus"
    ]
    """<p>Describes if the software currently installed on all devices in the environment is a supported version.</p>"""
    created_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the environment was created.</p>"""
    updated_at: NotRequired["capo_workspaces_thin_client.types.timestamp.Timestamp"]
    """<p>The timestamp of when the device was updated.</p>"""
    arn: NotRequired["capo_workspaces_thin_client.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the environment.</p>"""
    kms_key_arn: NotRequired["capo_workspaces_thin_client.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service key used to encrypt the environment.</p>"""
    device_creation_tags: NotRequired[
        "capo_workspaces_thin_client.types.device_creation_tags_map.DeviceCreationTagsMap"
    ]
    """<p>The tag keys and optional values for the newly created devices for this environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environment) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "desktop_arn" in value:
        out["desktopArn"] = value["desktop_arn"]
    if "desktop_endpoint" in value:
        out["desktopEndpoint"] = value["desktop_endpoint"]
    if "desktop_type" in value:
        import capo_workspaces_thin_client.types.desktop_type

        out["desktopType"] = (
            capo_workspaces_thin_client.types.desktop_type.serialize_json(
                value["desktop_type"]
            )
        )
    if "activation_code" in value:
        out["activationCode"] = value["activation_code"]
    if "registered_devices_count" in value:
        out["registeredDevicesCount"] = value["registered_devices_count"]
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
    if "pending_software_set_id" in value:
        out["pendingSoftwareSetId"] = value["pending_software_set_id"]
    if "pending_software_set_version" in value:
        out["pendingSoftwareSetVersion"] = value["pending_software_set_version"]
    if "software_set_compliance_status" in value:
        import capo_workspaces_thin_client.types.environment_software_set_compliance_status

        out["softwareSetComplianceStatus"] = (
            capo_workspaces_thin_client.types.environment_software_set_compliance_status.serialize_json(
                value["software_set_compliance_status"]
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
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "device_creation_tags" in value:
        import capo_workspaces_thin_client.types.device_creation_tags_map

        out["deviceCreationTags"] = (
            capo_workspaces_thin_client.types.device_creation_tags_map.serialize_json(
                value["device_creation_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("desktopArn") is not None:
        out["desktop_arn"] = data["desktopArn"]
    if data.get("desktopEndpoint") is not None:
        out["desktop_endpoint"] = data["desktopEndpoint"]
    if data.get("desktopType") is not None:
        import capo_workspaces_thin_client.types.desktop_type

        out["desktop_type"] = (
            capo_workspaces_thin_client.types.desktop_type.deserialize_json(
                data["desktopType"]
            )
        )
    if data.get("activationCode") is not None:
        out["activation_code"] = data["activationCode"]
    if data.get("registeredDevicesCount") is not None:
        out["registered_devices_count"] = data["registeredDevicesCount"]
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
    if data.get("pendingSoftwareSetId") is not None:
        out["pending_software_set_id"] = data["pendingSoftwareSetId"]
    if data.get("pendingSoftwareSetVersion") is not None:
        out["pending_software_set_version"] = data["pendingSoftwareSetVersion"]
    if data.get("softwareSetComplianceStatus") is not None:
        import capo_workspaces_thin_client.types.environment_software_set_compliance_status

        out["software_set_compliance_status"] = (
            capo_workspaces_thin_client.types.environment_software_set_compliance_status.deserialize_json(
                data["softwareSetComplianceStatus"]
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
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("deviceCreationTags") is not None:
        import capo_workspaces_thin_client.types.device_creation_tags_map

        out["device_creation_tags"] = (
            capo_workspaces_thin_client.types.device_creation_tags_map.deserialize_json(
                data["deviceCreationTags"]
            )
        )
    return out


def redact_sensitive(value: Environment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "desktop_endpoint" in value:
        out["desktop_endpoint"] = "*** Sensitive Data Redacted ***"
    if "activation_code" in value:
        out["activation_code"] = "*** Sensitive Data Redacted ***"
    if "device_creation_tags" in value:
        out["device_creation_tags"] = "*** Sensitive Data Redacted ***"
    return out
