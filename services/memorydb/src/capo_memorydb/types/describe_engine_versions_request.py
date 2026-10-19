"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeEngineVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.boolean
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeEngineVersionsRequest(TypedDict, closed=True):
    engine: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the engine for which to list available versions.</p>"""
    engine_version: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Redis OSS engine version</p>"""
    parameter_group_family: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of a specific parameter group family to return details for.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    default_only: NotRequired["capo_memorydb.types.boolean.Boolean"]
    """<p>If true, specifies that only the default version of the specified engine or engine and major version combination is to be returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEngineVersionsRequest) -> dict:
    out: dict = {}
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "parameter_group_family" in value:
        out["ParameterGroupFamily"] = value["parameter_group_family"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "default_only" in value:
        out["DefaultOnly"] = value["default_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEngineVersionsRequest:
    out: DescribeEngineVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("ParameterGroupFamily") is not None:
        out["parameter_group_family"] = data["ParameterGroupFamily"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("DefaultOnly") is not None:
        out["default_only"] = data["DefaultOnly"]
    return out
