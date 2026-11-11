"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DataAccessActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.data_access_action_name

DataAccessActionList: TypeAlias = list[
    "capo_cloudwatchomni.types.data_access_action_name.DataAccessActionName"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataAccessActionList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DataAccessActionList:
    return [item for item in data if item is not None]
