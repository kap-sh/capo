"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalEmbeddedImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.nullable_string
    import capo_marketplace_discovery.types.url


class PromotionalEmbeddedImage(TypedDict, closed=True):
    title: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The title displayed when hovering over the image.</p>"""
    url: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the image file.</p>"""
    description: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>An optional description of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalEmbeddedImage) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["url"] = value["url"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PromotionalEmbeddedImage:
    out: PromotionalEmbeddedImage = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
