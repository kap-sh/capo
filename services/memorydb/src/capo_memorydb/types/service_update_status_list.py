"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.service_update_status

ServiceUpdateStatusList: TypeAlias = list[
    "capo_memorydb.types.service_update_status.ServiceUpdateStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateStatusList) -> list:
    import capo_memorydb.types.service_update_status

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.service_update_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceUpdateStatusList:
    import capo_memorydb.types.service_update_status

    out: ServiceUpdateStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.service_update_status.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceUpdateStatusList) -> list:
    import capo_memorydb.types.service_update_status

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.service_update_status.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServiceUpdateStatusList:
    import capo_memorydb.types.service_update_status

    out: ServiceUpdateStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.service_update_status.deserialize_cbor(item))
    return out
