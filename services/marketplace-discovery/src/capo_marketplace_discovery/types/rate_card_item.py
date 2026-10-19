"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RateCardItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.dimension_label_list


class RateCardItem(TypedDict, closed=True):
    dimension_key: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The machine-readable key identifying the dimension being priced.</p>"""
    display_name: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The human-readable name of the dimension.</p>"""
    description: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>A description of the dimension being priced.</p>"""
    dimension_labels: NotRequired[
        "capo_marketplace_discovery.types.dimension_label_list.DimensionLabelList"
    ]
    """<p>Labels used to categorize this dimension, such as by region.</p>"""
    unit: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The unit of measurement for the dimension.</p>"""
    price: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The price per unit for the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RateCardItem) -> dict:
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
    out["price"] = value["price"]
    return out


def deserialize_json(data: dict) -> RateCardItem:
    out: RateCardItem = {}  # type: ignore[typeddict-item]
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
    if data.get("price") is not None:
        out["price"] = data["price"]
    else:
        out["price"] = ""
    return out
