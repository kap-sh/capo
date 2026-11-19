"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDirectoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_ids
    import capo_directory_service.types.limit
    import capo_directory_service.types.next_token


class DescribeDirectoriesRequest(TypedDict, closed=True):
    directory_ids: NotRequired[
        "capo_directory_service.types.directory_ids.DirectoryIds"
    ]
    """<p>A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <code>DescribeDirectoriesResult.NextToken</code> value from a previous call to <a>DescribeDirectories</a>. Pass null if this is the first call.</p>"""
    limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoriesRequest) -> dict:
    out: dict = {}
    if "directory_ids" in value:
        import capo_directory_service.types.directory_ids

        out["DirectoryIds"] = (
            capo_directory_service.types.directory_ids.serialize_aws_json_1_1(
                value["directory_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoriesRequest:
    out: DescribeDirectoriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryIds") is not None:
        import capo_directory_service.types.directory_ids

        out["directory_ids"] = (
            capo_directory_service.types.directory_ids.deserialize_aws_json_1_1(
                data["DirectoryIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectoriesRequest) -> dict:
    out: dict = {}
    if "directory_ids" in value:
        import capo_directory_service.types.directory_ids

        out["DirectoryIds"] = capo_directory_service.types.directory_ids.serialize_cbor(
            value["directory_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_cbor(data: dict) -> DescribeDirectoriesRequest:
    out: DescribeDirectoriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryIds") is not None:
        import capo_directory_service.types.directory_ids

        out["directory_ids"] = (
            capo_directory_service.types.directory_ids.deserialize_cbor(
                data["DirectoryIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
