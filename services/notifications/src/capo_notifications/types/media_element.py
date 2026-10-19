"""Generated from Smithy shape ``com.amazonaws.notifications#MediaElement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.media_element_type
    import capo_notifications.types.media_id
    import capo_notifications.types.text_part_reference
    import capo_notifications.types.url


class MediaElement(TypedDict, closed=True):
    media_id: "capo_notifications.types.media_id.MediaId"
    """<p>The unique ID for the media.</p>"""
    type: "capo_notifications.types.media_element_type.MediaElementType"
    """<p>The type of media.</p>"""
    url: "capo_notifications.types.url.Url"
    """<p>The URL of the media.</p>"""
    caption: "capo_notifications.types.text_part_reference.TextPartReference"
    """<p>The caption of the media.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaElement) -> dict:
    out: dict = {}
    out["mediaId"] = value["media_id"]
    out["type"] = value["type"]
    out["url"] = value["url"]
    out["caption"] = value["caption"]
    return out


def deserialize_json(data: dict) -> MediaElement:
    out: MediaElement = {}  # type: ignore[typeddict-item]
    if data.get("mediaId") is not None:
        out["media_id"] = data["mediaId"]
    else:
        out["media_id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("caption") is not None:
        out["caption"] = data["caption"]
    else:
        out["caption"] = ""
    return out
