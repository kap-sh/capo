"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_sort_by
    import capo_marketplace_catalog.types.sort_order


class ExpressPrivateOfferConfigurationSort(TypedDict, closed=True):
    sort_by: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_sort_by.ExpressPrivateOfferConfigurationSortBy"
    ]
    """<p>The field to sort by. Valid values are <code>EntityId</code>, <code>LastModifiedDate</code>, <code>ProductId</code>, and <code>State</code>.</p>"""
    sort_order: NotRequired["capo_marketplace_catalog.types.sort_order.SortOrder"]
    """<p>The sorting order. Valid values are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationSort) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_sort_by

        out["SortBy"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_marketplace_catalog.types.sort_order

        out["SortOrder"] = capo_marketplace_catalog.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> ExpressPrivateOfferConfigurationSort:
    out: ExpressPrivateOfferConfigurationSort = {}  # type: ignore[typeddict-item]
    if data.get("SortBy") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_sort_by

        out["sort_by"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_sort_by.deserialize_json(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_marketplace_catalog.types.sort_order

        out["sort_order"] = capo_marketplace_catalog.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    return out
