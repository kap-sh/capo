"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeUsersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.user_list


class DescribeUsersResponse(TypedDict, closed=True):
    users: NotRequired["capo_memorydb.types.user_list.UserList"]
    """<p>A list of users.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_memorydb.types.user_list

        out["Users"] = capo_memorydb.types.user_list.serialize_aws_json_1_1(
            value["users"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersResponse:
    out: DescribeUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_memorydb.types.user_list

        out["users"] = capo_memorydb.types.user_list.deserialize_aws_json_1_1(
            data["Users"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeUsersResponse) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_memorydb.types.user_list

        out["Users"] = capo_memorydb.types.user_list.serialize_cbor(value["users"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeUsersResponse:
    out: DescribeUsersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_memorydb.types.user_list

        out["users"] = capo_memorydb.types.user_list.deserialize_cbor(data["Users"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
