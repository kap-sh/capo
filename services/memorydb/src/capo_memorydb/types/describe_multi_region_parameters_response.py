"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionParametersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.multi_region_parameters_list
    import capo_memorydb.types.string


class DescribeMultiRegionParametersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional token to include in the response. If this token is provided, the response includes only results beyond the token, up to the value specified by MaxResults.</p>"""
    multi_region_parameters: NotRequired[
        "capo_memorydb.types.multi_region_parameters_list.MultiRegionParametersList"
    ]
    """<p>A list of parameters specific to a particular multi-region parameter group. Each element in the list contains detailed information about one parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionParametersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multi_region_parameters" in value:
        import capo_memorydb.types.multi_region_parameters_list

        out["MultiRegionParameters"] = (
            capo_memorydb.types.multi_region_parameters_list.serialize_aws_json_1_1(
                value["multi_region_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionParametersResponse:
    out: DescribeMultiRegionParametersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MultiRegionParameters") is not None:
        import capo_memorydb.types.multi_region_parameters_list

        out["multi_region_parameters"] = (
            capo_memorydb.types.multi_region_parameters_list.deserialize_aws_json_1_1(
                data["MultiRegionParameters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMultiRegionParametersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multi_region_parameters" in value:
        import capo_memorydb.types.multi_region_parameters_list

        out["MultiRegionParameters"] = (
            capo_memorydb.types.multi_region_parameters_list.serialize_cbor(
                value["multi_region_parameters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeMultiRegionParametersResponse:
    out: DescribeMultiRegionParametersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MultiRegionParameters") is not None:
        import capo_memorydb.types.multi_region_parameters_list

        out["multi_region_parameters"] = (
            capo_memorydb.types.multi_region_parameters_list.deserialize_cbor(
                data["MultiRegionParameters"]
            )
        )
    return out
