"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingFacet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.non_negative_count
    import capo_marketplace_discovery.types.nullable_string


class ListingFacet(TypedDict, closed=True):
    value: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The internal value used for filtering when passed back in a search filter.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the facet value, suitable for display in a user interface.</p>"""
    parent: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>The parent facet value for hierarchical facets, such as subcategories.</p>"""
    count: "capo_marketplace_discovery.types.non_negative_count.NonNegativeCount"
    """<p>The number of listings matching this facet value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingFacet) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["displayName"] = value["display_name"]
    if "parent" in value:
        out["parent"] = value["parent"]
    out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ListingFacet:
    out: ListingFacet = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("parent") is not None:
        out["parent"] = data["parent"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    return out
