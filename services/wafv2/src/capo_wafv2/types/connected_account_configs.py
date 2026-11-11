"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_config

ConnectedAccountConfigs: TypeAlias = list[
    "capo_wafv2.types.connected_account_config.ConnectedAccountConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountConfigs) -> list:
    import capo_wafv2.types.connected_account_config

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.connected_account_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectedAccountConfigs:
    import capo_wafv2.types.connected_account_config

    out: ConnectedAccountConfigs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wafv2.types.connected_account_config.deserialize_aws_json_1_1(item)
        )
    return out
