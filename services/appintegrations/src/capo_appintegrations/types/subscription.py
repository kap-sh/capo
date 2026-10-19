"""Generated from Smithy shape ``com.amazonaws.appintegrations#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.description
    import capo_appintegrations.types.event_name


class Subscription(TypedDict, closed=True):
    event: "capo_appintegrations.types.event_name.EventName"
    """<p>The name of the subscription.</p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The description of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    out["Event"] = value["event"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if data.get("Event") is not None:
        out["event"] = data["Event"]
    else:
        out["event"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
