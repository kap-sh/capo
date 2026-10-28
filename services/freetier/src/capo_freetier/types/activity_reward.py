"""Generated from Smithy shape ``com.amazonaws.freetier#ActivityReward``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_freetier.errors import DeserializationError, SerializationError
from capo_freetier.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_freetier.types.monetary_amount


class ActivityRewardCreditMember(TypedDict, closed=True):
    credit: "capo_freetier.types.monetary_amount.MonetaryAmount"


ActivityReward: TypeAlias = ActivityRewardCreditMember | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityReward) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ActivityReward: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "credit" in value:
        import capo_freetier.types.monetary_amount

        return {
            "credit": capo_freetier.types.monetary_amount.serialize_aws_json_1_0(
                value["credit"]
            )
        }
    else:
        raise SerializationError("ActivityReward: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ActivityReward:
    if data.get("credit") is not None:
        import capo_freetier.types.monetary_amount

        return {
            "credit": capo_freetier.types.monetary_amount.deserialize_aws_json_1_0(
                data["credit"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ActivityReward: no recognized variant key")
