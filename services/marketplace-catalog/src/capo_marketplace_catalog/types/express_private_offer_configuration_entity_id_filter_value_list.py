"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_string

ExpressPrivateOfferConfigurationEntityIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_string.ExpressPrivateOfferConfigurationEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ExpressPrivateOfferConfigurationEntityIdFilterValueList,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ExpressPrivateOfferConfigurationEntityIdFilterValueList:
    return [item for item in data if item is not None]
