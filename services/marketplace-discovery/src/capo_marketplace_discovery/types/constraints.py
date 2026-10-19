"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#Constraints``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.rate_card_constraint_type


class Constraints(TypedDict, closed=True):
    multiple_dimension_selection: "capo_marketplace_discovery.types.rate_card_constraint_type.RateCardConstraintType"
    """<p>Whether the buyer can select multiple dimensions. Values are <code>Allowed</code> or <code>Disallowed</code>.</p>"""
    quantity_configuration: "capo_marketplace_discovery.types.rate_card_constraint_type.RateCardConstraintType"
    """<p>Whether the buyer can configure quantities. Values are <code>Allowed</code> or <code>Disallowed</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Constraints) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.rate_card_constraint_type

    out["multipleDimensionSelection"] = (
        capo_marketplace_discovery.types.rate_card_constraint_type.serialize_json(
            value["multiple_dimension_selection"]
        )
    )
    import capo_marketplace_discovery.types.rate_card_constraint_type

    out["quantityConfiguration"] = (
        capo_marketplace_discovery.types.rate_card_constraint_type.serialize_json(
            value["quantity_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> Constraints:
    out: Constraints = {}  # type: ignore[typeddict-item]
    if data.get("multipleDimensionSelection") is not None:
        import capo_marketplace_discovery.types.rate_card_constraint_type

        out["multiple_dimension_selection"] = (
            capo_marketplace_discovery.types.rate_card_constraint_type.deserialize_json(
                data["multipleDimensionSelection"]
            )
        )
    else:
        import typing

        out["multiple_dimension_selection"] = typing.cast(
            "capo_marketplace_discovery.types.rate_card_constraint_type.RateCardConstraintType",
            "",
        )
    if data.get("quantityConfiguration") is not None:
        import capo_marketplace_discovery.types.rate_card_constraint_type

        out["quantity_configuration"] = (
            capo_marketplace_discovery.types.rate_card_constraint_type.deserialize_json(
                data["quantityConfiguration"]
            )
        )
    else:
        import typing

        out["quantity_configuration"] = typing.cast(
            "capo_marketplace_discovery.types.rate_card_constraint_type.RateCardConstraintType",
            "",
        )
    return out
