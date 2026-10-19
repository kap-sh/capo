"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.purchase_option_filter_type
    import capo_marketplace_discovery.types.purchase_option_filter_value_list


class PurchaseOptionFilter(TypedDict, closed=True):
    filter_type: "capo_marketplace_discovery.types.purchase_option_filter_type.PurchaseOptionFilterType"
    """<p>The type of filter to apply, such as <code>PRODUCT_ID</code>, <code>VISIBILITY_SCOPE</code>, or <code>PURCHASE_OPTION_TYPE</code>.</p>"""
    filter_values: "capo_marketplace_discovery.types.purchase_option_filter_value_list.PurchaseOptionFilterValueList"
    """<p>The values to filter by. Supported values depend on <code>filterType</code>:</p> <ul> <li> <p> <code>PRODUCT_ID</code> – One or more product identifiers to filter by.</p> </li> <li> <p> <code>SELLER_OF_RECORD_PROFILE_ID</code> – One or more seller profile identifiers to filter by.</p> </li> <li> <p> <code>PURCHASE_OPTION_TYPE</code> – One or more purchase option types to filter by: <code>OFFER</code> or <code>OFFERSET</code>.</p> </li> <li> <p> <code>VISIBILITY_SCOPE</code> – The visibility scope to filter by: <code>PRIVATE</code>.</p> </li> <li> <p> <code>AVAILABILITY_STATUS</code> – One or more availability statuses to filter by: <code>AVAILABLE</code> or <code>EXPIRED</code>.</p> </li> </ul> <p>To retrieve private offers and offer sets visible to you, use <code>VISIBILITY_SCOPE</code> with <code>PRIVATE</code>. OR logic combines multiple values within the same filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionFilter) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.purchase_option_filter_type

    out["filterType"] = (
        capo_marketplace_discovery.types.purchase_option_filter_type.serialize_json(
            value["filter_type"]
        )
    )
    import capo_marketplace_discovery.types.purchase_option_filter_value_list

    out["filterValues"] = (
        capo_marketplace_discovery.types.purchase_option_filter_value_list.serialize_json(
            value["filter_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> PurchaseOptionFilter:
    out: PurchaseOptionFilter = {}  # type: ignore[typeddict-item]
    if data.get("filterType") is not None:
        import capo_marketplace_discovery.types.purchase_option_filter_type

        out["filter_type"] = (
            capo_marketplace_discovery.types.purchase_option_filter_type.deserialize_json(
                data["filterType"]
            )
        )
    else:
        import typing

        out["filter_type"] = typing.cast(
            "capo_marketplace_discovery.types.purchase_option_filter_type.PurchaseOptionFilterType",
            "",
        )
    if data.get("filterValues") is not None:
        import capo_marketplace_discovery.types.purchase_option_filter_value_list

        out["filter_values"] = (
            capo_marketplace_discovery.types.purchase_option_filter_value_list.deserialize_json(
                data["filterValues"]
            )
        )
    else:
        out["filter_values"] = []
    return out
