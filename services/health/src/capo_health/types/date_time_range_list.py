"""Generated from Smithy shape ``com.amazonaws.health#dateTimeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.date_time_range

dateTimeRangeList: TypeAlias = list["capo_health.types.date_time_range.DateTimeRange"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: dateTimeRangeList) -> list:
    import capo_health.types.date_time_range

    out: list = []
    for item in value:
        out.append(capo_health.types.date_time_range.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> dateTimeRangeList:
    import capo_health.types.date_time_range

    out: dateTimeRangeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.date_time_range.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: dateTimeRangeList) -> list:
    import capo_health.types.date_time_range

    out: list = []
    for item in value:
        out.append(capo_health.types.date_time_range.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> dateTimeRangeList:
    import capo_health.types.date_time_range

    out: dateTimeRangeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.date_time_range.deserialize_cbor(item))
    return out
