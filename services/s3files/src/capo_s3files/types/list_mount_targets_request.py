"""Generated from Smithy shape ``com.amazonaws.s3files#ListMountTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.access_point_id
    import capo_s3files.types.file_system_id


class ListMountTargetsRequest(TypedDict, closed=True):
    file_system_id: NotRequired["capo_s3files.types.file_system_id.FileSystemId"]
    """<p>Optional filter to list only mount targets associated with the specified S3 File System ID or Amazon Resource Name (ARN). If provided, only mount targets for this file system will be returned in the response.</p>"""
    access_point_id: NotRequired["capo_s3files.types.access_point_id.AccessPointId"]
    """<p>Optional filter to list only mount targets associated with the specified access point ID or Amazon Resource Name (ARN).</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of mount targets to return in a single response.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token returned from a previous call to continue listing mount targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMountTargetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMountTargetsRequest:
    out: ListMountTargetsRequest = {}  # type: ignore[typeddict-item]
    return out
