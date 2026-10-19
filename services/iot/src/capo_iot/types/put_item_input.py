"""Generated from Smithy shape ``com.amazonaws.iot#PutItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.table_name


class PutItemInput(TypedDict, closed=True):
    table_name: "capo_iot.types.table_name.TableName"
    """<p>The table where the message data will be written.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutItemInput) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    return out


def deserialize_json(data: dict) -> PutItemInput:
    out: PutItemInput = {}  # type: ignore[typeddict-item]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    return out
