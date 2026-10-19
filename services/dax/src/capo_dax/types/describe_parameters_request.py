"""Generated from Smithy shape ``com.amazonaws.dax#DescribeParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.integer_optional
    import capo_dax.types.string


class DescribeParametersRequest(TypedDict, closed=True):
    parameter_group_name: "capo_dax.types.string.String"
    """<p>The name of the parameter group.</p>"""
    source: NotRequired["capo_dax.types.string.String"]
    """<p>How the parameter is defined. For example, <code>system</code> denotes a system-defined parameter.</p>"""
    max_results: NotRequired["capo_dax.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of results to include in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p> <p>The value for <code>MaxResults</code> must be between 20 and 100.</p>"""
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by <code>MaxResults</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParametersRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    if "source" in value:
        out["Source"] = value["source"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParametersRequest:
    out: DescribeParametersRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        out["parameter_group_name"] = ""
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
