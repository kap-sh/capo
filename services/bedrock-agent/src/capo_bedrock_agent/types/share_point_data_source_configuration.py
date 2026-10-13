"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointDataSourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.share_point_crawler_configuration
    import capo_bedrock_agent.types.share_point_source_configuration


class SharePointDataSourceConfiguration(TypedDict, closed=True):
    source_configuration: "capo_bedrock_agent.types.share_point_source_configuration.SharePointSourceConfiguration"
    """<p>The endpoint information to connect to your SharePoint data source.</p>"""
    crawler_configuration: NotRequired[
        "capo_bedrock_agent.types.share_point_crawler_configuration.SharePointCrawlerConfiguration"
    ]
    """<p>The configuration of the SharePoint content. For example, configuring specific types of SharePoint content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePointDataSourceConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.share_point_source_configuration

    out["sourceConfiguration"] = (
        capo_bedrock_agent.types.share_point_source_configuration.serialize_json(
            value["source_configuration"]
        )
    )
    if "crawler_configuration" in value:
        import capo_bedrock_agent.types.share_point_crawler_configuration

        out["crawlerConfiguration"] = (
            capo_bedrock_agent.types.share_point_crawler_configuration.serialize_json(
                value["crawler_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SharePointDataSourceConfiguration:
    out: SharePointDataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceConfiguration") is not None:
        import capo_bedrock_agent.types.share_point_source_configuration

        out["source_configuration"] = (
            capo_bedrock_agent.types.share_point_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SharePointDataSourceConfiguration.source_configuration required"
        )
    if data.get("crawlerConfiguration") is not None:
        import capo_bedrock_agent.types.share_point_crawler_configuration

        out["crawler_configuration"] = (
            capo_bedrock_agent.types.share_point_crawler_configuration.deserialize_json(
                data["crawlerConfiguration"]
            )
        )
    return out


def redact_sensitive(value: SharePointDataSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "crawler_configuration" in value:
        import capo_bedrock_agent.types.share_point_crawler_configuration

        out["crawler_configuration"] = (
            capo_bedrock_agent.types.share_point_crawler_configuration.redact_sensitive(
                value["crawler_configuration"]
            )
        )
    return out
