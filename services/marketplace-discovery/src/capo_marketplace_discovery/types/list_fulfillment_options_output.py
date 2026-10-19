"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListFulfillmentOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.fulfillment_options_list
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.next_token


class ListFulfillmentOptionsOutput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    fulfillment_options: "capo_marketplace_discovery.types.fulfillment_options_list.FulfillmentOptionsList"
    """<p>The fulfillment options available for the product. Each option describes how the buyer can deploy or access the product.</p>"""
    next_token: NotRequired["capo_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFulfillmentOptionsOutput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    import capo_marketplace_discovery.types.fulfillment_options_list

    out["fulfillmentOptions"] = (
        capo_marketplace_discovery.types.fulfillment_options_list.serialize_json(
            value["fulfillment_options"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFulfillmentOptionsOutput:
    out: ListFulfillmentOptionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("fulfillmentOptions") is not None:
        import capo_marketplace_discovery.types.fulfillment_options_list

        out["fulfillment_options"] = (
            capo_marketplace_discovery.types.fulfillment_options_list.deserialize_json(
                data["fulfillmentOptions"]
            )
        )
    else:
        out["fulfillment_options"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
