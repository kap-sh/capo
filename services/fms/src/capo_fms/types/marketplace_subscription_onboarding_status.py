"""Generated from Smithy shape ``com.amazonaws.fms#MarketplaceSubscriptionOnboardingStatus``."""

from typing import Literal, TypeAlias, cast

MarketplaceSubscriptionOnboardingStatus: TypeAlias = Literal[
    "NO_SUBSCRIPTION",
    "NOT_COMPLETE",
    "COMPLETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MarketplaceSubscriptionOnboardingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MarketplaceSubscriptionOnboardingStatus:
    return cast(MarketplaceSubscriptionOnboardingStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketplaceSubscriptionOnboardingStatus) -> str:
    return value


def deserialize_cbor(data: str) -> MarketplaceSubscriptionOnboardingStatus:
    return cast(MarketplaceSubscriptionOnboardingStatus, data)
