"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeDirectoryConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.directory_name_list
    import capo_appstream.types.integer
    import capo_appstream.types.string


class DescribeDirectoryConfigsRequest(TypedDict, closed=True):
    directory_names: NotRequired[
        "capo_appstream.types.directory_name_list.DirectoryNameList"
    ]
    """<p>The directory names.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDirectoryConfigsRequest) -> dict:
    out: dict = {}
    if "directory_names" in value:
        import capo_appstream.types.directory_name_list

        out["DirectoryNames"] = (
            capo_appstream.types.directory_name_list.serialize_aws_json_1_1(
                value["directory_names"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDirectoryConfigsRequest:
    out: DescribeDirectoryConfigsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryNames") is not None:
        import capo_appstream.types.directory_name_list

        out["directory_names"] = (
            capo_appstream.types.directory_name_list.deserialize_aws_json_1_1(
                data["DirectoryNames"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectoryConfigsRequest) -> dict:
    out: dict = {}
    if "directory_names" in value:
        import capo_appstream.types.directory_name_list

        out["DirectoryNames"] = capo_appstream.types.directory_name_list.serialize_cbor(
            value["directory_names"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeDirectoryConfigsRequest:
    out: DescribeDirectoryConfigsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryNames") is not None:
        import capo_appstream.types.directory_name_list

        out["directory_names"] = (
            capo_appstream.types.directory_name_list.deserialize_cbor(
                data["DirectoryNames"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
