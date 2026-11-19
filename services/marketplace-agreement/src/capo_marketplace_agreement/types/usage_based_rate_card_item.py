"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#UsageBasedRateCardItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.rate_card_list


class UsageBasedRateCardItem(TypedDict, closed=True):
    rate_card: NotRequired[
        "capo_marketplace_agreement.types.rate_card_list.RateCardList"
    ]
    """<p>Defines the per unit rates for product dimensions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageBasedRateCardItem) -> dict:
    out: dict = {}
    if "rate_card" in value:
        import capo_marketplace_agreement.types.rate_card_list

        out["rateCard"] = (
            capo_marketplace_agreement.types.rate_card_list.serialize_aws_json_1_0(
                value["rate_card"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UsageBasedRateCardItem:
    out: UsageBasedRateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("rateCard") is not None:
        import capo_marketplace_agreement.types.rate_card_list

        out["rate_card"] = (
            capo_marketplace_agreement.types.rate_card_list.deserialize_aws_json_1_0(
                data["rateCard"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsageBasedRateCardItem) -> dict:
    out: dict = {}
    if "rate_card" in value:
        import capo_marketplace_agreement.types.rate_card_list

        out["rateCard"] = (
            capo_marketplace_agreement.types.rate_card_list.serialize_cbor(
                value["rate_card"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UsageBasedRateCardItem:
    out: UsageBasedRateCardItem = {}  # type: ignore[typeddict-item]
    if data.get("rateCard") is not None:
        import capo_marketplace_agreement.types.rate_card_list

        out["rate_card"] = (
            capo_marketplace_agreement.types.rate_card_list.deserialize_cbor(
                data["rateCard"]
            )
        )
    return out
