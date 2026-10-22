"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationStateFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_state_string

ExpressPrivateOfferConfigurationStateFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.express_private_offer_configuration_state_string.ExpressPrivateOfferConfigurationStateString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationStateFilterValueList) -> list:
    import capo_marketplace_catalog.types.express_private_offer_configuration_state_string

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_catalog.types.express_private_offer_configuration_state_string.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> ExpressPrivateOfferConfigurationStateFilterValueList:
    import capo_marketplace_catalog.types.express_private_offer_configuration_state_string

    out: ExpressPrivateOfferConfigurationStateFilterValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_catalog.types.express_private_offer_configuration_state_string.deserialize_json(
                item
            )
        )
    return out
