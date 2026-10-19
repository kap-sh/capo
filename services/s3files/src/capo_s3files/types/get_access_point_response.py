"""Generated from Smithy shape ``com.amazonaws.s3files#GetAccessPointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.access_point_arn
    import capo_s3files.types.access_point_id
    import capo_s3files.types.aws_account_id
    import capo_s3files.types.client_token
    import capo_s3files.types.file_system_id
    import capo_s3files.types.life_cycle_state
    import capo_s3files.types.posix_user
    import capo_s3files.types.root_directory
    import capo_s3files.types.tag_list
    import capo_s3files.types.tag_value


class GetAccessPointResponse(TypedDict, closed=True):
    access_point_arn: "capo_s3files.types.access_point_arn.AccessPointArn"
    """<p>The ARN of the access point.</p>"""
    access_point_id: "capo_s3files.types.access_point_id.AccessPointId"
    """<p>The ID of the access point.</p>"""
    client_token: "capo_s3files.types.client_token.ClientToken"
    """<p>The client token used for idempotency when the access point was created.</p>"""
    file_system_id: "capo_s3files.types.file_system_id.FileSystemId"
    """<p>The ID of the S3 File System.</p>"""
    status: "capo_s3files.types.life_cycle_state.LifeCycleState"
    """<p>The current status of the access point.</p>"""
    owner_id: "capo_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the access point owner.</p>"""
    posix_user: NotRequired["capo_s3files.types.posix_user.PosixUser"]
    """<p>The POSIX identity configured for this access point.</p>"""
    root_directory: NotRequired["capo_s3files.types.root_directory.RootDirectory"]
    """<p>The root directory configuration for this access point.</p>"""
    tags: NotRequired["capo_s3files.types.tag_list.TagList"]
    """<p>The tags associated with the access point.</p>"""
    name: NotRequired["capo_s3files.types.tag_value.TagValue"]
    """<p>The name of the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessPointResponse) -> dict:
    out: dict = {}
    out["accessPointArn"] = value["access_point_arn"]
    out["accessPointId"] = value["access_point_id"]
    out["clientToken"] = value["client_token"]
    out["fileSystemId"] = value["file_system_id"]
    import capo_s3files.types.life_cycle_state

    out["status"] = capo_s3files.types.life_cycle_state.serialize_json(value["status"])
    out["ownerId"] = value["owner_id"]
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
    if "tags" in value:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.serialize_json(value["tags"])
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GetAccessPointResponse:
    out: GetAccessPointResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessPointArn") is not None:
        out["access_point_arn"] = data["accessPointArn"]
    else:
        out["access_point_arn"] = ""
    if data.get("accessPointId") is not None:
        out["access_point_id"] = data["accessPointId"]
    else:
        out["access_point_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        out["file_system_id"] = ""
    if data.get("status") is not None:
        import capo_s3files.types.life_cycle_state

        out["status"] = capo_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3files.types.life_cycle_state.LifeCycleState", ""
        )
    if data.get("ownerId") is not None:
        out["owner_id"] = data["ownerId"]
    else:
        out["owner_id"] = ""
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
    if data.get("tags") is not None:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.deserialize_json(data["tags"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
