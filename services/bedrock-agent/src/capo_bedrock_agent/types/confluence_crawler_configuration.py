"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceCrawlerConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.crawl_filter_configuration


class ConfluenceCrawlerConfiguration(TypedDict, closed=True):
    filter_configuration: NotRequired[
        "capo_bedrock_agent.types.crawl_filter_configuration.CrawlFilterConfiguration"
    ]
    """<p>The configuration of filtering the Confluence content. For example, configuring regular expression patterns to include or exclude certain content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceCrawlerConfiguration) -> dict:
    out: dict = {}
    if "filter_configuration" in value:
        import capo_bedrock_agent.types.crawl_filter_configuration

        out["filterConfiguration"] = (
            capo_bedrock_agent.types.crawl_filter_configuration.serialize_json(
                value["filter_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfluenceCrawlerConfiguration:
    out: ConfluenceCrawlerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("filterConfiguration") is not None:
        import capo_bedrock_agent.types.crawl_filter_configuration

        out["filter_configuration"] = (
            capo_bedrock_agent.types.crawl_filter_configuration.deserialize_json(
                data["filterConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ConfluenceCrawlerConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_configuration" in value:
        import capo_bedrock_agent.types.crawl_filter_configuration

        out["filter_configuration"] = (
            capo_bedrock_agent.types.crawl_filter_configuration.redact_sensitive(
                value["filter_configuration"]
            )
        )
    return out
