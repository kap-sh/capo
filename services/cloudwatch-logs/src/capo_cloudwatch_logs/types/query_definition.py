"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_names
    import capo_cloudwatch_logs.types.query_definition_name
    import capo_cloudwatch_logs.types.query_definition_string
    import capo_cloudwatch_logs.types.query_id
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_parameter_list
    import capo_cloudwatch_logs.types.timestamp


class QueryDefinition(TypedDict, closed=True):
    query_language: NotRequired[
        "capo_cloudwatch_logs.types.query_language.QueryLanguage"
    ]
    """<p>The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>"""
    query_definition_id: NotRequired["capo_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The unique ID of the query definition.</p>"""
    name: NotRequired[
        "capo_cloudwatch_logs.types.query_definition_name.QueryDefinitionName"
    ]
    """<p>The name of the query definition.</p>"""
    query_string: NotRequired[
        "capo_cloudwatch_logs.types.query_definition_string.QueryDefinitionString"
    ]
    """<p>The query string to use for this definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">CloudWatch Logs Insights Query Syntax</a>.</p>"""
    last_modified: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date that the query definition was most recently modified.</p>"""
    log_group_names: NotRequired[
        "capo_cloudwatch_logs.types.log_group_names.LogGroupNames"
    ]
    """<p>If this query definition contains a list of log groups that it is limited to, that list appears here.</p>"""
    parameters: NotRequired[
        "capo_cloudwatch_logs.types.query_parameter_list.QueryParameterList"
    ]
    """<p>If this query definition contains a list of query parameters that define placeholder variables for the query string, that list appears here.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryDefinition) -> dict:
    out: dict = {}
    if "query_language" in value:
        import capo_cloudwatch_logs.types.query_language

        out["queryLanguage"] = (
            capo_cloudwatch_logs.types.query_language.serialize_aws_json_1_1(
                value["query_language"]
            )
        )
    if "query_definition_id" in value:
        out["queryDefinitionId"] = value["query_definition_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "last_modified" in value:
        out["lastModified"] = value["last_modified"]
    if "log_group_names" in value:
        import capo_cloudwatch_logs.types.log_group_names

        out["logGroupNames"] = (
            capo_cloudwatch_logs.types.log_group_names.serialize_aws_json_1_1(
                value["log_group_names"]
            )
        )
    if "parameters" in value:
        import capo_cloudwatch_logs.types.query_parameter_list

        out["parameters"] = (
            capo_cloudwatch_logs.types.query_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryDefinition:
    out: QueryDefinition = {}  # type: ignore[typeddict-item]
    if data.get("queryLanguage") is not None:
        import capo_cloudwatch_logs.types.query_language

        out["query_language"] = (
            capo_cloudwatch_logs.types.query_language.deserialize_aws_json_1_1(
                data["queryLanguage"]
            )
        )
    if data.get("queryDefinitionId") is not None:
        out["query_definition_id"] = data["queryDefinitionId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("queryString") is not None:
        out["query_string"] = data["queryString"]
    if data.get("lastModified") is not None:
        out["last_modified"] = data["lastModified"]
    if data.get("logGroupNames") is not None:
        import capo_cloudwatch_logs.types.log_group_names

        out["log_group_names"] = (
            capo_cloudwatch_logs.types.log_group_names.deserialize_aws_json_1_1(
                data["logGroupNames"]
            )
        )
    if data.get("parameters") is not None:
        import capo_cloudwatch_logs.types.query_parameter_list

        out["parameters"] = (
            capo_cloudwatch_logs.types.query_parameter_list.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    return out
