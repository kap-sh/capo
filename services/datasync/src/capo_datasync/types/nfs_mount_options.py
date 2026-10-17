"""Generated from Smithy shape ``com.amazonaws.datasync#NfsMountOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.nfs_version


class NfsMountOptions(TypedDict, closed=True):
    version: NotRequired["capo_datasync.types.nfs_version.NfsVersion"]
    """<p>Specifies the NFS version that you want DataSync to use when mounting your NFS share. If the server refuses to use the version specified, the task fails.</p> <p>You can specify the following options:</p> <ul> <li> <p> <code>AUTOMATIC</code> (default): DataSync chooses NFS version 4.1.</p> </li> <li> <p> <code>NFS3</code>: Stateless protocol version that allows for asynchronous writes on the server.</p> </li> <li> <p> <code>NFSv4_0</code>: Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.</p> </li> <li> <p> <code>NFSv4_1</code>: Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0.</p> </li> </ul> <note> <p>DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NfsMountOptions) -> dict:
    out: dict = {}
    if "version" in value:
        import capo_datasync.types.nfs_version

        out["Version"] = capo_datasync.types.nfs_version.serialize_aws_json_1_1(
            value["version"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NfsMountOptions:
    out: NfsMountOptions = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        import capo_datasync.types.nfs_version

        out["version"] = capo_datasync.types.nfs_version.deserialize_aws_json_1_1(
            data["Version"]
        )
    return out
