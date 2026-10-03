"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#TabularConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.order_by_list
    import capo_iottwinmaker.types.property_filters


class TabularConditions(TypedDict, closed=True):
    order_by: NotRequired["capo_iottwinmaker.types.order_by_list.OrderByList"]
    """<p>Filter criteria that orders the output. It can be sorted in ascending or descending order.</p>"""
    property_filters: NotRequired[
        "capo_iottwinmaker.types.property_filters.PropertyFilters"
    ]
    """<p>You can filter the request using various logical operators and a key-value format. For example:</p> <p> <code>{"key": "serverType", "value": "webServer"}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TabularConditions) -> dict:
    out: dict = {}
    if "order_by" in value:
        import capo_iottwinmaker.types.order_by_list

        out["orderBy"] = capo_iottwinmaker.types.order_by_list.serialize_json(
            value["order_by"]
        )
    if "property_filters" in value:
        import capo_iottwinmaker.types.property_filters

        out["propertyFilters"] = (
            capo_iottwinmaker.types.property_filters.serialize_json(
                value["property_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TabularConditions:
    out: TabularConditions = {}  # type: ignore[typeddict-item]
    if data.get("orderBy") is not None:
        import capo_iottwinmaker.types.order_by_list

        out["order_by"] = capo_iottwinmaker.types.order_by_list.deserialize_json(
            data["orderBy"]
        )
    if data.get("propertyFilters") is not None:
        import capo_iottwinmaker.types.property_filters

        out["property_filters"] = (
            capo_iottwinmaker.types.property_filters.deserialize_json(
                data["propertyFilters"]
            )
        )
    return out
