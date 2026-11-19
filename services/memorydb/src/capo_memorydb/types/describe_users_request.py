"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.filter_list
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string
    import capo_memorydb.types.user_name


class DescribeUsersRequest(TypedDict, closed=True):
    user_name: NotRequired["capo_memorydb.types.user_name.UserName"]
    """<p>The name of the user.</p>"""
    filters: NotRequired["capo_memorydb.types.filter_list.FilterList"]
    """<p>Filter to determine the list of users to return.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "filters" in value:
        import capo_memorydb.types.filter_list

        out["Filters"] = capo_memorydb.types.filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersRequest:
    out: DescribeUsersRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Filters") is not None:
        import capo_memorydb.types.filter_list

        out["filters"] = capo_memorydb.types.filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeUsersRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "filters" in value:
        import capo_memorydb.types.filter_list

        out["Filters"] = capo_memorydb.types.filter_list.serialize_cbor(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeUsersRequest:
    out: DescribeUsersRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Filters") is not None:
        import capo_memorydb.types.filter_list

        out["filters"] = capo_memorydb.types.filter_list.deserialize_cbor(
            data["Filters"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
