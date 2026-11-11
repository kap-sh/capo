"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountPrices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_price

ConnectedAccountPrices: TypeAlias = list[
    "capo_wafv2.types.connected_account_price.ConnectedAccountPrice"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountPrices) -> list:
    import capo_wafv2.types.connected_account_price

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.connected_account_price.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectedAccountPrices:
    import capo_wafv2.types.connected_account_price

    out: ConnectedAccountPrices = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wafv2.types.connected_account_price.deserialize_aws_json_1_1(item)
        )
    return out
