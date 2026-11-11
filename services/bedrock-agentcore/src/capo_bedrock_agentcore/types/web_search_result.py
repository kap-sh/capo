"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#WebSearchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.date_timestamp


class WebSearchResult(TypedDict, closed=True):
    title: NotRequired["str"]
    """<p>The title of the page.</p>"""
    url: NotRequired["str"]
    """<p>The URL of the page.</p>"""
    text: "str"
    """<p>A text extract from the page.</p>"""
    published_at: NotRequired[
        "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time the page was published. This field is absent when the publication time is not known.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebSearchResult) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "url" in value:
        out["url"] = value["url"]
    out["text"] = value["text"]
    if "published_at" in value:
        import capo_bedrock_agentcore.types.date_timestamp

        out["publishedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
            value["published_at"]
        )
    return out


def deserialize_json(data: dict) -> WebSearchResult:
    out: WebSearchResult = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("publishedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["published_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["publishedAt"]
            )
        )
    return out
