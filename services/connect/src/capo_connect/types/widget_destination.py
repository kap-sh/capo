"""Generated from Smithy shape ``com.amazonaws.connect#WidgetDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.customer_profile_id
    import capo_connect.types.widget_id


class WidgetDestination(TypedDict, closed=True):
    widget_id: "capo_connect.types.widget_id.WidgetId"
    """<p>The identifier of the communication widget that delivers the notification to the customer's browser.</p>"""
    profile_id: "capo_connect.types.customer_profile_id.CustomerProfileId"
    """<p>The identifier of the customer profile associated with the browser session that should receive the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WidgetDestination) -> dict:
    out: dict = {}
    out["WidgetId"] = value["widget_id"]
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> WidgetDestination:
    out: WidgetDestination = {}  # type: ignore[typeddict-item]
    if data.get("WidgetId") is not None:
        out["widget_id"] = data["WidgetId"]
    else:
        out["widget_id"] = ""
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
