"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.service_update

ServiceUpdateList: TypeAlias = list["capo_memorydb.types.service_update.ServiceUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateList) -> list:
    import capo_memorydb.types.service_update

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.service_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceUpdateList:
    import capo_memorydb.types.service_update

    out: ServiceUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.service_update.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceUpdateList) -> list:
    import capo_memorydb.types.service_update

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.service_update.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServiceUpdateList:
    import capo_memorydb.types.service_update

    out: ServiceUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.service_update.deserialize_cbor(item))
    return out
