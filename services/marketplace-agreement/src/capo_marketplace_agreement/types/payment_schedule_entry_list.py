"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentScheduleEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.payment_schedule_entry

PaymentScheduleEntryList: TypeAlias = list[
    "capo_marketplace_agreement.types.payment_schedule_entry.PaymentScheduleEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentScheduleEntryList) -> list:
    import capo_marketplace_agreement.types.payment_schedule_entry

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.payment_schedule_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PaymentScheduleEntryList:
    import capo_marketplace_agreement.types.payment_schedule_entry

    out: PaymentScheduleEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.payment_schedule_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentScheduleEntryList) -> list:
    import capo_marketplace_agreement.types.payment_schedule_entry

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.payment_schedule_entry.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PaymentScheduleEntryList:
    import capo_marketplace_agreement.types.payment_schedule_entry

    out: PaymentScheduleEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.payment_schedule_entry.deserialize_cbor(
                item
            )
        )
    return out
