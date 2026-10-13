"""Generated from Smithy shape ``com.amazonaws.bedrockagent#WebDataSourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.web_crawler_configuration
    import capo_bedrock_agent.types.web_source_configuration


class WebDataSourceConfiguration(TypedDict, closed=True):
    source_configuration: (
        "capo_bedrock_agent.types.web_source_configuration.WebSourceConfiguration"
    )
    """<p>The source configuration details for the web data source.</p>"""
    crawler_configuration: NotRequired[
        "capo_bedrock_agent.types.web_crawler_configuration.WebCrawlerConfiguration"
    ]
    """<p>The Web Crawler configuration details for the web data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebDataSourceConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.web_source_configuration

    out["sourceConfiguration"] = (
        capo_bedrock_agent.types.web_source_configuration.serialize_json(
            value["source_configuration"]
        )
    )
    if "crawler_configuration" in value:
        import capo_bedrock_agent.types.web_crawler_configuration

        out["crawlerConfiguration"] = (
            capo_bedrock_agent.types.web_crawler_configuration.serialize_json(
                value["crawler_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WebDataSourceConfiguration:
    out: WebDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceConfiguration") is not None:
        import capo_bedrock_agent.types.web_source_configuration

        out["source_configuration"] = (
            capo_bedrock_agent.types.web_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "WebDataSourceConfiguration.source_configuration required"
        )
    if data.get("crawlerConfiguration") is not None:
        import capo_bedrock_agent.types.web_crawler_configuration

        out["crawler_configuration"] = (
            capo_bedrock_agent.types.web_crawler_configuration.deserialize_json(
                data["crawlerConfiguration"]
            )
        )
    return out


def redact_sensitive(value: WebDataSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "crawler_configuration" in value:
        import capo_bedrock_agent.types.web_crawler_configuration

        out["crawler_configuration"] = (
            capo_bedrock_agent.types.web_crawler_configuration.redact_sensitive(
                value["crawler_configuration"]
            )
        )
    return out
