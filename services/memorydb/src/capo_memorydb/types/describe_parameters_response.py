"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeParametersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.parameters_list
    import capo_memorydb.types.string


class DescribeParametersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    parameters: NotRequired["capo_memorydb.types.parameters_list.ParametersList"]
    """<p>A list of parameters specific to a particular parameter group. Each element in the list contains detailed information about one parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParametersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameters" in value:
        import capo_memorydb.types.parameters_list

        out["Parameters"] = capo_memorydb.types.parameters_list.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParametersResponse:
    out: DescribeParametersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Parameters") is not None:
        import capo_memorydb.types.parameters_list

        out["parameters"] = (
            capo_memorydb.types.parameters_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeParametersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameters" in value:
        import capo_memorydb.types.parameters_list

        out["Parameters"] = capo_memorydb.types.parameters_list.serialize_cbor(
            value["parameters"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeParametersResponse:
    out: DescribeParametersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Parameters") is not None:
        import capo_memorydb.types.parameters_list

        out["parameters"] = capo_memorydb.types.parameters_list.deserialize_cbor(
            data["Parameters"]
        )
    return out
