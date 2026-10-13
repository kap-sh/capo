"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_list
    import capo_billingconductor.types.token


class ListCustomLineItemsOutput(TypedDict, closed=True):
    custom_line_items: NotRequired[
        "capo_billingconductor.types.custom_line_item_list.CustomLineItemList"
    ]
    """<p> A list of <code>FreeFormLineItemListElements</code> received. </p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemsOutput) -> dict:
    out: dict = {}
    if "custom_line_items" in value:
        import capo_billingconductor.types.custom_line_item_list

        out["CustomLineItems"] = (
            capo_billingconductor.types.custom_line_item_list.serialize_json(
                value["custom_line_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomLineItemsOutput:
    out: ListCustomLineItemsOutput = {}  # type: ignore[typeddict-item]
    if data.get("CustomLineItems") is not None:
        import capo_billingconductor.types.custom_line_item_list

        out["custom_line_items"] = (
            capo_billingconductor.types.custom_line_item_list.deserialize_json(
                data["CustomLineItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListCustomLineItemsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_line_items" in value:
        import capo_billingconductor.types.custom_line_item_list

        out["custom_line_items"] = (
            capo_billingconductor.types.custom_line_item_list.redact_sensitive(
                value["custom_line_items"]
            )
        )
    return out
