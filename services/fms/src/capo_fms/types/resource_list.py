"""Generated from Smithy shape ``com.amazonaws.fms#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.resource

ResourceList: TypeAlias = list["capo_fms.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceList) -> list:
    import capo_fms.types.resource

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceList:
    import capo_fms.types.resource

    out: ResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.resource.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceList) -> list:
    import capo_fms.types.resource

    out: list = []
    for item in value:
        out.append(capo_fms.types.resource.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResourceList:
    import capo_fms.types.resource

    out: ResourceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.resource.deserialize_cbor(item))
    return out
