"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLookupTablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_lookup_tables_max_results
    import capo_cloudwatch_logs.types.lookup_table_name
    import capo_cloudwatch_logs.types.next_token


class DescribeLookupTablesRequest(TypedDict, closed=True):
    lookup_table_name_prefix: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_name.LookupTableName"
    ]
    """<p>A prefix to filter lookup tables by name. Only tables whose names start with this prefix are returned. If you don't specify a prefix, all tables in the account and Region are returned.</p>"""
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.describe_lookup_tables_max_results.DescribeLookupTablesMaxResults"
    ]
    """<p>The maximum number of lookup tables to return in the response. The default value is 50 and the maximum value is 100.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLookupTablesRequest) -> dict:
    out: dict = {}
    if "lookup_table_name_prefix" in value:
        out["lookupTableNamePrefix"] = value["lookup_table_name_prefix"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLookupTablesRequest:
    out: DescribeLookupTablesRequest = {}  # type: ignore[typeddict-item]
    if data.get("lookupTableNamePrefix") is not None:
        out["lookup_table_name_prefix"] = data["lookupTableNamePrefix"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
