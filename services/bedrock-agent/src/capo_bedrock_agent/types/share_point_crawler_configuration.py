"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointCrawlerConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.crawl_filter_configuration


class SharePointCrawlerConfiguration(TypedDict, closed=True):
    filter_configuration: NotRequired[
        "capo_bedrock_agent.types.crawl_filter_configuration.CrawlFilterConfiguration"
    ]
    """<p>The configuration of filtering the SharePoint content. For example, configuring regular expression patterns to include or exclude certain content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePointCrawlerConfiguration) -> dict:
    out: dict = {}
    if "filter_configuration" in value:
        import capo_bedrock_agent.types.crawl_filter_configuration

        out["filterConfiguration"] = (
            capo_bedrock_agent.types.crawl_filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SharePointCrawlerConfiguration:
    out: SharePointCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("filterConfiguration") is not None:
        import capo_bedrock_agent.types.crawl_filter_configuration

        out["filter_configuration"] = (
            capo_bedrock_agent.types.crawl_filter_configuration.deserialize_json(
                data["filterConfiguration"]
            )
        )
    return out


def redact_sensitive(value: SharePointCrawlerConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_configuration" in value:
        import capo_bedrock_agent.types.crawl_filter_configuration

        out["filter_configuration"] = (
            capo_bedrock_agent.types.crawl_filter_configuration.redact_sensitive(
                value["filter_configuration"]
            )
        )
    return out
