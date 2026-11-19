"""Generated from Smithy shape ``com.amazonaws.datasync#FsxProtocolNfs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.nfs_mount_options


class FsxProtocolNfs(TypedDict, closed=True):
    mount_options: NotRequired["capo_datasync.types.nfs_mount_options.NfsMountOptions"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxProtocolNfs) -> dict:
    out: dict = {}
    if "mount_options" in value:
        import capo_datasync.types.nfs_mount_options

        out["MountOptions"] = (
            capo_datasync.types.nfs_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FsxProtocolNfs:
    out: FsxProtocolNfs = {}  # type: ignore[typeddict-item]
    if data.get("MountOptions") is not None:
        import capo_datasync.types.nfs_mount_options

        out["mount_options"] = (
            capo_datasync.types.nfs_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FsxProtocolNfs) -> dict:
    out: dict = {}
    if "mount_options" in value:
        import capo_datasync.types.nfs_mount_options

        out["MountOptions"] = capo_datasync.types.nfs_mount_options.serialize_cbor(
            value["mount_options"]
        )
    return out


def deserialize_cbor(data: dict) -> FsxProtocolNfs:
    out: FsxProtocolNfs = {}  # type: ignore[typeddict-item]
    if data.get("MountOptions") is not None:
        import capo_datasync.types.nfs_mount_options

        out["mount_options"] = capo_datasync.types.nfs_mount_options.deserialize_cbor(
            data["MountOptions"]
        )
    return out
