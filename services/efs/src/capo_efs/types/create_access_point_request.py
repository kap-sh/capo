"""Generated from Smithy shape ``com.amazonaws.efs#CreateAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.client_token
    import capo_efs.types.file_system_id
    import capo_efs.types.posix_user
    import capo_efs.types.root_directory
    import capo_efs.types.tags


class CreateAccessPointRequest(TypedDict, closed=True):
    client_token: "capo_efs.types.client_token.ClientToken"
    """<p>A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.</p>"""
    tags: NotRequired["capo_efs.types.tags.Tags"]
    """<p>Creates tags associated with the access point. Each tag is a key-value pair, each key must be unique. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the EFS file system that the access point provides access to.</p>"""
    posix_user: NotRequired["capo_efs.types.posix_user.PosixUser"]
    """<p>The operating system user and group applied to all file system requests made using the access point.</p>"""
    root_directory: NotRequired["capo_efs.types.root_directory.RootDirectory"]
    """<p>Specifies the directory on the EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the <code>RootDirectory</code> > <code>Path</code> specified does not exist, Amazon EFS creates it and applies the <code>CreationInfo</code> settings when a client connects to an access point. When specifying a <code>RootDirectory</code>, you must provide the <code>Path</code>, and the <code>CreationInfo</code>.</p> <p>Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPointRequest) -> dict:
    out: dict = {}
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_efs.types.tags

        out["Tags"] = capo_efs.types.tags.serialize_json(value["tags"])
    out["FileSystemId"] = value["file_system_id"]
    if "posix_user" in value:
        import capo_efs.types.posix_user

        out["PosixUser"] = capo_efs.types.posix_user.serialize_json(value["posix_user"])
    if "root_directory" in value:
        import capo_efs.types.root_directory

        out["RootDirectory"] = capo_efs.types.root_directory.serialize_json(
            value["root_directory"]
        )
    return out


def deserialize_json(data: dict) -> CreateAccessPointRequest:
    out: CreateAccessPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateAccessPointRequest.client_token required")
    if data.get("Tags") is not None:
        import capo_efs.types.tags

        out["tags"] = capo_efs.types.tags.deserialize_json(data["Tags"])
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("CreateAccessPointRequest.file_system_id required")
    if data.get("PosixUser") is not None:
        import capo_efs.types.posix_user

        out["posix_user"] = capo_efs.types.posix_user.deserialize_json(
            data["PosixUser"]
        )
    if data.get("RootDirectory") is not None:
        import capo_efs.types.root_directory

        out["root_directory"] = capo_efs.types.root_directory.deserialize_json(
            data["RootDirectory"]
        )
    return out
