"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#WebSearchFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.domain_filter
    import capo_bedrock_agentcore.types.published_date_filter


class WebSearchFilters(TypedDict, closed=True):
    domain_filter: NotRequired[
        "capo_bedrock_agentcore.types.domain_filter.DomainFilter"
    ]
    """<p>The domains to include in or exclude from the results.</p>"""
    published_date_filter: NotRequired[
        "capo_bedrock_agentcore.types.published_date_filter.PublishedDateFilter"
    ]
    """<p>The publication time range of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebSearchFilters) -> dict:
    out: dict = {}
    if "domain_filter" in value:
        import capo_bedrock_agentcore.types.domain_filter

        out["domainFilter"] = capo_bedrock_agentcore.types.domain_filter.serialize_json(
            value["domain_filter"]
        )
    if "published_date_filter" in value:
        import capo_bedrock_agentcore.types.published_date_filter

        out["publishedDateFilter"] = (
            capo_bedrock_agentcore.types.published_date_filter.serialize_json(
                value["published_date_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> WebSearchFilters:
    out: WebSearchFilters = {}  # type: ignore[typeddict-item]
    if data.get("domainFilter") is not None:
        import capo_bedrock_agentcore.types.domain_filter

        out["domain_filter"] = (
            capo_bedrock_agentcore.types.domain_filter.deserialize_json(
                data["domainFilter"]
            )
        )
    if data.get("publishedDateFilter") is not None:
        import capo_bedrock_agentcore.types.published_date_filter

        out["published_date_filter"] = (
            capo_bedrock_agentcore.types.published_date_filter.deserialize_json(
                data["publishedDateFilter"]
            )
        )
    return out
