"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#OfferVisibilityScope``."""

from typing import Literal, TypeAlias, cast

OfferVisibilityScope: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OfferVisibilityScope) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OfferVisibilityScope:
    return cast(OfferVisibilityScope, data)
