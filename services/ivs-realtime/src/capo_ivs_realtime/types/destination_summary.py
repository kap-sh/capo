"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.destination_state
    import capo_ivs_realtime.types.string
    import capo_ivs_realtime.types.time


class DestinationSummary(TypedDict, closed=True):
    id: "capo_ivs_realtime.types.string.String"
    """<p>Unique identifier for this destination, assigned by IVS.</p>"""
    state: "capo_ivs_realtime.types.destination_state.DestinationState"
    """<p>State of the Composition Destination.</p>"""
    start_time: NotRequired["capo_ivs_realtime.types.time.Time"]
    """<p>UTC time of the destination start. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    end_time: NotRequired["capo_ivs_realtime.types.time.Time"]
    """<p>UTC time of the destination end. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["state"] = value["state"]
    if "start_time" in value:
        import capo_ivs_realtime.types.time

        out["startTime"] = capo_ivs_realtime.types.time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ivs_realtime.types.time

        out["endTime"] = capo_ivs_realtime.types.time.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> DestinationSummary:
    out: DestinationSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("startTime") is not None:
        import capo_ivs_realtime.types.time

        out["start_time"] = capo_ivs_realtime.types.time.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_ivs_realtime.types.time

        out["end_time"] = capo_ivs_realtime.types.time.deserialize_json(data["endTime"])
    return out
