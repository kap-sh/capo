"""Generated from Smithy shape ``com.amazonaws.fsx#Volume``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.administrative_actions
    import capo_fsx.types.creation_time
    import capo_fsx.types.file_system_id
    import capo_fsx.types.lifecycle_transition_reason
    import capo_fsx.types.ontap_volume_configuration
    import capo_fsx.types.open_zfs_volume_configuration
    import capo_fsx.types.resource_arn
    import capo_fsx.types.tags
    import capo_fsx.types.volume_id
    import capo_fsx.types.volume_lifecycle
    import capo_fsx.types.volume_name
    import capo_fsx.types.volume_type


class Volume(TypedDict, closed=True):
    creation_time: NotRequired["capo_fsx.types.creation_time.CreationTime"]
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    lifecycle: NotRequired["capo_fsx.types.volume_lifecycle.VolumeLifecycle"]
    """<p>The lifecycle status of the volume.</p> <ul> <li> <p> <code>AVAILABLE</code> - The volume is fully available for use.</p> </li> <li> <p> <code>CREATED</code> - The volume has been created.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the new volume.</p> </li> <li> <p> <code>DELETING</code> - Amazon FSx is deleting an existing volume.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx was unable to create the volume.</p> </li> <li> <p> <code>MISCONFIGURED</code> - The volume is in a failed but recoverable state.</p> </li> <li> <p> <code>PENDING</code> - Amazon FSx hasn't started creating the volume.</p> </li> </ul>"""
    name: NotRequired["capo_fsx.types.volume_name.VolumeName"]
    """<p>The name of the volume.</p>"""
    ontap_configuration: NotRequired[
        "capo_fsx.types.ontap_volume_configuration.OntapVolumeConfiguration"
    ]
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The system-generated, unique ID of the volume.</p>"""
    volume_type: NotRequired["capo_fsx.types.volume_type.VolumeType"]
    """<p>The type of the volume.</p>"""
    lifecycle_transition_reason: NotRequired[
        "capo_fsx.types.lifecycle_transition_reason.LifecycleTransitionReason"
    ]
    """<p>The reason why the volume lifecycle status changed.</p>"""
    administrative_actions: NotRequired[
        "capo_fsx.types.administrative_actions.AdministrativeActions"
    ]
    """<p>A list of administrative actions for the volume that are in process or waiting to be processed. Administrative actions describe changes to the volume that you have initiated using the <code>UpdateVolume</code> action.</p>"""
    open_zfs_configuration: NotRequired[
        "capo_fsx.types.open_zfs_volume_configuration.OpenZFSVolumeConfiguration"
    ]
    """<p>The configuration of an Amazon FSx for OpenZFS volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Volume) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_fsx.types.creation_time

        out["CreationTime"] = capo_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "lifecycle" in value:
        import capo_fsx.types.volume_lifecycle

        out["Lifecycle"] = capo_fsx.types.volume_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "ontap_configuration" in value:
        import capo_fsx.types.ontap_volume_configuration

        out["OntapConfiguration"] = (
            capo_fsx.types.ontap_volume_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "volume_type" in value:
        import capo_fsx.types.volume_type

        out["VolumeType"] = capo_fsx.types.volume_type.serialize_aws_json_1_1(
            value["volume_type"]
        )
    if "lifecycle_transition_reason" in value:
        import capo_fsx.types.lifecycle_transition_reason

        out["LifecycleTransitionReason"] = (
            capo_fsx.types.lifecycle_transition_reason.serialize_aws_json_1_1(
                value["lifecycle_transition_reason"]
            )
        )
    if "administrative_actions" in value:
        import capo_fsx.types.administrative_actions

        out["AdministrativeActions"] = (
            capo_fsx.types.administrative_actions.serialize_aws_json_1_1(
                value["administrative_actions"]
            )
        )
    if "open_zfs_configuration" in value:
        import capo_fsx.types.open_zfs_volume_configuration

        out["OpenZFSConfiguration"] = (
            capo_fsx.types.open_zfs_volume_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        import capo_fsx.types.creation_time

        out["creation_time"] = capo_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.volume_lifecycle

        out["lifecycle"] = capo_fsx.types.volume_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OntapConfiguration") is not None:
        import capo_fsx.types.ontap_volume_configuration

        out["ontap_configuration"] = (
            capo_fsx.types.ontap_volume_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    if data.get("VolumeType") is not None:
        import capo_fsx.types.volume_type

        out["volume_type"] = capo_fsx.types.volume_type.deserialize_aws_json_1_1(
            data["VolumeType"]
        )
    if data.get("LifecycleTransitionReason") is not None:
        import capo_fsx.types.lifecycle_transition_reason

        out["lifecycle_transition_reason"] = (
            capo_fsx.types.lifecycle_transition_reason.deserialize_aws_json_1_1(
                data["LifecycleTransitionReason"]
            )
        )
    if data.get("AdministrativeActions") is not None:
        import capo_fsx.types.administrative_actions

        out["administrative_actions"] = (
            capo_fsx.types.administrative_actions.deserialize_aws_json_1_1(
                data["AdministrativeActions"]
            )
        )
    if data.get("OpenZFSConfiguration") is not None:
        import capo_fsx.types.open_zfs_volume_configuration

        out["open_zfs_configuration"] = (
            capo_fsx.types.open_zfs_volume_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out


def redact_sensitive(value: Volume) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "administrative_actions" in value:
        import capo_fsx.types.administrative_actions

        out["administrative_actions"] = (
            capo_fsx.types.administrative_actions.redact_sensitive(
                value["administrative_actions"]
            )
        )
    return out
