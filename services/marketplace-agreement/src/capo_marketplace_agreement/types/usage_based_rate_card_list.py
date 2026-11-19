"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#UsageBasedRateCardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.usage_based_rate_card_item

UsageBasedRateCardList: TypeAlias = list[
    "capo_marketplace_agreement.types.usage_based_rate_card_item.UsageBasedRateCardItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageBasedRateCardList) -> list:
    import capo_marketplace_agreement.types.usage_based_rate_card_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.usage_based_rate_card_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UsageBasedRateCardList:
    import capo_marketplace_agreement.types.usage_based_rate_card_item

    out: UsageBasedRateCardList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.usage_based_rate_card_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UsageBasedRateCardList) -> list:
    import capo_marketplace_agreement.types.usage_based_rate_card_item

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.usage_based_rate_card_item.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> UsageBasedRateCardList:
    import capo_marketplace_agreement.types.usage_based_rate_card_item

    out: UsageBasedRateCardList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.usage_based_rate_card_item.deserialize_cbor(
                item
            )
        )
    return out
