"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountPaymentNetworks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_chain_config

ConnectedAccountPaymentNetworks: TypeAlias = list[
    "capo_wafv2.types.connected_account_chain_config.ConnectedAccountChainConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountPaymentNetworks) -> list:
    import capo_wafv2.types.connected_account_chain_config

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.connected_account_chain_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectedAccountPaymentNetworks:
    import capo_wafv2.types.connected_account_chain_config

    out: ConnectedAccountPaymentNetworks = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wafv2.types.connected_account_chain_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
