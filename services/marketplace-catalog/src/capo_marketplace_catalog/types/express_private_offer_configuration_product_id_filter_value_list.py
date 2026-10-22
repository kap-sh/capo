"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationProductIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_product_id_string

ExpressPrivateOfferConfigurationProductIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.express_private_offer_configuration_product_id_string.ExpressPrivateOfferConfigurationProductIdString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ExpressPrivateOfferConfigurationProductIdFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ExpressPrivateOfferConfigurationProductIdFilterValueList:
    return [item for item in data if item is not None]
