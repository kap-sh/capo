"""Generated from Smithy shape ``com.amazonaws.memorydb#RecurringChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.recurring_charge

RecurringChargeList: TypeAlias = list[
    "capo_memorydb.types.recurring_charge.RecurringCharge"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurringChargeList) -> list:
    import capo_memorydb.types.recurring_charge

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.recurring_charge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecurringChargeList:
    import capo_memorydb.types.recurring_charge

    out: RecurringChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.recurring_charge.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecurringChargeList) -> list:
    import capo_memorydb.types.recurring_charge

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.recurring_charge.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RecurringChargeList:
    import capo_memorydb.types.recurring_charge

    out: RecurringChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.recurring_charge.deserialize_cbor(item))
    return out
