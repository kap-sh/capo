"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeACLsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeACLsRequest(TypedDict, closed=True):
    acl_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the ACL.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeACLsRequest) -> dict:
    out: dict = {}
    if "acl_name" in value:
        out["ACLName"] = value["acl_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeACLsRequest:
    out: DescribeACLsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ACLName") is not None:
        out["acl_name"] = data["ACLName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeACLsRequest) -> dict:
    out: dict = {}
    if "acl_name" in value:
        out["ACLName"] = value["acl_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeACLsRequest:
    out: DescribeACLsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ACLName") is not None:
        out["acl_name"] = data["ACLName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
