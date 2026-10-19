"""Generated from Smithy shape ``com.amazonaws.s3files#ListFileSystemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.bucket_arn


class ListFileSystemsRequest(TypedDict, closed=True):
    bucket: NotRequired["capo_s3files.types.bucket_arn.BucketArn"]
    """<p>Optional filter to list only file systems associated with the specified S3 bucket Amazon Resource Name (ARN). If provided, only file systems that provide access to this bucket will be returned in the response.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of file systems to return in a single response. If not specified, up to 100 file systems are returned.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token returned from a previous call to continue listing file systems.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFileSystemsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFileSystemsRequest:
    out: ListFileSystemsRequest = {}  # type: ignore[typeddict-item]
    return out
