"""Generated from Smithy shape ``com.amazonaws.health#entityStatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.entity_status_code

entityStatusCodeList: TypeAlias = list[
    "capo_health.types.entity_status_code.entityStatusCode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: entityStatusCodeList) -> list:
    import capo_health.types.entity_status_code

    out: list = []
    for item in value:
        out.append(capo_health.types.entity_status_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> entityStatusCodeList:
    import capo_health.types.entity_status_code

    out: entityStatusCodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.entity_status_code.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: entityStatusCodeList) -> list:
    import capo_health.types.entity_status_code

    out: list = []
    for item in value:
        out.append(capo_health.types.entity_status_code.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> entityStatusCodeList:
    import capo_health.types.entity_status_code

    out: entityStatusCodeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.entity_status_code.deserialize_cbor(item))
    return out
