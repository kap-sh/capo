"""Generated from Smithy shape ``com.amazonaws.securityhub#KbArticle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class KbArticle(TypedDict, closed=True):
    title: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The title of the <code>KbArticle</code>.</p>"""
    url: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URL of the <code>KbArticle</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KbArticle) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> KbArticle:
    out: KbArticle = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
