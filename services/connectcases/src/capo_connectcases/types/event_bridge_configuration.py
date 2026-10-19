"""Generated from Smithy shape ``com.amazonaws.connectcases#EventBridgeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.event_included_data


class EventBridgeConfiguration(TypedDict, closed=True):
    enabled: "bool"
    """<p>Indicates whether the to broadcast case event data to the customer.</p>"""
    included_data: NotRequired[
        "capo_connectcases.types.event_included_data.EventIncludedData"
    ]
    """<p>Details of what case and related item data is published through the case event stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "included_data" in value:
        import capo_connectcases.types.event_included_data

        out["includedData"] = (
            capo_connectcases.types.event_included_data.serialize_json(
                value["included_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventBridgeConfiguration:
    out: EventBridgeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("includedData") is not None:
        import capo_connectcases.types.event_included_data

        out["included_data"] = (
            capo_connectcases.types.event_included_data.deserialize_json(
                data["includedData"]
            )
        )
    return out
