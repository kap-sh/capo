"""Generated from Smithy shape ``com.amazonaws.health#eventStatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_status_code

eventStatusCodeList: TypeAlias = list[
    "capo_health.types.event_status_code.eventStatusCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventStatusCodeList) -> list:
    import capo_health.types.event_status_code

    out: list = []
    for item in value:
        out.append(capo_health.types.event_status_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> eventStatusCodeList:
    import capo_health.types.event_status_code

    out: eventStatusCodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_status_code.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: eventStatusCodeList) -> list:
    import capo_health.types.event_status_code

    out: list = []
    for item in value:
        out.append(capo_health.types.event_status_code.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> eventStatusCodeList:
    import capo_health.types.event_status_code

    out: eventStatusCodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.event_status_code.deserialize_cbor(item))
    return out
