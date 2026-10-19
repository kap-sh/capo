"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ResourceLink``."""

from typing_extensions import NotRequired, TypedDict


class ResourceLink(TypedDict, closed=True):
    url: "str"
    """<p>The URL of the external reference.</p>"""
    title: NotRequired["str"]
    """<p>An optional human-readable title for the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLink) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "title" in value:
        out["title"] = value["title"]
    return out


def deserialize_json(data: dict) -> ResourceLink:
    out: ResourceLink = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    return out
