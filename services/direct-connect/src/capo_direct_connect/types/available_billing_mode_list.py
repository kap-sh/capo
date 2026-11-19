"""Generated from Smithy shape ``com.amazonaws.directconnect#AvailableBillingModeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.available_billing_mode

AvailableBillingModeList: TypeAlias = list[
    "capo_direct_connect.types.available_billing_mode.AvailableBillingMode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailableBillingModeList) -> list:
    import capo_direct_connect.types.available_billing_mode

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.available_billing_mode.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AvailableBillingModeList:
    import capo_direct_connect.types.available_billing_mode

    out: AvailableBillingModeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.available_billing_mode.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AvailableBillingModeList) -> list:
    import capo_direct_connect.types.available_billing_mode

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.available_billing_mode.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AvailableBillingModeList:
    import capo_direct_connect.types.available_billing_mode

    out: AvailableBillingModeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.available_billing_mode.deserialize_cbor(item)
        )
    return out
