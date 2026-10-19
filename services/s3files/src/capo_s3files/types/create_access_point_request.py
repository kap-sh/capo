"""Generated from Smithy shape ``com.amazonaws.s3files#CreateAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.client_token
    import capo_s3files.types.file_system_id
    import capo_s3files.types.posix_user
    import capo_s3files.types.root_directory
    import capo_s3files.types.tag_list


class CreateAccessPointRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_s3files.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Web Services ignores the request, but does not return an error.</p>"""
    tags: NotRequired["capo_s3files.types.tag_list.TagList"]
    """<p>An array of key-value pairs to apply to the access point for resource tagging.</p>"""
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System.</p>"""
    posix_user: NotRequired["capo_s3files.types.posix_user.PosixUser"]
    """<p>The POSIX identity with uid, gid, and secondary group IDs for user enforcement when accessing the file system through this access point.</p>"""
    root_directory: NotRequired["capo_s3files.types.root_directory.RootDirectory"]
    """<p>The root directory path for the access point, with optional creation permissions for newly created directories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessPointRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.serialize_json(value["tags"])
    out["fileSystemId"] = value["file_system_id"]
    if "posix_user" in value:
        import capo_s3files.types.posix_user

        out["posixUser"] = capo_s3files.types.posix_user.serialize_json(
            value["posix_user"]
        )
    if "root_directory" in value:
        import capo_s3files.types.root_directory

        out["rootDirectory"] = capo_s3files.types.root_directory.serialize_json(
            value["root_directory"]
        )
    return out


def deserialize_json(data: dict) -> CreateAccessPointRequest:
    out: CreateAccessPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.deserialize_json(data["tags"])
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("posixUser") is not None:
        import capo_s3files.types.posix_user

        out["posix_user"] = capo_s3files.types.posix_user.deserialize_json(
            data["posixUser"]
        )
    if data.get("rootDirectory") is not None:
        import capo_s3files.types.root_directory

        out["root_directory"] = capo_s3files.types.root_directory.deserialize_json(
            data["rootDirectory"]
        )
    return out
