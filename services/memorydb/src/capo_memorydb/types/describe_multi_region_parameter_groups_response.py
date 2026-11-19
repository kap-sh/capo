"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionParameterGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.multi_region_parameter_group_list
    import capo_memorydb.types.string


class DescribeMultiRegionParameterGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional token to include in the response. If this token is provided, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""
    multi_region_parameter_groups: NotRequired[
        "capo_memorydb.types.multi_region_parameter_group_list.MultiRegionParameterGroupList"
    ]
    """<p>A list of multi-region parameter groups. Each element in the list contains detailed information about one parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionParameterGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multi_region_parameter_groups" in value:
        import capo_memorydb.types.multi_region_parameter_group_list

        out["MultiRegionParameterGroups"] = (
            capo_memorydb.types.multi_region_parameter_group_list.serialize_aws_json_1_1(
                value["multi_region_parameter_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionParameterGroupsResponse:
    out: DescribeMultiRegionParameterGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MultiRegionParameterGroups") is not None:
        import capo_memorydb.types.multi_region_parameter_group_list

        out["multi_region_parameter_groups"] = (
            capo_memorydb.types.multi_region_parameter_group_list.deserialize_aws_json_1_1(
                data["MultiRegionParameterGroups"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMultiRegionParameterGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multi_region_parameter_groups" in value:
        import capo_memorydb.types.multi_region_parameter_group_list

        out["MultiRegionParameterGroups"] = (
            capo_memorydb.types.multi_region_parameter_group_list.serialize_cbor(
                value["multi_region_parameter_groups"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeMultiRegionParameterGroupsResponse:
    out: DescribeMultiRegionParameterGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MultiRegionParameterGroups") is not None:
        import capo_memorydb.types.multi_region_parameter_group_list

        out["multi_region_parameter_groups"] = (
            capo_memorydb.types.multi_region_parameter_group_list.deserialize_cbor(
                data["MultiRegionParameterGroups"]
            )
        )
    return out
