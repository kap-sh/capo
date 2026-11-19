"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationNfsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.nfs_mount_options
    import capo_datasync.types.on_prem_config
    import capo_datasync.types.time


class DescribeLocationNfsResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the NFS location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The URI of the NFS location.</p>"""
    on_prem_config: NotRequired["capo_datasync.types.on_prem_config.OnPremConfig"]
    mount_options: NotRequired["capo_datasync.types.nfs_mount_options.NfsMountOptions"]
    """<p>The mount options that DataSync uses to mount your NFS file server.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time when the NFS location was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationNfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
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
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationNfsResponse:
    out: DescribeLocationNfsResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
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
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeLocationNfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "on_prem_config" in value:
        import capo_datasync.types.on_prem_config

        out["OnPremConfig"] = capo_datasync.types.on_prem_config.serialize_cbor(
            value["on_prem_config"]
        )
    if "mount_options" in value:
        import capo_datasync.types.nfs_mount_options

        out["MountOptions"] = capo_datasync.types.nfs_mount_options.serialize_cbor(
            value["mount_options"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_cbor(
            value["creation_time"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeLocationNfsResponse:
    out: DescribeLocationNfsResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("OnPremConfig") is not None:
        import capo_datasync.types.on_prem_config

        out["on_prem_config"] = capo_datasync.types.on_prem_config.deserialize_cbor(
            data["OnPremConfig"]
        )
    if data.get("MountOptions") is not None:
        import capo_datasync.types.nfs_mount_options

        out["mount_options"] = capo_datasync.types.nfs_mount_options.deserialize_cbor(
            data["MountOptions"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_cbor(
            data["CreationTime"]
        )
    return out
