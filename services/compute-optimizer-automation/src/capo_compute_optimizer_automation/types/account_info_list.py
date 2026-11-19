"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AccountInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.account_info

AccountInfoList: TypeAlias = list[
    "capo_compute_optimizer_automation.types.account_info.AccountInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountInfoList) -> list:
    import capo_compute_optimizer_automation.types.account_info

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.account_info.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccountInfoList:
    import capo_compute_optimizer_automation.types.account_info

    out: AccountInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.account_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountInfoList) -> list:
    import capo_compute_optimizer_automation.types.account_info

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.account_info.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AccountInfoList:
    import capo_compute_optimizer_automation.types.account_info

    out: AccountInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer_automation.types.account_info.deserialize_cbor(item)
        )
    return out
