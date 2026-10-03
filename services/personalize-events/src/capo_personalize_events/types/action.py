"""Generated from Smithy shape ``com.amazonaws.personalizeevents#Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize_events.types.string_type
    import capo_personalize_events.types.synthesized_json_action_properties


class Action(TypedDict, closed=True):
    action_id: "capo_personalize_events.types.string_type.StringType"
    """<p>The ID associated with the action.</p>"""
    properties: NotRequired[
        "capo_personalize_events.types.synthesized_json_action_properties.SynthesizedJsonActionProperties"
    ]
    r"""<p>A string map of action-specific metadata. Each element in the map consists of a key-value pair. For example, <code>{"value": "100"}</code>.</p> <p>The keys use camel case names that match the fields in the schema for the Actions dataset. In the previous example, the <code>value</code> matches the 'VALUE' field defined in the Actions schema. For categorical string data, to include multiple categories for a single action, separate each category with a pipe separator (<code>|</code>). For example, <code>\"Deluxe|Premium\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    if "properties" in value:
        out["properties"] = value["properties"]
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        raise DeserializationError("Action.action_id required")
    if data.get("properties") is not None:
        out["properties"] = data["properties"]
    return out
