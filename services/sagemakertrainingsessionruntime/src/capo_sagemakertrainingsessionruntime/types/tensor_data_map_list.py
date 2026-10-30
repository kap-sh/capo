"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TensorDataMapList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.tensor_data_map

TensorDataMapList: TypeAlias = list[
    "capo_sagemakertrainingsessionruntime.types.tensor_data_map.TensorDataMap"
]


# --- restJson1 ser/de ---
def serialize_json(value: TensorDataMapList) -> list:
    import capo_sagemakertrainingsessionruntime.types.tensor_data_map

    out: list = []
    for item in value:
        out.append(
            capo_sagemakertrainingsessionruntime.types.tensor_data_map.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TensorDataMapList:
    import capo_sagemakertrainingsessionruntime.types.tensor_data_map

    out: TensorDataMapList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemakertrainingsessionruntime.types.tensor_data_map.deserialize_json(
                item
            )
        )
    return out
