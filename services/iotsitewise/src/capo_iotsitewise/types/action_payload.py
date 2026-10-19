"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ActionPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_payload_string


class ActionPayload(TypedDict, closed=True):
    string_value: "capo_iotsitewise.types.action_payload_string.ActionPayloadString"
    """<p>The payload of the action in a JSON string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionPayload) -> dict:
    out: dict = {}
    out["stringValue"] = value["string_value"]
    return out


def deserialize_json(data: dict) -> ActionPayload:
    out: ActionPayload = {}  # type: ignore[typeddict-item]
    if data.get("stringValue") is not None:
        out["string_value"] = data["stringValue"]
    else:
        out["string_value"] = ""
    return out
