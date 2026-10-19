"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.search_filter_type
    import capo_marketplace_discovery.types.search_filter_value_list


class SearchFilter(TypedDict, closed=True):
    filter_type: "capo_marketplace_discovery.types.search_filter_type.SearchFilterType"
    """<p>The type of filter to apply.</p>"""
    filter_values: "capo_marketplace_discovery.types.search_filter_value_list.SearchFilterValueList"
    """<p>The values to filter by. Term filters accept multiple values (OR logic). Range filters (MIN/MAX_AVERAGE_CUSTOMER_RATING) accept a single value between 0.0 and 5.0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilter) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.search_filter_type

    out["filterType"] = (
        capo_marketplace_discovery.types.search_filter_type.serialize_json(
            value["filter_type"]
        )
    )
    import capo_marketplace_discovery.types.search_filter_value_list

    out["filterValues"] = (
        capo_marketplace_discovery.types.search_filter_value_list.serialize_json(
            value["filter_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("filterType") is not None:
        import capo_marketplace_discovery.types.search_filter_type

        out["filter_type"] = (
            capo_marketplace_discovery.types.search_filter_type.deserialize_json(
                data["filterType"]
            )
        )
    else:
        import typing

        out["filter_type"] = typing.cast(
            "capo_marketplace_discovery.types.search_filter_type.SearchFilterType", ""
        )
    if data.get("filterValues") is not None:
        import capo_marketplace_discovery.types.search_filter_value_list

        out["filter_values"] = (
            capo_marketplace_discovery.types.search_filter_value_list.deserialize_json(
                data["filterValues"]
            )
        )
    else:
        out["filter_values"] = []
    return out
