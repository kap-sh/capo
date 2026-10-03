"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationNfsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.location_arn
    import capo_datasync.types.nfs_mount_options
    import capo_datasync.types.nfs_subdirectory
    import capo_datasync.types.on_prem_config
    import capo_datasync.types.server_hostname


class UpdateLocationNfsRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the NFS transfer location that you want to update.</p>"""
    subdirectory: NotRequired["capo_datasync.types.nfs_subdirectory.NfsSubdirectory"]
    """<p>Specifies the export path in your NFS file server that you want DataSync to mount.</p> <p>This path (or a subdirectory of the path) is where DataSync transfers data to or from. For information on configuring an export for DataSync, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html#accessing-nfs">Accessing NFS file servers</a>.</p>"""
    server_hostname: NotRequired["capo_datasync.types.server_hostname.ServerHostname"]
    """<p>Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.</p>"""
    on_prem_config: NotRequired["capo_datasync.types.on_prem_config.OnPremConfig"]
    mount_options: NotRequired["capo_datasync.types.nfs_mount_options.NfsMountOptions"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationNfsRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "server_hostname" in value:
        out["ServerHostname"] = value["server_hostname"]
    if "on_prem_config" in value:
        import capo_datasync.types.on_prem_config

        out["OnPremConfig"] = capo_datasync.types.on_prem_config.serialize_aws_json_1_1(
            value["on_prem_config"]
        )
    if "mount_options" in value:
        import capo_datasync.types.nfs_mount_options

        out["MountOptions"] = (
            capo_datasync.types.nfs_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationNfsRequest:
    out: UpdateLocationNfsRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError("UpdateLocationNfsRequest.location_arn required")
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("ServerHostname") is not None:
        out["server_hostname"] = data["ServerHostname"]
    if data.get("OnPremConfig") is not None:
        import capo_datasync.types.on_prem_config

        out["on_prem_config"] = (
            capo_datasync.types.on_prem_config.deserialize_aws_json_1_1(
                data["OnPremConfig"]
            )
        )
    if data.get("MountOptions") is not None:
        import capo_datasync.types.nfs_mount_options

        out["mount_options"] = (
            capo_datasync.types.nfs_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    return out
