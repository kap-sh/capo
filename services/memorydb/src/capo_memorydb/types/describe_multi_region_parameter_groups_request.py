"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionParameterGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeMultiRegionParameterGroupsRequest(TypedDict, closed=True):
    multi_region_parameter_group_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The request for information on a specific multi-region parameter group.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionParameterGroupsRequest) -> dict:
    out: dict = {}
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionParameterGroupsRequest:
    out: DescribeMultiRegionParameterGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMultiRegionParameterGroupsRequest) -> dict:
    out: dict = {}
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeMultiRegionParameterGroupsRequest:
    out: DescribeMultiRegionParameterGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionParameterGroupName") is not None:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
