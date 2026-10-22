"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationStateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.express_private_offer_configuration_state_filter_value_list


class ExpressPrivateOfferConfigurationStateFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.express_private_offer_configuration_state_filter_value_list.ExpressPrivateOfferConfigurationStateFilterValueList"
    ]
    """<p>A list of <code>State</code> values to filter on. Valid values are <code>ACTIVE</code> and <code>INACTIVE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationStateFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.express_private_offer_configuration_state_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_state_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExpressPrivateOfferConfigurationStateFilter:
    out: ExpressPrivateOfferConfigurationStateFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.express_private_offer_configuration_state_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.express_private_offer_configuration_state_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
