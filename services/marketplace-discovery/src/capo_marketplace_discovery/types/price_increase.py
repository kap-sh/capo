"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PriceIncrease``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError, SerializationError
from capo_marketplace_discovery.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.fixed_percentage
    import capo_marketplace_discovery.types.percentage_range


class PriceIncreaseFixedPercentageMember(TypedDict, closed=True):
    fixedPercentage: "capo_marketplace_discovery.types.fixed_percentage.FixedPercentage"


class PriceIncreasePercentageRangeMember(TypedDict, closed=True):
    percentageRange: "capo_marketplace_discovery.types.percentage_range.PercentageRange"


PriceIncrease: TypeAlias = (
    PriceIncreaseFixedPercentageMember
    | PriceIncreasePercentageRangeMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PriceIncrease) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PriceIncrease: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fixedPercentage" in value:
        import capo_marketplace_discovery.types.fixed_percentage

        return {
            "fixedPercentage": capo_marketplace_discovery.types.fixed_percentage.serialize_json(
                value["fixedPercentage"]
            )
        }
    elif "percentageRange" in value:
        import capo_marketplace_discovery.types.percentage_range

        return {
            "percentageRange": capo_marketplace_discovery.types.percentage_range.serialize_json(
                value["percentageRange"]
            )
        }
    else:
        raise SerializationError("PriceIncrease: no variant present")


def deserialize_json(data: dict) -> PriceIncrease:
    if data.get("fixedPercentage") is not None:
        import capo_marketplace_discovery.types.fixed_percentage

        return {
            "fixedPercentage": capo_marketplace_discovery.types.fixed_percentage.deserialize_json(
                data["fixedPercentage"]
            )
        }
    elif data.get("percentageRange") is not None:
        import capo_marketplace_discovery.types.percentage_range

        return {
            "percentageRange": capo_marketplace_discovery.types.percentage_range.deserialize_json(
                data["percentageRange"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PriceIncrease: no recognized variant key")
