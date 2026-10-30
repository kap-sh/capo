"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#TensorData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.integer_list


class TensorData(TypedDict, closed=True):
    data: "object"
    """<p>The raw tensor data as JSON. The format is determined by the <code>dtype</code> field: integer arrays for <code>int64</code>, floating-point arrays for <code>float32</code>.</p>"""
    dtype: "str"
    """<p>The data type of the tensor elements, such as <code>int64</code> or <code>float32</code>.</p>"""
    shape: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.integer_list.IntegerList"
    ]
    """<p>The dimensions of the tensor, such as [batch_size, seq_length].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TensorData) -> dict:
    out: dict = {}
    out["data"] = value["data"]
    out["dtype"] = value["dtype"]
    if "shape" in value:
        import capo_sagemakertrainingsessionruntime.types.integer_list

        out["shape"] = (
            capo_sagemakertrainingsessionruntime.types.integer_list.serialize_json(
                value["shape"]
            )
        )
    return out


def deserialize_json(data: dict) -> TensorData:
    out: TensorData = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    else:
        out["data"] = None
    if data.get("dtype") is not None:
        out["dtype"] = data["dtype"]
    else:
        out["dtype"] = ""
    if data.get("shape") is not None:
        import capo_sagemakertrainingsessionruntime.types.integer_list

        out["shape"] = (
            capo_sagemakertrainingsessionruntime.types.integer_list.deserialize_json(
                data["shape"]
            )
        )
    return out
