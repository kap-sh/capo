"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeParameterGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.parameter_group_list
    import capo_memorydb.types.string


class DescribeParameterGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    parameter_groups: NotRequired[
        "capo_memorydb.types.parameter_group_list.ParameterGroupList"
    ]
    """<p>A list of parameter groups. Each element in the list contains detailed information about one parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParameterGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameter_groups" in value:
        import capo_memorydb.types.parameter_group_list

        out["ParameterGroups"] = (
            capo_memorydb.types.parameter_group_list.serialize_aws_json_1_1(
                value["parameter_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParameterGroupsResponse:
    out: DescribeParameterGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ParameterGroups") is not None:
        import capo_memorydb.types.parameter_group_list

        out["parameter_groups"] = (
            capo_memorydb.types.parameter_group_list.deserialize_aws_json_1_1(
                data["ParameterGroups"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeParameterGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameter_groups" in value:
        import capo_memorydb.types.parameter_group_list

        out["ParameterGroups"] = (
            capo_memorydb.types.parameter_group_list.serialize_cbor(
                value["parameter_groups"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeParameterGroupsResponse:
    out: DescribeParameterGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ParameterGroups") is not None:
        import capo_memorydb.types.parameter_group_list

        out["parameter_groups"] = (
            capo_memorydb.types.parameter_group_list.deserialize_cbor(
                data["ParameterGroups"]
            )
        )
    return out
