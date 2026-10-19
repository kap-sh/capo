"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionExecutionPayloadField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_payload_field_value


class ActionExecutionPayloadField(TypedDict, closed=True):
    value: "capo_qbusiness.types.action_payload_field_value.ActionPayloadFieldValue"
    """<p>The content of a user input field in an plugin action execution payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionExecutionPayloadField) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ActionExecutionPayloadField:
    out: ActionExecutionPayloadField = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = None
    return out
