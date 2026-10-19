"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GrantItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.dimension_label_list


class GrantItem(TypedDict, closed=True):
    dimension_key: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The machine-readable key identifying the entitlement dimension.</p>"""
    display_name: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The human-readable name of the entitlement dimension.</p>"""
    description: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>A description of the entitlement.</p>"""
    dimension_labels: NotRequired[
        "capo_marketplace_discovery.types.dimension_label_list.DimensionLabelList"
    ]
    """<p>Labels used to categorize this entitlement, such as by region.</p>"""
    unit: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The unit of measurement for the entitlement.</p>"""
    max_quantity: NotRequired["int"]
    """<p>The maximum quantity of the entitlement that can be granted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantItem) -> dict:
    out: dict = {}
    out["dimensionKey"] = value["dimension_key"]
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "dimension_labels" in value:
        import capo_marketplace_discovery.types.dimension_label_list

        out["dimensionLabels"] = (
            capo_marketplace_discovery.types.dimension_label_list.serialize_json(
                value["dimension_labels"]
            )
        )
    out["unit"] = value["unit"]
    if "max_quantity" in value:
        out["maxQuantity"] = value["max_quantity"]
    return out


def deserialize_json(data: dict) -> GrantItem:
    out: GrantItem = {}  # type: ignore[typeddict-item]
    if data.get("dimensionKey") is not None:
        out["dimension_key"] = data["dimensionKey"]
    else:
        out["dimension_key"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dimensionLabels") is not None:
        import capo_marketplace_discovery.types.dimension_label_list

        out["dimension_labels"] = (
            capo_marketplace_discovery.types.dimension_label_list.deserialize_json(
                data["dimensionLabels"]
            )
        )
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    else:
        out["unit"] = ""
    if data.get("maxQuantity") is not None:
        out["max_quantity"] = data["maxQuantity"]
    return out
