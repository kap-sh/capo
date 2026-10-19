"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetBatchError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.read_set_id


class ReadSetBatchError(TypedDict, closed=True):
    id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The error's ID.</p>"""
    code: "str"
    """<p>The error's code.</p>"""
    message: "str"
    """<p>The error's message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetBatchError) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ReadSetBatchError:
    out: ReadSetBatchError = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
