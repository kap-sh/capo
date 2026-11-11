"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DataAccessTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.data_access_target

DataAccessTargetList: TypeAlias = list[
    "capo_cloudwatchomni.types.data_access_target.DataAccessTarget"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataAccessTargetList) -> list:
    import capo_cloudwatchomni.types.data_access_target

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.data_access_target.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DataAccessTargetList:
    import capo_cloudwatchomni.types.data_access_target

    out: DataAccessTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.data_access_target.deserialize_cbor(item))
    return out
