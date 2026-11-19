"""Generated from Smithy shape ``com.amazonaws.memorydb#EngineVersionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.engine_version_info

EngineVersionInfoList: TypeAlias = list[
    "capo_memorydb.types.engine_version_info.EngineVersionInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersionInfoList) -> list:
    import capo_memorydb.types.engine_version_info

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.engine_version_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EngineVersionInfoList:
    import capo_memorydb.types.engine_version_info

    out: EngineVersionInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.engine_version_info.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EngineVersionInfoList) -> list:
    import capo_memorydb.types.engine_version_info

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.engine_version_info.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EngineVersionInfoList:
    import capo_memorydb.types.engine_version_info

    out: EngineVersionInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.engine_version_info.deserialize_cbor(item))
    return out
