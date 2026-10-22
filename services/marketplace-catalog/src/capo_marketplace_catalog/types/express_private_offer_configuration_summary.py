"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_product_id_string
    import capo_marketplace_catalog.types.express_private_offer_configuration_state_string


class ExpressPrivateOfferConfigurationSummary(TypedDict, closed=True):
    product_id: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_product_id_string.ExpressPrivateOfferConfigurationProductIdString"
    ]
    """<p>The product ID associated with the express private offer configuration.</p>"""
    state: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_state_string.ExpressPrivateOfferConfigurationStateString"
    ]
    """<p>The state of the express private offer configuration. Valid values are the following:</p> <ul> <li> <p> <code>ACTIVE</code> – The configuration is active and you can use it to generate offers.</p> </li> <li> <p> <code>INACTIVE</code> – The configuration is deprecated or deleted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationSummary) -> dict:
    out: dict = {}
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "state" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_state_string

        out["State"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_state_string.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExpressPrivateOfferConfigurationSummary:
    out: ExpressPrivateOfferConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("State") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_state_string

        out["state"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_state_string.deserialize_json(
                data["State"]
            )
        )
    return out
