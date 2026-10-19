"""Generated from Smithy shape ``com.amazonaws.qconnect#IntentInputData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.uuid


class IntentInputData(TypedDict, closed=True):
    intent_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentInputData) -> dict:
    out: dict = {}
    out["intentId"] = value["intent_id"]
    return out


def deserialize_json(data: dict) -> IntentInputData:
    out: IntentInputData = {}  # type: ignore[typeddict-item]
    if data.get("intentId") is not None:
        out["intent_id"] = data["intentId"]
    else:
        out["intent_id"] = ""
    return out
