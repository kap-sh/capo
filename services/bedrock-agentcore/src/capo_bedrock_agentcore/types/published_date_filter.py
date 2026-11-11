"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PublishedDateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.date_timestamp


class PublishedDateFilter(TypedDict, closed=True):
    published_after: NotRequired[
        "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The earliest publication time of the results, inclusive.</p>"""
    published_before: NotRequired[
        "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The latest publication time of the results, inclusive. A date without a time, such as one passed to the AWS CLI, means midnight UTC. To include a whole day, use the last second of that day, for example <code>2026-01-31T23:59:59Z</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishedDateFilter) -> dict:
    out: dict = {}
    if "published_after" in value:
        import capo_bedrock_agentcore.types.date_timestamp

        out["publishedAfter"] = (
            capo_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["published_after"]
            )
        )
    if "published_before" in value:
        import capo_bedrock_agentcore.types.date_timestamp

        out["publishedBefore"] = (
            capo_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["published_before"]
            )
        )
    return out


def deserialize_json(data: dict) -> PublishedDateFilter:
    out: PublishedDateFilter = {}  # type: ignore[typeddict-item]
    if data.get("publishedAfter") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["published_after"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["publishedAfter"]
            )
        )
    if data.get("publishedBefore") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["published_before"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["publishedBefore"]
            )
        )
    return out
