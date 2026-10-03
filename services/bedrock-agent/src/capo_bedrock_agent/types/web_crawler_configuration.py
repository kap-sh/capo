"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebCrawlerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.filter_list
    import capo_bedrock_agent.types.user_agent
    import capo_bedrock_agent.types.user_agent_header
    import capo_bedrock_agent.types.web_crawler_limits
    import capo_bedrock_agent.types.web_scope_type


class WebCrawlerConfiguration(TypedDict, closed=True):
    crawler_limits: NotRequired[
        "capo_bedrock_agent.types.web_crawler_limits.WebCrawlerLimits"
    ]
    """<p>The configuration of crawl limits for the web URLs.</p>"""
    inclusion_filters: NotRequired["capo_bedrock_agent.types.filter_list.FilterList"]
    """<p>A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.</p>"""
    exclusion_filters: NotRequired["capo_bedrock_agent.types.filter_list.FilterList"]
    """<p>A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.</p>"""
    scope: NotRequired["capo_bedrock_agent.types.web_scope_type.WebScopeType"]
    """<p>The scope of what is crawled for your URLs.</p> <p>You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL "https://docs.aws.amazon.com/bedrock/latest/userguide/" and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain "aws.amazon.com" can also include sub domain "docs.aws.amazon.com".</p>"""
    user_agent: NotRequired["capo_bedrock_agent.types.user_agent.UserAgent"]
    """<p>Returns the user agent suffix for your web crawler.</p>"""
    user_agent_header: NotRequired[
        "capo_bedrock_agent.types.user_agent_header.UserAgentHeader"
    ]
    """<p>A string used for identifying the crawler or bot when it accesses a web server. The user agent header value consists of the <code>bedrockbot</code>, UUID, and a user agent suffix for your crawler (if one is provided). By default, it is set to <code>bedrockbot_UUID</code>. You can optionally append a custom suffix to <code>bedrockbot_UUID</code> to allowlist a specific user agent permitted to access your source URLs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebCrawlerConfiguration) -> dict:
    out: dict = {}
    if "crawler_limits" in value:
        import capo_bedrock_agent.types.web_crawler_limits

        out["crawlerLimits"] = (
            capo_bedrock_agent.types.web_crawler_limits.serialize_json(
                value["crawler_limits"]
            )
        )
    if "inclusion_filters" in value:
        import capo_bedrock_agent.types.filter_list

        out["inclusionFilters"] = capo_bedrock_agent.types.filter_list.serialize_json(
            value["inclusion_filters"]
        )
    if "exclusion_filters" in value:
        import capo_bedrock_agent.types.filter_list

        out["exclusionFilters"] = capo_bedrock_agent.types.filter_list.serialize_json(
            value["exclusion_filters"]
        )
    if "scope" in value:
        import capo_bedrock_agent.types.web_scope_type

        out["scope"] = capo_bedrock_agent.types.web_scope_type.serialize_json(
            value["scope"]
        )
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    if "user_agent_header" in value:
        out["userAgentHeader"] = value["user_agent_header"]
    return out


def deserialize_json(data: dict) -> WebCrawlerConfiguration:
    out: WebCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("crawlerLimits") is not None:
        import capo_bedrock_agent.types.web_crawler_limits

        out["crawler_limits"] = (
            capo_bedrock_agent.types.web_crawler_limits.deserialize_json(
                data["crawlerLimits"]
            )
        )
    if data.get("inclusionFilters") is not None:
        import capo_bedrock_agent.types.filter_list

        out["inclusion_filters"] = (
            capo_bedrock_agent.types.filter_list.deserialize_json(
                data["inclusionFilters"]
            )
        )
    if data.get("exclusionFilters") is not None:
        import capo_bedrock_agent.types.filter_list

        out["exclusion_filters"] = (
            capo_bedrock_agent.types.filter_list.deserialize_json(
                data["exclusionFilters"]
            )
        )
    if data.get("scope") is not None:
        import capo_bedrock_agent.types.web_scope_type

        out["scope"] = capo_bedrock_agent.types.web_scope_type.deserialize_json(
            data["scope"]
        )
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    if data.get("userAgentHeader") is not None:
        out["user_agent_header"] = data["userAgentHeader"]
    return out
