"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeSubnetGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string
    import capo_memorydb.types.subnet_group_list


class DescribeSubnetGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    subnet_groups: NotRequired["capo_memorydb.types.subnet_group_list.SubnetGroupList"]
    """<p>A list of subnet groups. Each element in the list contains detailed information about one group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubnetGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "subnet_groups" in value:
        import capo_memorydb.types.subnet_group_list

        out["SubnetGroups"] = (
            capo_memorydb.types.subnet_group_list.serialize_aws_json_1_1(
                value["subnet_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubnetGroupsResponse:
    out: DescribeSubnetGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SubnetGroups") is not None:
        import capo_memorydb.types.subnet_group_list

        out["subnet_groups"] = (
            capo_memorydb.types.subnet_group_list.deserialize_aws_json_1_1(
                data["SubnetGroups"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSubnetGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "subnet_groups" in value:
        import capo_memorydb.types.subnet_group_list

        out["SubnetGroups"] = capo_memorydb.types.subnet_group_list.serialize_cbor(
            value["subnet_groups"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeSubnetGroupsResponse:
    out: DescribeSubnetGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SubnetGroups") is not None:
        import capo_memorydb.types.subnet_group_list

        out["subnet_groups"] = capo_memorydb.types.subnet_group_list.deserialize_cbor(
            data["SubnetGroups"]
        )
    return out
