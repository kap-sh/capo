"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeQueryDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.query_definition_name
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_list_max_results


class DescribeQueryDefinitionsRequest(TypedDict, closed=True):
    query_language: NotRequired[
        "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>"""
    query_definition_name_prefix: NotRequired[
        "capo_cloudwatch_logs.types.query_definition_name.QueryDefinitionName"
    ]
    """<p>Use this parameter to filter your results to only the query definitions that have names that start with the prefix you specify.</p>"""
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.query_list_max_results.QueryListMaxResults"
    ]
    """<p>Limits the number of returned query definitions to the specified number.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQueryDefinitionsRequest) -> dict:
    out: dict = {}
    if "query_language" in value:
        import capo_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            capo_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "query_definition_name_prefix" in value:
        out["queryDefinitionNamePrefix"] = value["query_definition_name_prefix"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQueryDefinitionsRequest:
    out: DescribeQueryDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryLanguage") is not None:
        import capo_cloudwatch_logs.types.query_language

        out["query_language"] = (
            capo_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if data.get("queryDefinitionNamePrefix") is not None:
        out["query_definition_name_prefix"] = data["queryDefinitionNamePrefix"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
