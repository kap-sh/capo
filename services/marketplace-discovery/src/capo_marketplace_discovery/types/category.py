"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Category``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string


class Category(TypedDict, closed=True):
    category_id: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The machine-readable identifier of the category.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> dict:
    out: dict = {}
    out["categoryId"] = value["category_id"]
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if data.get("categoryId") is not None:
        out["category_id"] = data["categoryId"]
    else:
        out["category_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    return out
