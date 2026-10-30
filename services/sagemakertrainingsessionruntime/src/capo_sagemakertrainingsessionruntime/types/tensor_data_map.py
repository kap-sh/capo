"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TensorDataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.tensor_data

TensorDataMap: TypeAlias = dict[
    "str", "capo_sagemakertrainingsessionruntime.types.tensor_data.TensorData"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TensorDataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sagemakertrainingsessionruntime.types.tensor_data

        out[key] = (
            capo_sagemakertrainingsessionruntime.types.tensor_data.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> TensorDataMap:
    out: TensorDataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_sagemakertrainingsessionruntime.types.tensor_data

        out[key] = (
            capo_sagemakertrainingsessionruntime.types.tensor_data.deserialize_json(
                value
            )
        )
    return out
