"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter
    import capo_marketplace_catalog.types.express_private_offer_configuration_product_id_filter
    import capo_marketplace_catalog.types.express_private_offer_configuration_state_filter


class ExpressPrivateOfferConfigurationFilters(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter.ExpressPrivateOfferConfigurationEntityIdFilter"
    ]
    """<p>You can filter on the <code>EntityId</code> of an express private offer configuration.</p>"""
    product_id: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_product_id_filter.ExpressPrivateOfferConfigurationProductIdFilter"
    ]
    """<p>You can filter on the <code>ProductId</code> of an express private offer configuration.</p>"""
    state: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_state_filter.ExpressPrivateOfferConfigurationStateFilter"
    ]
    """<p>The state of the express private offer configuration to filter on. Valid values are the following:</p> <ul> <li> <p> <code>ACTIVE</code> – The configuration is active and you can use it to generate offers.</p> </li> <li> <p> <code>INACTIVE</code> – The configuration is deprecated or deleted.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter

        out["EntityId"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "product_id" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_product_id_filter

        out["ProductId"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_product_id_filter.serialize_json(
                value["product_id"]
            )
        )
    if "state" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_state_filter

        out["State"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_state_filter.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExpressPrivateOfferConfigurationFilters:
    out: ExpressPrivateOfferConfigurationFilters = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter

        out["entity_id"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if data.get("ProductId") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_product_id_filter

        out["product_id"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_product_id_filter.deserialize_json(
                data["ProductId"]
            )
        )
    if data.get("State") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_state_filter

        out["state"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_state_filter.deserialize_json(
                data["State"]
            )
        )
    return out
