"""Generated from Smithy shape ``com.amazonaws.oam#ListLinksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_oam.types.list_links_items


class ListLinksOutput(TypedDict, closed=True):
    items: "capo_oam.types.list_links_items.ListLinksItems"
    """<p>An array of structures that contain the information about the returned links.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use when requesting the next set of links.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinksOutput) -> dict:
    out: dict = {}
    import capo_oam.types.list_links_items

    out["Items"] = capo_oam.types.list_links_items.serialize_json(value["items"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinksOutput:
    out: ListLinksOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_oam.types.list_links_items

        out["items"] = capo_oam.types.list_links_items.deserialize_json(data["Items"])
    else:
        out["items"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
