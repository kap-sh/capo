"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PriceIncrease``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.fixed_percentage
    import capo_marketplace_agreement.types.percentage_range


class PriceIncreaseFixedPercentageMember(TypedDict, closed=True):
    fixedPercentage: "capo_marketplace_agreement.types.fixed_percentage.FixedPercentage"


class PriceIncreasePercentageRangeMember(TypedDict, closed=True):
    percentageRange: "capo_marketplace_agreement.types.percentage_range.PercentageRange"


PriceIncrease: TypeAlias = (
    PriceIncreaseFixedPercentageMember
    | PriceIncreasePercentageRangeMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PriceIncrease) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PriceIncrease: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fixedPercentage" in value:
        import capo_marketplace_agreement.types.fixed_percentage

        return {
            "fixedPercentage": capo_marketplace_agreement.types.fixed_percentage.serialize_aws_json_1_0(
                value["fixedPercentage"]
            )
        }
    elif "percentageRange" in value:
        import capo_marketplace_agreement.types.percentage_range

        return {
            "percentageRange": capo_marketplace_agreement.types.percentage_range.serialize_aws_json_1_0(
                value["percentageRange"]
            )
        }
    else:
        raise SerializationError("PriceIncrease: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PriceIncrease:
    if data.get("fixedPercentage") is not None:
        import capo_marketplace_agreement.types.fixed_percentage

        return {
            "fixedPercentage": capo_marketplace_agreement.types.fixed_percentage.deserialize_aws_json_1_0(
                data["fixedPercentage"]
            )
        }
    elif data.get("percentageRange") is not None:
        import capo_marketplace_agreement.types.percentage_range

        return {
            "percentageRange": capo_marketplace_agreement.types.percentage_range.deserialize_aws_json_1_0(
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
