"""Generated from Smithy shape ``com.amazonaws.shield#DescribeSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.subscription


class DescribeSubscriptionResponse(TypedDict, closed=True):
    subscription: NotRequired["capo_shield.types.subscription.Subscription"]
    """<p>The Shield Advanced subscription details for an account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import capo_shield.types.subscription

        out["Subscription"] = capo_shield.types.subscription.serialize_aws_json_1_1(
            value["subscription"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscriptionResponse:
    out: DescribeSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Subscription") is not None:
        import capo_shield.types.subscription

        out["subscription"] = capo_shield.types.subscription.deserialize_aws_json_1_1(
            data["Subscription"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import capo_shield.types.subscription

        out["Subscription"] = capo_shield.types.subscription.serialize_cbor(
            value["subscription"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeSubscriptionResponse:
    out: DescribeSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Subscription") is not None:
        import capo_shield.types.subscription

        out["subscription"] = capo_shield.types.subscription.deserialize_cbor(
            data["Subscription"]
        )
    return out
