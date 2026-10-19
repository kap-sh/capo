"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.url


class ImageLocation(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the image.</p>"""
    url: "capo_iotsitewise.types.url.Url"
    """<p>The URL where the image is available. The URL is valid for 15 minutes so that you can view and download the image</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLocation) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ImageLocation:
    out: ImageLocation = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    return out
