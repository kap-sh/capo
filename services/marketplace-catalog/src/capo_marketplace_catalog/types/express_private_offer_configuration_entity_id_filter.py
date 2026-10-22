"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationEntityIdFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter_value_list


class ExpressPrivateOfferConfigurationEntityIdFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter_value_list.ExpressPrivateOfferConfigurationEntityIdFilterValueList"
    ]
    """<p>A list of <code>EntityId</code> values to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationEntityIdFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExpressPrivateOfferConfigurationEntityIdFilter:
    out: ExpressPrivateOfferConfigurationEntityIdFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_entity_id_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
