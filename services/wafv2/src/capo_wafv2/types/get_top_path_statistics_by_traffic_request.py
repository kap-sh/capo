"""Generated from Smithy shape ``com.amazonaws.wafv2#GetTopPathStatisticsByTrafficRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.filter_string
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.number_of_top_traffic_bots_per_path
    import capo_wafv2.types.path_statistics_limit
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.scope
    import capo_wafv2.types.time_window
    import capo_wafv2.types.uri_path_prefix_string


class GetTopPathStatisticsByTrafficRequest(TypedDict, closed=True):
    web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL for which you want to retrieve path statistics.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether the web ACL is for an Amazon Web Services CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer, an AppSync GraphQL API, an Amazon Cognito user pool, an Amazon Web Services App Runner service, or an Amazon Web Services Verified Access instance.</p>"""
    uri_path_prefix: NotRequired[
        "capo_wafv2.types.uri_path_prefix_string.UriPathPrefixString"
    ]
    """<p>A URI path prefix to filter the results. When you specify this parameter, the operation returns statistics for individual URIs within the specified path prefix. For example, if you specify <code>/api</code>, the response includes statistics for paths like <code>/api/v1/users</code> and <code>/api/v2/orders</code>. If you don't specify this parameter, the operation returns top-level path statistics.</p>"""
    time_window: "capo_wafv2.types.time_window.TimeWindow"
    """<p>The time window for which you want to retrieve path statistics. The time window must be within the data retention period for your web ACL.</p>"""
    bot_category: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>Filters the results to include only traffic from bots in the specified category. For example, you can filter by <code>ai</code> to see only AI crawler traffic, or <code>search_engine</code> to see only search engine bot traffic. When you apply this filter, the <code>Source</code> field is populated in the response.</p>"""
    bot_organization: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>Filters the results to include only traffic from bots belonging to the specified organization. For example, you can filter by <code>openai</code> or <code>google</code>. When you apply this filter, the <code>Source</code> field is populated in the response.</p>"""
    bot_name: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>Filters the results to include only traffic from the specified bot. For example, you can filter by <code>gptbot</code> or <code>googlebot</code>. When you apply this filter, the <code>Source</code> field is populated in the response.</p>"""
    limit: "capo_wafv2.types.path_statistics_limit.PathStatisticsLimit"
    """<p>The maximum number of path statistics to return. Valid values are 1 to 100.</p>"""
    number_of_top_traffic_bots_per_path: "capo_wafv2.types.number_of_top_traffic_bots_per_path.NumberOfTopTrafficBotsPerPath"
    """<p>The maximum number of top bots to include in the statistics for each path. Valid values are 1 to 10.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTopPathStatisticsByTrafficRequest) -> dict:
    out: dict = {}
    out["WebAclArn"] = value["web_acl_arn"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "uri_path_prefix" in value:
        out["UriPathPrefix"] = value["uri_path_prefix"]
    import capo_wafv2.types.time_window

    out["TimeWindow"] = capo_wafv2.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    if "bot_category" in value:
        out["BotCategory"] = value["bot_category"]
    if "bot_organization" in value:
        out["BotOrganization"] = value["bot_organization"]
    if "bot_name" in value:
        out["BotName"] = value["bot_name"]
    out["Limit"] = value["limit"]
    out["NumberOfTopTrafficBotsPerPath"] = value["number_of_top_traffic_bots_per_path"]
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTopPathStatisticsByTrafficRequest:
    out: GetTopPathStatisticsByTrafficRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebAclArn") is not None:
        out["web_acl_arn"] = data["WebAclArn"]
    else:
        out["web_acl_arn"] = ""
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("UriPathPrefix") is not None:
        out["uri_path_prefix"] = data["UriPathPrefix"]
    if data.get("TimeWindow") is not None:
        import capo_wafv2.types.time_window

        out["time_window"] = capo_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError(
            "GetTopPathStatisticsByTrafficRequest.time_window required"
        )
    if data.get("BotCategory") is not None:
        out["bot_category"] = data["BotCategory"]
    if data.get("BotOrganization") is not None:
        out["bot_organization"] = data["BotOrganization"]
    if data.get("BotName") is not None:
        out["bot_name"] = data["BotName"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if data.get("NumberOfTopTrafficBotsPerPath") is not None:
        out["number_of_top_traffic_bots_per_path"] = data[
            "NumberOfTopTrafficBotsPerPath"
        ]
    else:
        out["number_of_top_traffic_bots_per_path"] = 0
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
